from sklearn.externals import joblib
clf = joblib.load('model.pkl')

class make_predictions:

	def __init__(self,a,b,c,d):
		self.val1 = a
		self.val2 = b
		self.val3 = c
		self.val4 = d

	def make_a_list(self):
		test_list = [self.val1,self.val2,self.val3,self.val4]
		return test_list

	def make_predict_out(self):
		#get data from make_a_list
		test_list = self.make_a_list()
		print("you enterd data is :",test_list)
		#make pridictions
		print(clf.predict([test_list]))


		
d1 = int(input('enter value one:'))
d2 = int(input('enter value two:'))
d3 = int(input('enter value two:'))
d4 = int(input('etere value three:'))

test1 = make_predictions(d1,d2,d3,d4)
test1.make_a_list()
test1.make_predict_out()
		
