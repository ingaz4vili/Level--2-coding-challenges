def square(number,str):
    for i in range(number):
        for j in range(number):
            print(str, end="")
        print("\r")
number = 2
str= '*'
square(number,str)