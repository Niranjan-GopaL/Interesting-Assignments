#IMT2022543

def sumdigit(n):
    if n==0:
        return 0
    else:
        return n%10 + sumdigit(n//10)   # sum(1234) = 4 + sum(123)

n=int(input())
print(sumdigit(n))
    

    
