#Python as calculator
print('***Welcome to Python calculator***')
#operator = input('Type S for sum, M for multiplication, D for division, \n')

#start of the loop
while True:
#    x=input('') #input arguments are strings
#        #operator = input('Type + for sum, * for multiplication, / for division, \n')
#    operator = input()
#    y=input()
#    X, operator, Y = float(input('Please type first number:')), input('Please choose operator from +,-,*,/:'), float(input('Please type second number:')) #all inputs in a row
    x, operator, y = input('Please type first number:'), input('Please choose operator from +,-,*,/:'), input('Please type second number:') #all inputs in a row

#    if type(x)==(class 'string'):
#        print('Input is not a number')

    X=float(x) #string is converted to float
    Y=float(y)

    def calculate(operator):
        if operator == '+':
            SUM = X+Y
            print('X+Y=', SUM)
        elif operator == '*':
            multi = X*Y
            print('X*Y=', multi)
        elif operator == '/':
            div = X/Y
            print('X/Y=', div)
        elif operator == '-':
            sub = X-Y
            print('X-Y=', sub)
        else:
            print('You have not choosen suitable operation e.g., +, -, *, /')
#            SUM = X+Y
#            multi = X*Y
#            div = X/Y
#            print('SUM of X and Y =', SUM)
#            print('Multiplication of X with Y =', multi)
#            print('Division of X by Y =', div)


#Function calling
    calculate(operator)
#repeat the calculation
    demand_input = input('Do more calculation? (y/n):')
    if demand_input == 'n':
        print('The calculator exits')
        break
print('Thank you for using Python calculator') #end of the loop
