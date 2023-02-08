sclass Complex:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)

    def __sub__(self,other):
        return Complex(self.real - other.real , self.imag - other.imag)

    def __mul__(self,other):
        return Complex(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)

inp1=input()
inp2=input()

z1 = Complex(int(inp1.split()[0]),int(inp2.split()[1]))
z2 = Complex(int(inp2.split()[0]),int(inp2.split()[1]))

print(z1+z2)
print(z1-z2)
print(z1*z2)
