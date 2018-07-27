#Python as calculator
print('***Welcome to Python calculator***')
#do = input('Type S for sum, M for multiplication, D for division, \n')
x=input('') #input arguments are string
X=float(x) #string is converted to float
#do = input('Type + for sum, * for multiplication, / for division, \n')
do = input('')
y=input('')
Y=float(y)

#Condition checking
def calculate(do):
    if do == '+':
        SUM = X+Y
        print('SUM of X and Y =', SUM)
    elif do == '*':
        multi = X*Y
        print('Multiplication of X with Y =', multi)
    elif do == '/':
        div = X/Y
        print('Division of X by Y =', div)
    else:
        SUM = X+Y
        multi = X*Y
        div = X/Y
        print('SUM of X and Y =', SUM)
        print('Multiplication of X with Y =', multi)
        print('Division of X by Y =', div)


#Function calling
calculate(do)
