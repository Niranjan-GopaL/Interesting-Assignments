l1 = list(map(int,input().split(",")))
l1.sort(reverse = True)

# for i_index,i in enumerate(l1[0:-1]):
    # l.append((l1[i_index+1],i))

l=[(l1[i_index+1],i) for i_index,i in enumerate(l1[0:-1])]
print(l)

'''
Sample Input
1,2,3,4

Sample Output
[(3, 4), (2, 3), (1, 2)]
'''