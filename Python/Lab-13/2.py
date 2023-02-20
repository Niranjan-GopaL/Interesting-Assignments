l1 = list(map(int,input().split(" ")))
l1.sort()
l1 = list(set(l1))

l = []

# for i_index,i in enumerate(l1[0:-2]):
#     for j_index,j in enumerate(l1[i_index+1:]):
#         l.append((i,j))

l = [(i,j) for i_index,i in enumerate(l1[0:-2]) for j_index,j in enumerate(l1[i_index+1:])  ]
newl = [sublist for sublist in l if sublist[0]*sublist[1] % 2 == 0]
print(newl)


# [print(i*x,end=' ') for i in l1]


'''
Basically when you have questions like this :

1)FIRST WRITE THE NESTED LOOPS
2)THEN CONVERT INTO LIST COMPHREHENSION
https://www.youtube.com/watch?v=AzKV9NbtNJ0 watch this to know basics
https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/

Important techniques used:

->converting nested for loop to list comprehension
-> l1 = list(set(l1))
-> enumerate and slicing
'''