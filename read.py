file_ = open('read.txt')
print("opening file..")
# file_data = file_.read()
# print(file_data)
n = 0
for line in file_:
    n += 1
    # print(f"line-{n}: {line}")

    line = line.split(',')

    print(f"line-{n}: {line[0]}, {float(line[1])}")

#     if n % 2 != 0:
#         dir_ = line
#     else:
#         t_point = int(line)
# print(f"Dir: {dir_}\ntime: {t_point}")