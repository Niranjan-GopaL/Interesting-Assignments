n=int(input())
d={}
for i in range(n):
    [k,v] = input().split(":")
    d[k]=v


num_k = int(input())


while num_k <= len(d) and num_k>1:
    key = [k for k, v in d.items() if v==max(d.values) ][0]
    d.pop(key)
    k-=1

print(max(d.values))
