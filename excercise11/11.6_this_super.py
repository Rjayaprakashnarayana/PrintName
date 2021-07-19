
# super and self is used in methods of class
# Python program to demonstrate
# super function


class Animals:
	
	# Initializing constructor
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	
	def isMammal(self):
		if self.mammals:# here we used self instead of this in methods of class
			print("It is a mammal.")
	
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
	
class Dogs(Animals):
	def __init__(self):
		super().__init__()# here super is used to call the parent class constructor

	def isMammal(self):
		super().isMammal()# here we used self instead of this in methods of class

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()
