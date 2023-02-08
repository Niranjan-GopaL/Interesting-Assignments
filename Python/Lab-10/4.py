
#Initializing variables
l=[]
newL=[]
sum=0


#accepting the list
n=int(input())
for i in range(n):
    l.append(int(input()))

#forming the accumulator list
for i in l:
    sum+=i
    newL.append(sum)

print(newL)