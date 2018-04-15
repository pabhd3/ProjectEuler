def multiplesOf3or5(n):
    sum = 0
    for i in range(0, int(n)):
        if(i % 3 == 0 or i % 5 ==0):
            sum += i
    return sum

if __name__ == "__main__":
    n = input("Enter an integer n: ")
    print("\nSum of multiples of 3 or 5 below {:,}".format(int(n)))
    print("{:,}".format(multiplesOf3or5(n)))
