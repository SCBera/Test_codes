def convert_float(number):
    try:
        X = float(number)  # string is converted to float
        return X
        # print(X)
    except:
        print('Input is not a number')


def find_operator(user_input):
    if user_input.find('+') > 0:
        operator = '+'
        pos = user_input.find('+')
        return operator, pos
    else:
        print("Operator not found!")


user_input = input("Type>")

# X1 = convert_float(x)
print(find_operator(user_input))
