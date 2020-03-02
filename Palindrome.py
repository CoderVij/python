#Vijesh.V
#checking if a given string is palindrome
#a string or number is palindrome that reads the same forward and backward

# function which return reverse of a string 
def palindrome(string):
    j = 1
    for x in string:
        if x == string[-j]:
            j = j +1
            continue
        else:
            return False
    return True

#calling the function to check
str = input("Enter any string: ")
str_without_whitespace = (str.replace(" ", "")).lower()  #removing the white spaces and converting it into lowercase
if(palindrome(str_without_whitespace)):
    print("The string- %s -is palindrome" %str)
else:
    print("The string %s is not palindrome" %str)