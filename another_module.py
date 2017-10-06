#!/usr/bin/env python
from sklearn.externals import joblib

clf = joblib.load('model.pkl')


def get_value(*args):
	test_list = [5,3,2,0]
	
	get_pre = clf.predict([test_list])
	pre = get_pre[0]
	
        return  pre + ":".join(map(str, args))

def main(argv):
    print(get_value(*argv[1:]))

if __name__ == "__main__":
    import sys
    main(sys.argv)
