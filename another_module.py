#!/usr/bin/env python
from sklearn.externals import joblib
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#clf1 = joblib.load('model2.pkl')


def main(arg):
    #b = test_list 
    #arg1 = str(arg)
    iris = datasets.load_iris()

    x = iris.data
    y = iris.target


    knn = KNeighborsClassifier()
    clf = knn.fit(x,y)
    test_list = arg
	
    get_pre = clf.predict([test_list])
    pre = get_pre[0]
	
    pred1 = iris.target_names[pre]
    text = pred1 
    return text
#print(get_value())


if __name__ == "__main__":
    main(b)