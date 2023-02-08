lol=[]
l=[]

# accepting the list
n=int(input())
for i in range(n):
    lol.append(eval(input()))

# flattening the lol (list of lists)
for i in lol:
    for j in i:
        l.append(j)

print(l)