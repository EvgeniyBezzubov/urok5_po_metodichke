def steprn(A,B,otvet=1, step=0):
    otvet = otvet*A
    step+=1
    if step ==B:
        print("ответ ", otvet)
    else:
        steprn(A, B, otvet, step)

a = int(input("введите число :"))
b = int(input("введите степень :"))
steprn(a, b)
