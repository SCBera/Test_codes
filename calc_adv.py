# Python as calculator
print('*** Welcome to Python calculator ***')


def calculate(operator):
    if operator == '+':
        SUM = X+Y
        print(X, '+', Y, '=', SUM)
    elif operator == '*':
        print(X, '*', Y, '=', X*Y)
    elif operator == '/':
        if Y == 0.0:
            print('Invalid input, Denominator =', Y)
        else:
            print(X, '/', Y, '=', X/Y)
    elif operator == '-':
        sub = X-Y
        print(X, '-', Y, '=', sub)


def convert_float(number):
    try:
        num = float(number)  # string is converted to float
        return num
    except:
        print('Input is not a number')



# Start of the loop
while True:
    x_loop = True
    # x input loop starts
    while x_loop:
        x = input('Please type>')
        if x.find('+') > 0:
            operator = '+'
            pos = x.find('+')
            num1 = x[:pos]
            X = convert_float(num1)
            num2 = x[pos+1:]
            Y = convert_float(num2)
            x_loop = False
        else:
            print("type a ...")

            x_loop = True  # loop continues

    # Function calling

    # repeat the calculation
calculate(operator)


user_input = input('Stop calculation? (y):')
if 'y' == user_input or 'Y' == user_input:
    print('The calculator exits')
    break

print('Thank you for using Python calculator')  # End of the loop
