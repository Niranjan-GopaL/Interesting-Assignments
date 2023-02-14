cube = lambda x : x*x*x
line = list(map(int,input().split(" ")))
line = list(map(cube , line))
[print(i,end=' ') for i in line]
