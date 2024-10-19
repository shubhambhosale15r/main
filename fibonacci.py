# Function to print Fibonacci series up to n terms
def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input: Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))

# Output: Fibonacci series
print(f"Fibonacci series up to {n} terms: {fibonacci_series(n)}")
