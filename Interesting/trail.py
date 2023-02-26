
n=0b00000010100101000001111010011100
n=str(n)
s=n[0]
for i in n[1:]:
    if i==1:
        s+='0'
    else:
        s+='1'
print(s)
