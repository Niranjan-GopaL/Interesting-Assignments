# H_row , H_column = map(int , input().split())
# image_tensor = []
# for i in range(H_row):
#     image_tensor.append(list(map(int,input().split())))

# F_row , F_column = map(int , input().split())
# feature_detector_tensor = []
# for i in range(F_row):
#     feature_detector_tensor.append(list(map(int,input().split())))

H_row = 7
H_column = 5

image_tensor =[[1,0,1,0,1],[1,1,1,1,0],[0,0,1,1,1],[0,0,1,1,1],[1,0,1,0,1],[0,0,0,1,1],[1,1,1,1,1]]
feature_detector_tensor=[[1,1,1],[-3,-3,-3],[0,0,0]]


convolusion = []
m = H_row -2
n = H_column -2
sum = 0


for row_convolusion in range(m):
    for column_convolusion in range(n):
        for j in range(H_row):
            for k in range(H_column):
                sum += (image_tensor[j][k] * feature_detector_tensor[j-row_convolusion][k-column_convolusion])
        convolusion.append([])
        convolusion[row_convolusion].append(sum)
        sum = 0


for row in range(m):
    for column in range(n):
        print(convolusion[row][column],end=' ')
    print()
