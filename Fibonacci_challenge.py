def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


n = int(input(" Enter the number of digits inside Fibonacci: "))
sequence = fibonacci(n)
print("Fibonacci Sequence:", sequence)
print("Next number in sequence:", sequence[-1] + sequence[-2])
print(type(sequence))