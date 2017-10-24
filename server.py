import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from flask import (
	Flask,
	request,
	render_template)


df = pd.read_excel('D:/Boombastis/Data/data_aggregator/new.xlsx')

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['judul'], 
                                                    df['num_cat'], 
                                                    random_state=0)

# Fit the CountVectorizer to the training data
vect = CountVectorizer().fit(X_train)

# transform the documents in the training data to a document-term matrix
X_train_vectorized = vect.transform(X_train)

# Train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Predict the transformed test documents
predictions = model.predict(vect.transform(X_test))

# These reviews are now correctly identified
def run(judul):
	# judul = 'Kata Plt Dirjen Hubla soal Suap Rp 20 Miliar yang Dibongkar KPK'
	res = model.predict(vect.transform([judul]))
	return res

aplikasi = Flask(__name__)

@aplikasi.route("/prediksi", methods = ["POST"])
def prediksi():
	if request.method == "POST":
		judul = request.form['judul']
		data = run(judul)
		print(data)
		return render_template("result.html", data = data)

if __name__ == "__main__":
   aplikasi.run()