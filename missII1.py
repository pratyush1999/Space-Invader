from missile import *
class missI1(missile):
	def __init__(self,x,y):	
		super(missI1,self).__init__(x,y)
		self.speed=2
		self.h=10