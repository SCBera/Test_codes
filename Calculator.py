#Python as calculator
print('*** Welcome to Python calculator ***')

def calculate(operator):
    if operator == '+':
        SUM = X+Y
        print(X,'+',Y,'=', SUM)
    elif operator == '*':
        print(X,'*',Y,'=', X*Y)
    elif operator == '/':
        if Y==0.0:
            print('Invalid input, Denominator =', Y)
        else:
            print(X,'/',Y,'=', X/Y)
    elif operator == '-':
        sub = X-Y
        print(X,'-',Y,'=', sub)

#Start of the loop
while True:
    x_loop=True
    # x input loop starts
    while x_loop:
        x = input('Please type first number:')
        try:
            X=float(x) #string is converted to float
            x_loop=False #loop ends
        except:
            print('Input is not a number')
            x_loop=True #loop continues
    # y input loop starts
    y_loop=True
    while y_loop:
        y = input('Please type second number:')
        try:
            Y=float(y) #string is converted to float
            y_loop=False
        except:
            print('Input is not a number')
            y_loop=True
    # operator input loop starts
    op_loop=True
    while op_loop:
        operator = input('Please choose operator from +,-,*,/:')
        if '-' == operator or '+' == operator or '*' == operator or '/' == operator: #True for valid input
            #print(op_loop)
            op_loop=False
        else:
            #print(op_loop)
            print('Input is not an suitable operator')
            op_loop=True

    #Function calling
    calculate(operator)
    #repeat the calculation
    demand_input = input('Stop calculation? (y):')
    if  'y' == demand_input or 'Y' == demand_input:
        print('The calculator exits')
        break
print('Thank you for using Python calculator') #End of the loop
