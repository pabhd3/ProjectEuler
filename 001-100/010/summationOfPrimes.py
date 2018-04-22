from math import sqrt, ceil

# Check if a number is prime
def isPrime(n):
    for i in range(2, ceil(sqrt(n))):
        if(int(n) % i == 0):
            return False
    return True
# Get the summation of primes
def summationOfPrimes(n):
    sum = 0
    for i in range(1, int(n)):
        if(isPrime(i)):
            sum += i
    return sum

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    # Print results
    print("Summation of primes below " + "{:,}".format(int(n)))
    print("{:,}".format(summationOfPrimes(n)))
