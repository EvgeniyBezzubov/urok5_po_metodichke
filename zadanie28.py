def prugressia():
    lst = []
    a1 = int(input("введи первый элемент арифметическйо прогрессии :"))
    n = int(input("Введи количество элементов: "))
    d = int(input("Введи шаг прогрессии : "))
    for i in range(1,n+1):
        an = a1 + (i-1)*d
        lst.append(an)
    print(lst)

prugressia()
