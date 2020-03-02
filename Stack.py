#Vijesh.V @freakoutgames
#stack datastructure - FILO

class stack:
    data = []
    def push(self,num):
        self.data.append(num)

    def popp(self):
        return self.data.pop(len(self.data)-1)

    def isempty(self):
        return (len(self.data) == 0)

    def size(self):
        return (len(self.data))

    def top(self):
        if(len(self.data) > 0):
            return (self.data[len(self.data)-1])
        else:
            return 0



#calling the function to check
stackObj = stack()
#stackObj.push(1)
#stackObj.push(2)
#stackObj.push(3)
#stackObj.push(9)
#print(stackObj.popp())
#print(stackObj.popp())
print(stackObj.isempty())
print(stackObj.top())
print(stackObj.size())

#basically the stack is easily represented by list data structure