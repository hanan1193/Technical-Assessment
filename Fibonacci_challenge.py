#This function that takes one argument n.
#n is the number of Fibonacci numbers you want to generate.
#This function returns a list.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


n = int(input(" Enter the number of digits inside Fibonacci: "))
sequence = fibonacci(n)
print("Fibonacci Sequence:", sequence)
print("Next number in sequence:", sequence[-1] + sequence[-2])#Adding the last two numbers in the list to genarate the 
#next number in the sequence.