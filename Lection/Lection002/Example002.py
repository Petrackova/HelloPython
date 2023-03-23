#КОРТЕЖИ (tuple)


#t = ()
#print(type(t))
#t = (1,)
#print(type(t))

#v = [1,2,3]
#print(v)
#print(type(v))

#v = tuple(v)
#print(v)
#print(type(v))

#a = 1
#b = 2
#a, b = 1, 2
#a = b = 1


#a,b,c = v
#print(a,b,c)


"""t = (1,2,4,6,8,)
print(t[1])
for i in t:
    print(i)"""

t = (1,2,4,6,8,)
for i in range(len(t)):
    print(t[i])

# t[0] = 2 # ОШИбка преобразования элемента

