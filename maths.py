class Math():
	def __init__(self,a,b):
		self.val1 = a
		self.val2 = b
		self.result=0
	def printresult(self):
		print(self.result)
	def add(self):
		self.result = self.val1 + self.val2
		self.printresult()
	def multiply(self):
		self.result = self.val1 * self.val2
		self.printresult()
calc = Math(2,3)
calc.add()
calc.multiply()
