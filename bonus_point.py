

def validate_input(numbers):
    #isinstance(numbers, list) this checks whether the input numbers is of type list
    #all(isinstance(i, int) for i in numbers):this part checks if all elements in the numbers list are integers.
    if isinstance(numbers, list) and all(isinstance(i, int) for i in numbers):
        return True
    else:
        return False

# Example
input_list = [2, 1, 5, 4, 6, '9', 7, 8, 10]  # Invalid input Because it contains string instead of int.
if validate_input(input_list):
    print("Valid input!")
else:
    print("Invalid input!")