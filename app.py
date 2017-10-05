from flask import Flask 
from sklearn.externals import joblib



app = Flask(__name__)

clf = joblib.load('modle.pkl')

@app.route('/')
def test():
	test_list = [5,3,2,0]
	get_pre = clf.predict([test_list])
	pre = get_pre[0]
	print(pre)


	
if __name__ == '__main__':
	app.run()
