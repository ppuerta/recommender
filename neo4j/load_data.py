# -*- coding: utf-8; -*-

from py2neo import Graph

__author__ = 'puertaballesteros.pedro@gmail.com (Pedro Puertas)'

graph = Graph('bolt://localhost:7687')

load_data = graph.run("""\

LOAD CSV WITH HEADERS FROM 'file:///dataset_keywords.csv' AS line
WITH line where not line.user_id is null
MERGE (user:User { id: line.user_id})
MERGE (product:Product { id:line.tag_id, product_name:line.product_name, keyword:line.keyword })
MERGE (user)-[:VIEW]->(product)
""")
