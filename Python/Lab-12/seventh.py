import functools
from functools import reduce

l = list(map(int,input().split(" ")))
temp=l.copy()
product_ = reduce(lambda x, y: x * y, l)
sum_ = reduce(lambda x, y: x + y, temp)

print(sum_)
print(product_)
