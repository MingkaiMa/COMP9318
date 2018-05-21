from sklearn import svm
import numpy as np



X  = np.array([[3, 3],
               [4, 3],
               [1, 1]])

Y = np.array([1, 1, -1])


clf = svm.SVC(kernel = 'poly')
clf.fit(X, Y)


