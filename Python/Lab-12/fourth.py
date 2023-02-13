def check(l):
    for index,element in enumerate(l):
        if element.len() < 4 :
            l.pop(index)
    return l

line = input().spit(" ")
ans = filter(check,line)
[print(i,end=' ') for i in ans]