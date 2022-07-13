import sys

if len(sys.argv) != 4:
    raise Exception("Длинна аргументов меньше или больше четырех")

if not type(sys.argv[1]) and type(sys.argv[3]) is int:
    raise TypeError("Только действительное число")

s=sys.argv[2]
if s in ('+','-','*','/'):
    x= int(sys.argv[1])
    y= int(sys.argv[3])
    if s=='+':
        print(x+y)
    elif s=='-':
        print(x-y)
    elif s=='*':
        print(x*y)
    elif s=='/':
        if y!=0:
            print(x/y)
        else:
            print("Деление на 0")


else:
    raise Exception("Должен быть только арефметический знак!!")
