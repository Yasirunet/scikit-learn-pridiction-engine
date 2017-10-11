from flask import Flask, jsonify ,request
#from sklearn.externals import joblib



app = Flask(__name__)


@app.route('/',methods=['POST'])
def test():
	#restfull service
	##get value from json reqvest
	data = request.get_json()
	name = data['name']
	test_list = data['val']
	##get pridictions from model
	import another_module
        a = test_list
        var = another_module.main(a)
 	#return values
	return jsonify({'request_stat':'success!','name':name , 'your valuues': test_list ,'prediction':var})

	
if __name__ == '__main__':
    app.run()
