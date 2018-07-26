#Python as calculator
print('Add X to Y')
x=input('X=') #input arguments are string
X=float(x) #string is converted to float
y=input('Y=')
Y=float(y)
SUM = X+Y
print('SUM of X and Y =', SUM)

#Function calling

def addition():
        add = X+Y
        print('SUM from function=', add) #do not print but remember
addition() #calling the function

