# # x = int(input("Input first number "))
# # y = int(input("Input second number "))
# # print( x+y)

# x=float(input("Input first number "))
# y=float(input("Input second number "))
# z=round(x+y)
# # print(z)
# #answer with comma
# print(f"{z:,}")

# z=x/y
# print(f"{z:.2f}")#format to 2 decimal places
# z=round(x/y,2 )
# print(z)


def main():
    x=int(input("Input the Number "))
    print("X squared is :" , square(x))


def square(n):
    # return n*n
    # return n**2
    return pow(n,2)




main()
