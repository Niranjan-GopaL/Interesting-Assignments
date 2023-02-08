List = list(map(eval,input().split()))
Tuple = (List[0], List[-1], len(List))
print(Tuple)