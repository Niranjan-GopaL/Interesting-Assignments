'''
Techniques used:
- usage of any() and  all() functions
- Catching many Value errors at the same time
'''


while True:
    try:
        num_list = input()
        # If the input is "" that is False 
        if not num_list:
            raise ValueError("List is empty")

        # Even if the a int("SomeString") , it'll raise a ValueError
        num_list = [int(num) for num in num_list.split(' ')]
        # perfect place to use any(iterable)
        if any(num < 0 for num in num_list):
            raise ValueError("List contains negative numbers")
        
        avg = sum(num_list) / len(num_list)
        print("The average of the numbers is:", avg)
        break

    except ValueError as value_error:
        print("Invalid input:", value_error)
    except Exception as e:
        print("An error occurred:", e)
