n = 1.345
print(int(n)) 
# Отбрасывается дробная часть вне зависимости больше 0.5 или меньше
m = '345'
print(m * 2)
 # При умножении строки на число, она повторяется столько раз на какое была умножена
print(int(m) * 2)

n = 1.345
print(str(n) * 2)

n = '1.345'
print(float(n) * 2)
m = 2
print(float(m))

a = 1.43425
b = 2.2983
c = round(a * b, 5) # 3,29633

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)


n = int(input())
if n % 2 == 0 and n % 3 == 0:
    print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
    print('Число кратно 15')


n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa) # 9


i = 0
while i < 5:
    if i == 3:
        break
        i = i + 1
    else:
        print('Пожалуй')
print('хватит )')
print(i)



n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
else:
    print('Пожалуй')
print('хватит )')
print(summa)
# Пожалуй
# хватит )
# 9



n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
flag = False
i += 1

for i in 1, -2, 3, 14, 5:
    print(i)

r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)


for i in range(5):
    print(i)
# 0 1 2 3 4



text = 'СъЕШЬ ещё этих МяГкИх французских булок'
#Определить количество символов в строке:
print(len(text)) # 39
#Проверить наличие символа в строке (in):
print('ещё' in text) # True
#Функция, которая делает все буквы строки маленькими:
print(text.lower()) # съешь ещё этих мягких французских булок
#Функция, которая делает все буквы строки большими:
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
#Заменить слово на другое :
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...