l = [1 ,2 ,-3 ,4 , -5]

'''In the two print statements the lambda f() is same,
the only difference is that one is a map() another in filter().
This perrfectly illustrates the difference between the two'''


#This prints [True, True, False, True, False]
print(list(map(lambda x: x > 0 , l)))

#This prints [1, 2, 4]
print(list(filter(lambda x: x > 0, l)))






