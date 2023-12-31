print("*" * 10, "Калькулятор", "*" * 10)
print("Нажмите q для выхода")
while True:
    s = input("Знак (+, -, *, /, **): ")
    if s == 'q':
        break
    if s in ('+', '-', '*', '/', '**'):
        x = float(input('x= '))
        y = float(input('y= '))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '**':
            print("%.2f" % (x ** y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print('Ошибка')
    else:
        print("Неверный ввод")