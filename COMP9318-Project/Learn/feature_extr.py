from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm



corpus = ['I am love - , . love to beijing tiananmen',
          'I like Pudong',
          'You Barcelone best']


test = ['What the hell',
        'No best']


vectorizer = CountVectorizer(min_df=1, token_pattern='(?u)\\b\\w+\\b',
                             stop_words = None)

vectorizer.fit(corpus)

train_data1 = vectorizer.transform(corpus)


test_data = vectorizer.transform(test)

vectorizer.get_feature_names()
