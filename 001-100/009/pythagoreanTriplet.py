from math import sqrt

# Determine if a triplet is a pythagorean triplet
def isPythagoreanTriplet(a, b):
    c = sqrt(pow(a, 2) + pow(b, 2))
    test1 = False; test2 = False
    if(a < b and b < c):
        test1 = True
    if(pow(int(c), 2) == pow(a, 2) + pow(b, 2)):
        test2 = True
    return test1 and test2
# Print the triplet in a specific format
def printTriplet(a, b):
    c = sqrt(pow(a, 2) + pow(b, 2))
    product = a * b * c
    print("a = ", a, "   b = ", b, "   c = ", int(c), "   abc = ", "{:,}".format(int(product)))
# Find all the pythagorean triplets below n
def pythagoreanTriplets(n):
    i = 0; j = 0; iWorks = True
    while(iWorks):
        jWorks = True; j = 0
        while(jWorks):
            if(pow(i, 2) > int(n)):
                iWorks = False
            if(pow(i, 2) + pow(j, 2) < int(n)):
                if(isPythagoreanTriplet(i, j)):
                    printTriplet(i, j)
            else:
                jWorks = False
            j += 1
        i += 1

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    # Print results
    pythagoreanTriplets(n)
