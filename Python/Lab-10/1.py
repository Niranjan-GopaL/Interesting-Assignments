import math
#function to check if there is a number is Prime , returns true if it is , else false .
def isPrime(n):
    if n == 1 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# Taking in input
l=[]
newL=[]
n=int(input())
for i in range(n):
    l.append(int(input()))

# removing all the composite numbers (numbers that are not prime)
for i in range(n):
    if isPrime(l[i]):
        newL.append(l[i])
print(newL)

