#input list with values separated by comma
numbers = input().split(",")
# convert each string in list to integer
numbers = list(map(int, numbers))

#list comprehension to get all unique pairs of numbers whose product is even
result = [(numbers[i], numbers[j]) for i in range(len(numbers)) for j in range(i+1, len(numbers)) if (numbers[i]*numbers[j])%2==0]
print(result)
