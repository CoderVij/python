#Vijesh.V @FreakoutGames
#Binary Serach

def BinarySearch(elementToSearch, startIndex, endIndex):
    if endIndex >= startIndex:
        midIndex = int((startIndex + endIndex) / 2)
        midElement = elementsList[midIndex]
        if midElement == elementToSearch:
            return midIndex
        elif elementToSearch > midElement:
            return BinarySearch(elementToSearch, midIndex+1, endIndex)
        elif elementToSearch < midElement:
            return BinarySearch(elementToSearch, 0, midIndex - 1)
    else:
        return -1


#first get the elements
numberofElements = int(input("Enter Total Number of Elements: "))
elementsList = []
for i in range(numberofElements):
    elementsList.append(int(input("Enter element %d: " % (i+1))))

elementsList.sort()
elementToSearch = int(input("Enter the element to search: "))

result = BinarySearch(elementToSearch, 0, len(elementsList)-1)

if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 


