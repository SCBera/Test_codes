# Python as calculator
print('*** Welcome to Python calculator ***')
print("PRESS 'CRTL+C' to exit")
# converts the numbers to float, can also say if the input is not a number!


def convert_float(number):
    try:
        num = float(number)  # string is converted to float
        return num
    except:
        return 'Input is not a number'


# perform the operation


def calculate(operator):
    if operator == '+':
        SUM = X+Y
        # print(X, '+', Y, '=', SUM)
        return SUM
    elif operator == '*':
        #print(X, '*', Y, '=', X*Y)
        return X*Y
    elif operator == "**":
        #print(X, 'power', Y, '=', X**Y)
        return X**Y
    elif operator == '/':
        if Y == 0.0:
            print('Invalid input, Denominator =', Y)
        else:
            #print(X, '/', Y, '=', X/Y)
            return X/Y
    elif operator == '-':
        sub = X-Y
        #print(X, '-', Y, '=', sub)
        return sub
    # Ans = SUM or X*Y or X**Y or X/Y or sub


while True:
    user_input = input(">")

    while True:
        operator = None
        X = None
        Y = None

        # find the operand and position of the operand
        if '+' in user_input:
            operator = '+'
            pos = user_input.find('+')
        elif '-' in user_input:
            operator = '-'
            pos = user_input.find('-')
        elif "**" in user_input:
            operator = "**"
            pos = user_input.find("**")
        elif '/' in user_input:
            operator = '/'
            pos = user_input.find('/')
        elif '*' in user_input:
            operator = '*'
            pos = user_input.find('*')
        else:
            print(operator)
            operator = "BAD"
            # ends the loop if operator not found
            break

        # gets the numbers from both sides of the operand

        if operator == "**" and convert_float(user_input[:pos]) == 'Input is not a number':
            global Ans
            X = Ans
            num2 = user_input[pos+2:]
            Y = convert_float(num2)
        elif operator == "**":
            num1 = user_input[:pos]
            X = convert_float(num1)
            num2 = user_input[pos+2:]
            Y = convert_float(num2)
        elif operator != None and convert_float(user_input[:pos]) == 'Input is not a number':
            X = Ans
            num2 = user_input[pos+1:]
            Y = convert_float(num2)
            # print('here')
        elif operator != None:
            num1 = user_input[:pos]
            X = convert_float(num1)
            num2 = user_input[pos+1:]
            Y = convert_float(num2)
        else:
            pass
        #print(X, Y, operator)
        break

    # calling the def for calculation
    # for num in numbers:
    if operator == 'BAD':
        print('Suitable operator not found!')
    elif X == 'Input is not a number' and Y == 'Input is not a number':
        print('Inputs are not a number')
    elif X == 'Input is not a number' or Y == 'Input is not a number':
        print('Input is not a number')
    else:
        Ans = calculate(operator)
        # global Ans
        print(Ans)

    # print("PRESS 'CRTL+C' to exit")


print('Thank you for using Python calculator')  # End of the loop
