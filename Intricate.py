n=int(input())

#works best for input greater than 3 

print('#','='*n*n,'#',sep='')
for i in range(n):
    print('|',('<>'+'.'*n*i+'<>').center(n*n,' '),'|',sep='')
for i in range(n-1,-1,-1):
    print('|',('<>'+'.'*n*i+'<>').center(n*n,' '),'|',sep='')
print('#','='*n*n,'#',sep='')    
    
