# Python as calculator
# from sys import argv
# num1, num2, num3 = argv

print('*** Welcome to Python calculator ***')
print("PRESS 'CRTL+C' to exit")
# perform the operation


def calculate(operator):
    if operator == '+':
        SUM = X+Y
        print(X, '+', Y, '=', SUM)
    elif operator == '*':
        print(X, '*', Y, '=', X*Y)
    elif operator == '**':
        print(X, 'power', Y, '=', X**Y)
    elif operator == '/':
        if Y == 0.0:
            print('Invalid input, Denominator =', Y)
        else:
            print(X, '/', Y, '=', X/Y)
    elif operator == '-':
        sub = X-Y
        print(X, '-', Y, '=', sub)

# converts the numbers to float, can also say if the input is not a number!


def convert_float(number):
    try:
        num = float(number)  # string is converted to float
        return num
    except:
        return 'Input is not a number'


while True:
    user_input = input("Please type>")

    while True:
        operator = None

        # find the operand and position of the operand
        if '+' in user_input:
            operator = '+'
            pos = user_input.find('+')
        elif '-' in user_input:
            operator = '-'
            pos = user_input.find('-')
        elif '**' in user_input:
            operator = '**'
            pos = user_input.find('**')
        elif '/' in user_input:
            operator = '/'
            pos = user_input.find('/')
        elif '*' in user_input:
            operator = '*'
            pos = user_input.find('*')
        else:
            pass
            #print("Suitable operator not found!")

        # gets the numbers from both sides of the operand
        if operator != None:
            num1 = user_input[:pos]
            X = convert_float(num1)
            num2 = user_input[pos+1:]
            Y = convert_float(num2)
        else:
            print("Suitable operator not found!")
        #numbers = [num1, num2]
        #print("end of the 2nd loop")
        print(X, Y)
        break

    # calling the def for calculation
    # for num in numbers:
    if X == 'Input is not a number' and Y == 'Input is not a number':
        print('Inputs are not a number')
    elif X == 'Input is not a number' or Y == 'Input is not a number':
        print('Input is not a number')
    else:
        calculate(operator)

    #print("PRESS 'CRTL+C' to exit")


print('Thank you for using Python calculator')  # End of the loop
