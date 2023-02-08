#IMT2022543

def isPalindrome(n):
  if n<0:
    return False
  elif n<10:
    return True
  else:
    big10 = 10**(len(str(n)) - 1)                        # in n is 3 digit number , big10 is 100 ; if a 4 digit number then 1000
    newN = n - ((n//big10)*big10)
    newN = newN //10                                     #if n is 12321 , newN is 232  ; if n is 232 , newN is 3 and so on
    return (n%10 == n//(big10)) and isPalindrome(newN)

n=int(input()) 
print(isPalindrome(n)) 
      
