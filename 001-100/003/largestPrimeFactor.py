from math import sqrt, ceil

def isPrime(n):
    for i in range(2, ceil(sqrt(int(n)))):
        if(int(n) % i == 0):
            return False
    return True

def largestPrime(n):
    largestPrime = 1
    for i in range(1, int(n)):
        if(isPrime(i) and i > largestPrime):
            largestPrime = i
    return largestPrime

if __name__ == "__main__":
    n = input("Enter an integer n: ")
    print("\nLargest Prime below {:,}".format(int(n)))
    print("{:,}".format(largestPrime(n)))