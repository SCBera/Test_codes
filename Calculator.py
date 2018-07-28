#Python as calculator
print('***Welcome to Python calculator***')
#operator = input('Type S for sum, M for multiplication, D for division, \n')

def calculate(operator):
    if operator == '+':
        SUM = X+Y
        print(X,'+',Y,'=', SUM)
    elif operator == '*':
        multi = X*Y
        print(X,'*',Y,'=', multi)
    elif operator == '/':
        div = X/Y
        print(X,'/',Y,'=', div)
    elif operator == '-':
        sub = X-Y
        print(X,'-',Y,'=', sub)
    else:
        print('You have not choosen suitable operator e.g., +, -, *, /')




#start of the loop
while True:
#    x=input('') #input arguments are strings
#    #operator = input('Type + for sum, * for multiplication, / for division, \n')
#    operator = input()
#    y=input()
#    X, operator, Y = float(input('Please type first number:')), input('Please choose operator from +,-,*,/:'), float(input('Please type second number:')) #all inputs in a row
#    x, operator, y = input('Please type first number:'), input('Please choose operator from +,-,*,/:'), input('Please type second number:') #all inputs in a row
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
            
 
    y_loop=True
    while y_loop:
        y = input('Please type second number:')
        try:
            Y=float(y) #string is converted to float
            y_loop=False
        except:
            print('Input is not a number')
            y_loop=True

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
            
            
#    y = input('Please type second number:')
#    try:
#        Y=float(y) #string is converted to float
#    except:
#        print('Input is not a number')

#    def calculate(operator):
#        if operator == '+':
#            SUM = X+Y
#            print(X,'+',Y,'=', SUM)
#        elif operator == '*':
#            multi = X*Y
#            print(X,'*',Y,'=', multi)
#        elif operator == '/':
#            div = X/Y
#            print(X,'/',Y,'=', div)
#        elif operator == '-':
#            sub = X-Y
#            print(X,'-',Y,'=', sub)
#        else:
#            print('You have not choosen suitable operator e.g., +, -, *, /')
#            SUM = X+Y
#            multi = X*Y
#            div = X/Y
#            print('SUM of X and Y =', SUM)
#            print('Multiplication of X with Y =', multi)
#            print('Division of X by Y =', div)


#Function calling
    calculate(operator)
#repeat the calculation
    demand_input = input('Stop calculation? (y):')
    if  'y' == demand_input:
        print('The calculator exits')
        break

print('Thank you for using Python calculator') #end of the loop
