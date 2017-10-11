from flask import Flask 
#from sklearn.externals import joblib



app = Flask(__name__)


@app.route('/')
def test():
    import another_module
    a = 35
    var = another_module.main(a)
    return var
	
if __name__ == '__main__':
    app.run()
