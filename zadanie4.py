def sum (n, sum_el=0):
    if n >=1:
        vvedennoe = int(input("введите следующее число для суммирования :"))
        sum_el += vvedennoe
        n = n -1
        sum(n, sum_el)
    else:
        print(sum_el)
n = int(input("введите количество числе в для суммирования:"))
sum(n)
