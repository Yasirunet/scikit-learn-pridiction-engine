from flask import Flask 
#from sklearn.externals import joblib

#clf = joblib.load('modle.pkl')

app = Flask(__name__)


@app.route('/')
def test():
	#test_list = [5,3,2,0]
	#get_pre = clf.predict([test_list])
	#pre = get_pre[0]
	return "pre"


	
if __name__ == '__main__':
	app.run()
