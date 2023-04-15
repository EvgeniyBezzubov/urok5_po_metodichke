def chet(a, chetnih = 0, ne_chetnih = 0):
    a = int(a)
    ostatok = a % 10
    if ostatok%2==0:
        chetnih+=1
    else:
        ne_chetnih+=1
    if len(str(a))!=1:
        a = a//10
        chet(a, chetnih, ne_chetnih)
    else:
        print("количество чётных цифр равно {0}, не чётных {1}".format(chetnih,ne_chetnih))
a = input("введите число произвольной длинны: ")
chet(a)
