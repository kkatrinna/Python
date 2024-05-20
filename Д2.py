'''
for i in range(20, 0, -1) :
    print(i)
print('Поехали!')
'''

#2
'''
weight = float(input("Введите ваш земной вес: "))

for year in range(0, 15):
    earth_weight = weight + year
    moon_weight = earth_weight * 0.165
    print(f"Год {year}: Лунный вес = {moon_weight:.2f} кг")
'''

#3
'''
hour = 3
coin_day = 5
day = int(input('Введите количество рабочих дней: '))
total_coin = hour * coin_day * day
print(f'Количество монет за месяц: {total_coin}')
'''

#4
'''
secret_nicks = ['456', '564', '554', '656']

while True :
    nick = input('Введите ваш ник: ')
    if nick in secret_nicks :
        print(f'{nick}! Добро пожаловать в "Мобильную группу"')
        break
    else : print('Доступ запрещен')
'''

#5
'''
while True :
    try:
        year = int(input('Введите год: '))
        break
    except ValueError :
        print('Неверно. Введите число')        

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print(f'{year} год является високосным')
else :
    print(f'{year} год не является високосным') 
'''

#6
'''
numbers = input('Введите числа через пробел: ')
list_num = numbers.split()
max_num = int(list_num[0])

for number in list_num :
    if int(number) > max_num :
        max_num = int(number)
print(f'Наибольшее число: {max_num}')
'''


#7
'''
num = int(input('Введите число: '))
factorial = 1
for i in range(2, num+1):
    factorial *= i
print(factorial)
'''

#8
'''
for i in range(1, 10) :
    for j in range(1, 10) :
        print('%4d' % (i*j), end=' ')
    print()
'''    

#9
'''
num = int(input('Введите положительное число: '))
if num < 0 :
    num = 0
count = 0
while num > 0 :
    count += num
    num -= 1
print(f'Результат: {count}')
'''

print('Привет')
name = input('Введите ваше имя: ')
races = ['Человек', 'Гном', 'Эльф', 'Хоббит']
print(f'Я рада тебя видеть, {name}!' + 
      f"К какому виду ты принадлежишь: {races}")
hp = 0
damage = 0
race = input()
if race == races[0] :
    hp = 80
    damage = 40
elif race == races[1] :
    hp = 110
    damage = 30
elif race == races[2] :
    hp = 70
    damage = 45
elif race == races[3] :
    hp = 90
    damage = 35
else :
    print('Некорректный выбор расы')

print(f'Имя: {name}')
print(f'Раса: {race}')
print(f'Здоровье: {hp}')
print(f'Урон: {damage}')

leves = ['легкий', 'средний', 'сложный']
print(f'Выберите уровень сложности: {leves}')
level = input()
for level in leves :
    if level == leves[0]:
        hp += 10
        damage += 10
    elif level == leves[1]:
        hp += 20
        damage += 15
    elif level == leves[2]:
        hp += 30
        damage += 25

print('После выбора уровня')
print(f'Здоровье: {hp}')
print(f'Урон: {damage}')
















































        

























    

    


