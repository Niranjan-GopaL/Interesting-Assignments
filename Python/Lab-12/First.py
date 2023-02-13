def is_neg(n):
    return [i for i in n if i < 0]

l1 = list(map(int,input().spit(" ")))
ans = list(filter(is_neg,l1))
print(ans)