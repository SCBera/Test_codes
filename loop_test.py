loop = True
while loop:
    x = input('Please type first number:')
    try:
        X=float(x) #string is converted to float
        print('before', loop)
        loop = False
        print('after', loop)
    except:
        print('Input is not a number')
        loop = True

print('loop ends', X)
        
