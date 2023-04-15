def prugressia(n,otvet = 0,  sum=0, curr_pos=0):


    sum +=1
    otvet = otvet + sum
    if sum ==n:
        print("ответ равен", otvet)

        otvet_teor = (n*(n+1))//2
        print("Теоретический ответ равен : ", otvet_teor)
        if otvet_teor== otvet:
            print("Совпало")

    else:
        prugressia(n, otvet, sum, curr_pos)

a = int(input("введи число для подсчёта арифметической прогрессии :"))
prugressia(a)
