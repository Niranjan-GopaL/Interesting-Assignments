n=int(input())
d={}
# accepting inputs in dictionary
for i in range(n):
    [k,v] = input().split(":")
    d[k]=int(v)

# createing a list of unique values of dictionary by using the property of a set
s = list(set(d.values()))

'''turns out that to use join function the elements of the iterable (here list must ALSO BE STRING so we are converting each element to string'''

# print(" ".join(s)) As is won't work 

s=list(map(str,s))
print(" ".join(s))