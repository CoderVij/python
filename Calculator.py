#author: Vijesh.V  @FreakoutGames
#building a calculator using Tkinter

import tkinter as tk

#intialize
root = tk.Tk()
root.title("Simple Calculator")


#input field
enteredNumbers = tk.Entry(root, width = 35, borderwidth= 2)
enteredNumbers.grid(row = 0, column= 0, columnspan= 3, ipadx = 19, ipady= 3)

enter = tk.Entry(root, width = 35, borderwidth= 10)
enter.grid(row = 1, column= 0, columnspan= 3, ipadx = 10, ipady= 10)

current = ""
def button_click(number):
    global current
    current = current + str(number)
    enter.delete(0, tk.END)
    enter.insert(0, current)

def clearGlobalVariables():
    global current
    global operandCount
    global result
    global equation
    current = ""
    operandCount = 0
    result = 0
    operandList.clear()
    operatorsList.clear()
    equation.clear()
    print(equation)

def cleardisplayNumbers():
    enteredNumbers.delete(0, tk.END)
    


def button_clear():
    enter.delete(0,tk.END)
    enteredNumbers.delete(0, tk.END)
    clearGlobalVariables()
    

def button_add():
    operatorHandler("+")


def operatorHandler(operator):
    global current
    global operatorsList
    global equation
    if current == "" and len(operatorsList) > 0 and operatorsList[len(operatorsList)-1] == operator:
        return

    if current == "":
        operatorsList[len(operatorsList)-1] = operator
        equation[len(equation)-1] = operator
        displayNumbers()
        return
    else:
        stackEquation(current, operator)


operatorsList = []
operandList = []
def stackEquation(element, operator):
    global operandList
    global operatorsList

    global current
    global equation
    current = ""
    operatorsList.append(operator)
    operandList.append(element)

    equation.append(operandList[len(operandList)-1])
    equation.append(operatorsList[len(operatorsList)-1])
    displayNumbers()
    doCalculation(operandList, operatorsList)

result = 0
operandCount = 0
def doCalculation(operands, operators):
    #global operandAndoperator
    global result
    global operandCount
    sum = 0

    print(result)
    if len(operands) < 2:
        return
    else:
        if operandCount == 0:
            result = int(operands[0])
            
        if operators[operandCount] == "+":
            sum = int(result) + int(operands[operandCount+1])
            result = sum
                #print(result)
            operandCount = operandCount + 1

            enter.delete(0, tk.END)
            enter.insert(0, result)
        elif operators[operandCount] == "-":
            sum = int(result) - int(operands[operandCount+1])
            result = sum
                #print(result)
            operandCount = operandCount + 1

            enter.delete(0, tk.END)
            enter.insert(0, result)
        elif operators[operandCount] == "/":
            sum = int(result) / int(operands[operandCount+1])
            result = sum
                #print(result)
            operandCount = operandCount + 1

            enter.delete(0, tk.END)
            enter.insert(0, result)
        elif operators[operandCount] == "*":
            sum = int(result) * int(operands[operandCount+1])
            result = sum
                #print(result)
            operandCount = operandCount + 1

            enter.delete(0, tk.END)
            enter.insert(0, result)
    
    print(operands)

def button_equalfunc():
    global result
    second_number = enter.get()
    enter.delete(0, tk.END)
    stackEquation(second_number, operatorsList[len(operatorsList)-1])
    
    #clearGlobalVariables()
    cleardisplayNumbers()
    return

equation = []
def displayNumbers():
    global equation
    enteredNumbers.delete(0, tk.END)
    enteredNumbers.insert(0,equation)

def button_subtract():
    operatorHandler("-")

def button_division():
    operatorHandler("/")

def button_multiply():
    operatorHandler("*")


button_1 = tk.Button(root, text="1", padx= 40, pady=20, command= lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx= 40, pady=20, command= lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx= 40, pady=20, command= lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx= 40, pady=20, command= lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx= 40, pady=20, command= lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx= 40, pady=20, command= lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx= 40, pady=20, command= lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx= 40, pady=20, command= lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx= 40, pady=20, command= lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx= 40, pady=20, command= lambda: button_click(0))
button_add= tk.Button(root, text="+", padx= 39, pady=20, command= button_add)
button_sub= tk.Button(root, text="-", padx= 39, pady=20, command= button_subtract)
button_div= tk.Button(root, text="/", padx= 39, pady=20, command= button_division)
button_mul= tk.Button(root, text="*", padx= 39, pady=20, command= button_multiply)
button_clear= tk.Button(root, text="clear", padx= 78, pady=20, command= button_clear)
button_equal= tk.Button(root, text="=", padx= 86, pady=20, command= button_equalfunc)

#button_substract= tk.Button(root, text="-", padx= 39, pady=20, command= button_add)

button_1.grid(row= 4, column=0)
button_2.grid(row= 4, column=1)
button_3.grid(row= 4, column=2)

button_4.grid(row= 3, column=0)
button_5.grid(row= 3, column=1)
button_6.grid(row= 3, column=2)

button_7.grid(row= 2, column=0)
button_8.grid(row= 2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row= 5, column= 0)
button_add.grid(row=6, column=0)
button_sub.grid(row=7, column=0)
button_div.grid(row=7, column=1)
button_mul.grid(row=7, column=2)
button_clear.grid(row=5, column=1, columnspan =3)
button_equal.grid(row=6, column=1, columnspan =3)


root.mainloop()