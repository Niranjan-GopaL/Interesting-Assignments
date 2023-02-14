l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
print(f'{[i for i in l1 if i in l2]}')
