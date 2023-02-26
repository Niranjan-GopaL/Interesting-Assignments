board=l=[0,0,0,0,0,0,0,0,0]
print("Enter the sudoku board like in the following example :")
print("""
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Enter each row of the board AS A LIST in the format as shown.
ONE ROW AT A TIME will be appended to a larger list called board
""")

print(""))
for i in range(9):
    board = board.append(input())

for 
for i in board:
    for j in i:
        if j != ".":
            if i.count(j)!=1:
                print(False)
                exit()
            
for i in range(9):
    l[i]=[]
    for row in board:
        l[i].append(row.pop())    


for i in l:
    for j in i:
        if j != ".":
            if i.count(j)!=1:
                print(False)
                exit()

for i in [0,3,6]:
    for j in [0,3,6]:
        n=l[i][j:j+3]+l[i+1][j:j+3]+l[i+2][j:j+3]     
        for k in n:
            if k!='.':
                if n.count(k)!=1:
                    print(False)
                    exit()
print(True) 
