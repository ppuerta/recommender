# -*- coding: utf-8; -*-

import nltk
nltk.download('punkt')
import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
import string


__author__ = 'puertaballesteros.pedro@gmail.com (Pedro Puertas)'

stop_words_en = set(stopwords.words('english'))
stop_words_es = set(stopwords.words('spanish'))
data = pd.read_csv('../data/21B_tag_views_dataset.csv')
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
data.to_csv('../data/dataset_keywords.csv', index=False)
