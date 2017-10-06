#!/usr/bin/env python
from sklearn.externals import joblib
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

clf1 = joblib.load('model2.pkl')


def main():

    iris = datasets.load_iris()

    x = iris.data
    y = iris.target
	
    clf1 = joblib.load('model2.pkl')

    #knn = KNeighborsClassifier()
    #clf = knn.fit(x,y)
    test_list = [10,3,2,10]
	
    get_pre = clf1.predict([test_list])
    pre = get_pre[0]
	
    pred1 = iris.target_names[pre]
    return pred1
#print(get_value())


if __name__ == "__main__":
    main()