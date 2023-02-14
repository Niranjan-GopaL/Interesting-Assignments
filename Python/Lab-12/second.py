l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
common_values = list(filter(lambda x: x in l2, l1))

[print(i,end=' ') for i in common_values]
