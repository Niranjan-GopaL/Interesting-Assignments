#initialization
l=[]
newL=[]

#accepting the input list
n=int(input())
for i in range(n):
    l.append(int(input()))

#reversing the list
for i in l[::-1]:
    newL.append(i)

print(newL)

