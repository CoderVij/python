#author: Vijesh.V  @FreakoutGames
#program to remove vowels from a string

def removeVowels(string):
    vowels = "aeiou"
    newstring = list(string)
    for i in vowels:
        length = len(newstring)
        for j in range(0, length):
            if newstring[j] == i.upper() or newstring[j] == i.lower():
                newstring[j]=""
    string = ''.join(newstring)
    return string

print(removeVowels("This program is for losers LOL!"))