first_row = list(map(int,input().split(" ")))
lol=[]
lol.append(first_row)
for i in range(len(first_row)-1):
    row = list(map(int,input().split(" ")))
    lol.append(row)

matrix_transpose = [[row[i] for row in lol] for i in range(len(lol))]

for i in matrix_transpose:
    [print(j,end=' ') for j in i]
    print()


