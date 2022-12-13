def fact(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*fact(n-1)


def BinoExpn(n):
    row=''
    for i in range(n+1):
         row = row + str(int(fact(n)/(fact(i)*fact(n-i))))+' '
    return row

n=int(input())

for i in range(n):
    print(BinoExpn(i).center(70,' '))
