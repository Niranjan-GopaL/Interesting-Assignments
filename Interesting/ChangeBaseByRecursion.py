def ChangeBase(n,r,s=""):
    Set="0123456789ABCDEF"
    s+=Set[n%r]
    if n==0:
        return s
    elif n==1:
        return s
    else:
         ChangeBase(n//r,r,s)
         return s
