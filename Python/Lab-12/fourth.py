line = input().split(" ")
ans = filter(lambda x: len(x)>3,line)
[print(i,end=' ') for i in ans]
