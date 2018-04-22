# Calculate the sum of the squares
def squareSum(n):
    sum = 0
    for i in range(1, int(n) + 1):
        sum += pow(i, 2)
    return sum

# Calculate the square of the sum
def sumSquares(n):
    sum = 0
    for i in range(1, int(n) + 1):
        sum += i
    return pow(sum, 2)

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    diff = sumSquares(n) - squareSum(n)
    # Print results
    print("Difference between the sum of squares of the first " + "{:,}".format(int(n)) + " natural numbers and the square of the sum")
    print("{:,}".format(diff))
