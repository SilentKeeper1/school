#Завдання 1
from random import randint

t = []

for i in range(7):
    a = randint(-10, 5)
    t.append(a)

print("Список температур за тиждень:", t)
k = 0

zero_count = 0

for i in range(len(t)-1):
    if t[i] * t[i+1] < 0:
        print(f"Зміна знаку між індексами {i} і {i+1}")
        k += 1
    if t[i] == 0:
        zero_count += 1

if t[-1] == 0:
    zero_count += 1

print("Кількість змін знаку температури:", k)
print("Кількість днів з температурою 0:", zero_count)

#Завдання 2

a = [11, 8, 6, 8, 12, 9, 7, 6]

s = sum(a)

av = s / len(a)

print("Середній бал:", round(av))


count_above_avg = 0
for grade in a:
    if grade > av:
        count_above_avg += 1

print("Кількість учнів із оцінкою вище середнього:", count_above_avg)

input_list = input("Введіть оцінки через пробіл: ")
a2 = list(map(int, input_list.split()))

av2 = sum(a2) / len(a2)
print("Середній бал (введені оцінки):", round(av2))

count_above_avg2 = sum(1 for grade in a2 if grade > av2)
print("Кількість учнів із оцінкою вище середнього (введені оцінки):", count_above_avg2)
