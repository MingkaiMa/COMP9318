import numpy as np
X = np.array([[[-1], [-1]], [[-2], [-1]], [[1], [1]], [[200], [1]]])
#y = np.array([1, 1, 2, 2])
y = [1,1,2,2]
from sklearn.svm import SVC
clf = SVC()
clf.fit(X, y)


print(clf.decision_function(X))
print(clf.predict(X))
