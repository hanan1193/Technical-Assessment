
def findMissingNumbers(n, arr):
    # Create hash array of size n+1 
    # is used to track how many times each number in the range [1, n] appears in arr.
    check_array = [0] * (n + 1)

    # Store frequencies of elements in arr
    for num in arr:
        check_array[num] += 1

    # List to store the missing numbers
    missing = []

    # Find the missing numbers by checking check_array
    for i in range(1, n + 1):
        if check_array[i] == 0:
            missing.append(i)

    return missing

# the main code
if __name__ == "__main__":
    arr = [2,1, 5, 4, 6, 9, 7, 8, 10]  
    n = 10  # The expected range of numbers

    result = findMissingNumbers(n, arr)

    # the result
    print("Missing numbers:", result)