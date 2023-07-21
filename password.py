import random
prl = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
"""
a: 1 спец символ
b: 2 буквы(маленькие или большие)
c: 1 число
d: 2 спец символа
e: 2 буквы(маленькие)
"""
a = '+-/*!&$#?=@'
b = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = '1234567890'
d = '+-/*!&$#?=@'
e = 'abcdefghijklnopqrstuvwxyz'

a = random.choice(a)
b = random.choices(b, k = 2)
c = random.choice(c)
d = random.choices(d, k = 2)
e = random.choices(e, k = 2)
b = b[0] + b[1]
d = d[0] + d[1]
e = e[0] + e[1]
print(a + str(b) + c + str(d) + str(e))
# a = '+-/!&$#?=@'
# b = 'abcdefghijklnopqrstuvwxyz'
# c = '1234567890'
# d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(random.choice(a)+ random.choice(b+d)+random.choice(b+d)+ random.choice(c)+random.choice(a)+random.choice(a)+random.choice(b)+random.choice(b))
