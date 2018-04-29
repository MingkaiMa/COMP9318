from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm



corpus = ['I love love to beijing tiananmen',
          'I like Pudong',
          'Barcelone best']


test = ['What the hell',
        'No best']


vectorizer = CountVectorizer(stop_words = None)

vectorizer.fit(corpus)

train_data1 = vectorizer.transform(corpus)


test_data = vectorizer.transform(test)
