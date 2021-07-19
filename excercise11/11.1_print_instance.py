"""In python we call self instead of
   this and here Ididn't created all objects I created
   one and used all classes using self"""

# Base class
class A:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class
class B(A):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		A.__init__(self, grandfathername)

# Derived class
class C(B):
	def __init__(self,sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		B.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

# Driver code
s1 = C('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
