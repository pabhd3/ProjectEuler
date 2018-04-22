from random import randint

# Generate a Random 1,000 digit number
def generateNumber(length):
    gen = ""
    for i in range(0, int(length)):
        gen += str(randint(0, 10))
    return gen
# Generate an array of adjacent digits in a string
def getMultiples(series, n, start):
    multiples = []
    for i in range(int(start), int(start) + int(n)):
        multiples.append(series[i])
    return multiples
# Get the product of an array of digits
def getProduct(multiples):
    product = 1
    for multiple in multiples:
        product *= int(multiple)
    return product
# Calculate the largest product in a series
def largestProductInASeries(choice, n, length):
    default = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
    if(choice == 'y'):
        series = default
    else:
        series = generateNumber(length)
    largest = 0
    for i in range(0, int(length) + 1 - int(n)):
        multiples = getMultiples(series, n, i)
        product = getProduct(multiples)
        if(product > largest):
            largest = product
            largestMultiples = multiples
    print("Series\n" + series + "\n")
    return largest, largestMultiples
# Print the result in a specific format
def printResults(largest, multiples):
    result = "{:,}".format(largest) + " = "
    for multiple in multiples:
        result += str(multiple) + " * "
    result = result[:-3]
    print(result + "\n")

if __name__ == "__main__":
    # Get user input
    choice = input("Would you like to use the default number? (y/n): ")
    length = 1000
    if(choice == "n"):
        length = input("How many digits do you want to be in the series? ")
    n = input("Enter the number of adjacent digits, n: ")
    largest, multiples = largestProductInASeries(choice, n, length)
    # Print results
    print("The largest product in the above series of " + n + " adjacent digits")
    printResults(largest, multiples)
