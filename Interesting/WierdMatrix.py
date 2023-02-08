#IMT2022543

n = int(input())
num = 1
space =' '*(2*n-3)*3
add = 3*n-5

flag= True

#works for all numbers even as large  as 30 and the output is
#designed to look elegent while taking into account the
#discrepencies that would come from the different spacing of
#two and three digit numbers


if n not in [1,2]:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=1 and i!=n:
                print(f'{num+add:3d}',space,f'{num:3d}',sep='',end='')
                if i!=n-1:num+=1
                add-=2
                break
            if i==1:
                print(f'{num:3d}',end='   ')
                num+=1
            if i==n:
                if flag == True:
                    num=num+n
                    flag=False
                    print(f'{num:3d}',end='   ')
                    num-=1
                else:
                    print(f'{num:3d}',end='   ')
                    num-=1
        print(end='\n\n\n')
elif n==1:
    print(n)
elif n==2:
    print('1','2',end='\n\n',sep='   ')
    print('4','3',sep='   ')
