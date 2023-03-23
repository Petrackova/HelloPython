text = 'СъЕШЬ ещё этих МяГкИх французских булок'
 
print(len(text)) # 39
print('ещё' in text) # True
print(text.upper()) # #СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.replace('ещё','ЕЩЁ')) #СъЕШЬ ЕЩЁ этих МяГкИх французских булок

print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # cъ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...