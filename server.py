import collections
import random
import pandas as pd
import nltk
import random
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.classify import DecisionTreeClassifier
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from flask import (
	Flask,
	request,
	render_template)


factory = StemmerFactory()
stemmer = factory.create_stemmer()

def cleansing(data):
    doc = []
    for key in other.keys():
        for judul in other[key]:
            title = judul.replace('\n', '') 
            title = judul.replace('\t', '')
            stem = stemmer.stem(title)
            title = nltk.word_tokenize(stem)
            doc.append((list(title), key))
    return doc

def document_features(document):
	document_words = set(document)
	features = {}
	for word in document_words:
	    features['contains(%s)' % word] = (True)
	return features

training_set = pd.read_excel('D:/Boombastis/Data/Data/data.xlsx')

data = {'Inspirasi':[],
       'UnikAneh':[],
       'Travel':[],
       'Tips':[],
       'Hiburan':[],
       'Olahraga':[],
       'Trends':[],
       'Block':[],
       'Entertainment':[]}

#train
Inspirasi = training_set.loc[training_set['CATEGORY'] == 'Inspirasi']
UnikAneh = training_set.loc[training_set['CATEGORY'] == 'UnikAneh']
Travel = training_set.loc[training_set['CATEGORY'] == 'Travel']
Tips = training_set.loc[training_set['CATEGORY'] == 'Tips']
Hiburan = training_set.loc[training_set['CATEGORY'] == 'Hiburan']
Olahraga = training_set.loc[training_set['CATEGORY'] == 'Olahraga']
Trends = training_set.loc[training_set['CATEGORY'] == 'Trends']
Block = training_set.loc[training_set['CATEGORY'] == 'Block']
Entertainment = training_set.loc[training_set['CATEGORY'] == 'Entertainment']

other = {}
other['Inspirasi'] = list(Inspirasi['TITLE'])
other['UnikAneh'] = list(UnikAneh['TITLE'])
other['Travel'] = list(Travel['TITLE'])
other['Tips'] = list(Tips['TITLE'])
other['Hiburan'] = list(Hiburan['TITLE'])
other['Olahraga'] = list(Olahraga['TITLE'])
other['Trends'] = list(Trends['TITLE'])
other['Block'] = list(Block['TITLE'])
other['Entertainment'] = list(Entertainment['TITLE'])

doc = cleansing(other)

featuresets = [(document_features(d), c) for (d,c) in doc]
random.shuffle(featuresets)

train_feats, test_feats = featuresets[:int(len(featuresets)*0.8)], featuresets[int(len(featuresets)*0.8):]
nb_classifier = NaiveBayesClassifier.train(train_feats)

# print(accuracy(nb_classifier, test_feats))

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
	if request.method == "POST":
		data = request.form['judul']
		doc = document_features(data)
		result = nb_classifier.classify(doc)

		return result


if __name__ == "__main__":
   app.run()