# Сумма чисел 
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
n = int(input()) # 5
print(sumNumbers(n)) # 15


# неограниченное количество аргументов
def summ_str(*args):
    res = ''
    for i in args:
        res+=i
    return res

print(summ_str('q','e','l'))
print(summ_str('q','e','l','adsf','asdf'))