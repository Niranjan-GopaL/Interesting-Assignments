def isLeapYear(year):
    
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False

def isMonthValid(month):
    
    if month in range(1,13):
        return True
    else:
        return False


def isDateValid(date,month,year):
    
    if month in [1,3,5,7,8,10,12]:
        if date in range(1,32):
            return True
        else:
            return False
        
    if month in [4,6,9,11]:
        if date in range(1,31):
            return True
        else:
            return False
        
    if month == 2:
        if isLeapYear(year):
            if date in range(1,30):
                return True
            else:
                return False
        else:
            if date in range(1,29):
                return True
            else:
                return False
            
        

date=int(input())
month=int(input())
year=int(input())
if isMonthValid(month) and isDateValid(date,month,year) :
    print("Valid")
else:
    print("Not Valid")
    
