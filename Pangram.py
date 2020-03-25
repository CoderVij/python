#author: Vijesh.V @FreakoutGames
#Program to check if a sentence is pangram or not

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def is_pangram(sentence):
    index = 0
    for char in alpha:
        x = char in sentence.lower()
        if x == True:
            index = index + 1

    if index == 26:
        return True
    else:
        return False

print(is_pangram("the quick brown fox jumps over the "))