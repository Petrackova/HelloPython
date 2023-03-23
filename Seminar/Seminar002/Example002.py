'''Дано натуральное число A > 1. Определите, каким посчету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 '''
num = int(input('Введите целое число: '))
number1 = 0
number2 = 1
a = 2
while True:
    s = number1+number2
    number1 = number2
    number2 = s
    a+=1
    if s==num:
        print(a)
        break
    elif s > num:
        print(-1)
        break

#number = int(input('Введите целое число: '))
#fibo_1, fibo_2 = 0,1
#index =1 
#while fibo_2 < number:
#    fibo_1,fibo_2 = fibo_2, fibo_1 + fibo_2
#    index +=1
#if fibo_2 == number:
#    print(index)
#else:
#    print(-1)