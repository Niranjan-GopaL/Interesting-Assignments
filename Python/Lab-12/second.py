def common(lol):
    return [i for i in lol[0] if i in lol[1]]

l1 = list(map(int,input().spit(" ")))
l2 = list(map(int,input().spit(" ")))
ans = list(filter(common,[l1,l2]))
print(ans)
[print(i,end=' ') for i in ans]