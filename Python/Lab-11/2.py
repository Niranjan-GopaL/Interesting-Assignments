class Rectangle:

    # if you begin any attribute with __ then that means that it is a aprivate attribute
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    
    # defining class , methodes 
    @classmethod
    def from_square(cls, side_length):
        return cls(side_length, side_length)
    
    def __del__(self):
        print("An instance of Rectangle has been deleted")

length, width = map(int, input().split())
r = Rectangle(length, width)
print(r.area(), r.perimeter())

s = Rectangle.from_square(10)
print(s.area(), s.perimeter())

del r, s