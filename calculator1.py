def calc():
    znak  = input("Введи знак выражения * - / +, либо 0 для выхода:")
    if znak == "*" or znak == "/" or znak == "+" or znak == "-":
        a = int(input("Введите первое число"))
        b = int(input("Введите второе число"))
        if znak == "*":
            otvet = a*b
            print("Ваш результат ", otvet)
        if znak == "/":
            if b ==0:
                b = int(input("Введите второе число заново, делить на ноль нельзя"))
            otvet = a/b
            print("Ваш результат ", otvet)
        if znak == "+":
            otvet = a+b
            print("Ваш результат ", otvet)
        if znak == "-":
            otvet = a-b
            print("Ваш результат ", otvet)
        calc()
    elif znak == "0":
        print("выход")
        exit(0)
    else:
        print("Введите корректно")
        calc()
calc()

