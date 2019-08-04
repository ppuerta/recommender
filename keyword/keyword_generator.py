# -*- coding: utf-8; -*-

import nltk

nltk.download('punkt')
import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import requests

__author__ = 'puertaballesteros.pedro@gmail.com (Pedro Puertas)'

stop_words_en = set(stopwords.words('english'))
stop_words_es = set(stopwords.words('spanish'))
url = 'https://s3-eu-west-1.amazonaws.com/dev-21b-redshift-populator/tech_test/21B_tag_views_dataset.csv'
s = requests.get(url).content
data = pd.read_csv(s)
keywords = []

for row in data['product_name']:
    word_tokens = word_tokenize(row.lower())

    # Delete spanish stopwords
    filtered_sentence = [w for w in word_tokens if not w in stop_words_es]
    # Delete english stopwords
    filtered_sentence = [w for w in filtered_sentence if not w in stop_words_en]
    # Delete punctuation
    filtered_sentence = [w for w in filtered_sentence if not w in string.punctuation]
    keywords.append(filtered_sentence)

data["keyword"] = keywords
data.to_csv('~/neo4j/import/dataset_keywords.csv', index=False)
