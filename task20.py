#Calculator project
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" :add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
continue_ = True
while continue_:
    num1 = float(input("what is the first number??\n"))
    num2 = float(input("what is the second number?\n"))
    for symbol in operation:
        print (symbol) 
    operation_symbol = input("Pick an operation from the line above")
    calculation = operation[operation_symbol]
    answer = calculation(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    while True:
        question = input("Do you want to continue the calculation carrying the result? Types 'y' for 'yes and 'n'for 'no'")
        if question == "n":
            break
        num = float(input("What is another number?\n"))
        a = answer
        for symbol in operation:
            print (symbol)
        operation_symbol = input("Pick an operation from the line above")
        answer = calculation(answer,num)
        print(f"{a} {operation_symbol} {num} = {answer}")
    if input("Enter 'y' to operate another calcualtion and 'n' to end ") == "n":
        continue_ = False
        



