def sum_p(li):
    for i in li:
        if i>0:
            sum+=i
    return sum

def sum_n(li):
    for i in li:
        if i<0:
            sum+=i
    return sum

some_sum = lambda given_list : print(f'{sum_p(given_list)} \n{sum_n(given_list)}')
l1 = list(map(int,input().spit(" ")))
some_sum(l1)