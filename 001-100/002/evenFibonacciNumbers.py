# Generate the Fibonacci list, stopping at given value
def maxFibonacciValue(n):
    fib = [1, 2]
    for i in range(2, int(n)):
        if(fib[i-1] + fib[i-2] > int(n)):
            break
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib

# Calculate even-valued sum
def evenFibonacciNumbers(n):
    sum = 0
    for value in maxFibonacciValue(n):
        if(value % 2 == 0):
            sum += value
    return sum

if __name__ == "__main__":
    n = input("Enter a max fibonacci value n: ")
    print("Sum of even-valued fibonacci terms below {:,}".format(int(n)))
    print("{:,}".format(evenFibonacciNumbers(n)))