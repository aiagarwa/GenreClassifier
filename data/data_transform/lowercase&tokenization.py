import pandas as pd
import numpy as np
import csv
from nltk import word_tokenize
"""
column_names = ['Title', 'Artist', 'Featuring','Featured_Artist','Lyrics','Tags','Genre']
data = pd.read_csv('dataset.csv', names=column_names)
X = data.iloc[:,4].values.astype('U')


for i in range(1,5546):
    X[i] = str.lower(X[i])
    a = word_tokenize(X[i])
    with open('tokenization.csv', 'a', newline='', encoding='utf-8') as csvfile:  # open new csv file
        writer = csv.writer(csvfile)  # create csv writer
        writer.writerow([a]) # each lyrics per row
"""
f1 = pd.read_csv('dataset.csv')
f2 = pd.read_csv('tokenization.csv')
file = [f1,f2]
train = pd.concat(file,axis=1)
train.to_csv("dataset_tokenized" + ".csv", index=0, sep=',')

