while True:
    firstNumber = int(input("Enter your first number (or type 'exit' to quit): "))
    if firstNumber == 'exit':
        break
    function = str(input("Enter the operator (+, -, *, /): "))
    secondNumber = int(input("Enter your second number: "))

    if function == "+":
        output = firstNumber + secondNumber
    elif function == "-":
        output = firstNumber - secondNumber
    elif function == "*":
        output = firstNumber * secondNumber
    elif function == "/":
        if secondNumber != 0:
            output = firstNumber / secondNumber
        else:
            print("Error: Division by zero!")
            continue  
    else:
        print("Invalid operator!")
        continue  

    print("Answer is:", output)


