#Vijesh.V @freakoutgames
#program for finding out if a number is prime number or not
#prime number is a number divisible by 1 or by itself

def prime_number(num):
    if (num <= 1):
        return False   #for numbers that is less or equal to 1

    for x in range(2, num):
        if (num % x == 0):
            return False
    return True

#calling the function to check
number = input("Enter any number to check: ")
if(prime_number(int (number))):
    print("The number %d is prime" % int (number))
else:
    print("The number %d is not prime" % int (number))