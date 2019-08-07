# -*- coding: utf-8; -*-

from py2neo import Graph
import pandas as pd
from difflib import SequenceMatcher

__author__ = 'puertaballesteros.pedro@gmail.com (Pedro Puertas)'

graph = Graph('bolt://localhost:7687')

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

item = graph.run("""\
MATCH (originalItem:Product {id: 'ff0d3fb21c00bc33f71187a2beec389e9eff5332'})
RETURN originalItem.id, originalItem.product_name, originalItem.keyword
LIMIT 1
""").to_data_frame()

recommendations = graph.run("""\
MATCH (originalItem:Product {id: 'ff0d3fb21c00bc33f71187a2beec389e9eff5332'})<-[:VIEW]-(otherUser:User)-[:VIEW]->(alsoVisit:Product)
WHERE alsoVisit <> originalItem
RETURN alsoVisit.id, alsoVisit.product_name, alsoVisit.keyword, count(alsoVisit) as frequency
ORDER BY frequency DESC
LIMIT 25
""").to_data_frame()

similarities = []

for index, row in recommendations.iterrows():
    similarities.append(similar(str(row['alsoVisit.keyword']), str(item['originalItem.keyword'])))

recommendations['similarity'] = similarities
recommendations['calculation'] = recommendations['similarity'] * recommendations['frequency']
recommendations = recommendations.sort_values(by='calculation', ascending=False)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(recommendations[:10])
