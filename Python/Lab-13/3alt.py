#input list
numbers = input().split(",")
# convert each string in the list to an integer
numbers = list(map(int, numbers))

#list comprehension to get all possible subarrays of length 2 and sort them in descending order by their product
result = sorted([(numbers[i], numbers[i+1]) for i in range(len(numbers)-1)], key=lambda x: x[0]*x[1], reverse=True)

print(result)