l1 = list(map(int,input().split(" ")))
l1.sort(reverse = True)

# for i_index,i in enumerate(l1[0:-1]):
    # l.append((i,l1[i_index+1]))

l=[(i,l1[i_index+1]) for i_index,i in enumerate(l1[0:-1])]
print(l)