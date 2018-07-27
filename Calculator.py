#Python as calculator
print('***Welcome to Python calculator***')
#operator = input('Type S for sum, M for multiplication, D for division, \n')

#start of the loop
while True:
    x=input('') #input arguments are strings
    X=float(x) #string is converted to float
#operator = input('Type + for sum, * for multiplication, / for division, \n')
    operator = input()
    y=input()
    Y=float(y)
        
    def calculate(operator):
        if operator == '+':
            SUM = X+Y
            print('SUM of X and Y =', SUM)
        elif operator == '*':
            multi = X*Y
            print('Multiplication of X with Y =', multi)
        elif operator == '/':
            div = X/Y
            print('Division of X by Y =', div)
        else:
            print('You have not choosen any operation')
#            SUM = X+Y
#            multi = X*Y
#            div = X/Y
#            print('SUM of X and Y =', SUM)
#            print('Multiplication of X with Y =', multi)
#            print('Division of X by Y =', div)


#Function calling
    calculate(operator)
#repeat the calculation
    demand_input = input('Do more calculatioin (Y/N?)')
    if demand_input == 'N':
        print('The calculator exits')
        break
print('Thank you for using Python calculator') #end of the loop