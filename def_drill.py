def convert_float(number):
    try:
        X = float(number)  # string is converted to float
        return X
        # print(X)
    except:
        print('Input is not a number')


x = input('>')

X1 = convert_float(x)
print(X1)
