import math
#Task #1

def DoubleEven(int1):
    try:
        if int(int1) % 2 == 0:
            even = int(int1) * 2
            return even
        else:
            not_even = -1
            return not_even
    except ValueError:
            return "that's no integer"

print(DoubleEven(input('Is it even or odd')))

#task #2

def Grade_Percent(grade):
    try:
        if int(grade) in range(0, 50):
            print('F')
        elif int(grade) in range(50,60):
            print('D')
        elif int(grade) in range(60,70):
            print('C')
        elif int(grade) in range(70,80):
            print('B')
        elif int(grade) in range(80,90):
            print('A')
        elif int(grade) in range(90,100):
            print('A+')
    except ValueError:
        print("That's not a grade.")

Grade_Percent(input('Input:'))