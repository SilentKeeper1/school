s = input("Введіть текст для шифрування: ")

if len(s) % 2 != 0:
    s = s + ' '

s1 = ''

for i in range(0, len(s), 2):
    s1 = s1 + s[i+1] + s[i]

print("Зашифрований текст:", s1)
