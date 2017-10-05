from flask import Flask 
#from sklearn.externals import joblib



app = Flask(__name__)


@app.route('/')
def test():
 	import another_module
	value = another_module.get_value(34)
	return value


	
if __name__ == '__main__':
    app.run()
