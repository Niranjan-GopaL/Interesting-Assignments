class Rectangle:

	def __init__(self, width, height):
		self.width=width
		self.height=height   

	def area(self):
		return self.width*self.height

	def perimeter(self):
		return 2*(self.width + self.height)

[h,w]=map(int,input().split())
rect=Rectangle(w,h)
print(rect.area())
print(rect.perimeter()	)
