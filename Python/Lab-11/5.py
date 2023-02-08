n = int(input())
d = {}

# accepting inputs from line and storing them in dictionary
for i in range(n):
    key, value = input().split(":")
    value = int(value)
    d[key] = value


k = int(input())

'''sorts d in a descending order based on the values, and returns a LIST of TUPLES, where each tuple is a key-value pair from the dictionary.'''
sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)

# since 2nd maximum number will be at index 1 of the list , k-1 is required
print(sorted_dict[k-1][0])