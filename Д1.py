'''madness = 'Безумие'
already = 'Я уже'
what = ', что такое'
replay = 'повторение'
that = 'и того'
once = 'раз за разом'
change = 'на изменение. Это'

print(already + ' говорил тебе' + what + ' безумие? ' + madness +
      ' - это точное ' + replay + ' одного ' + that + ' же действия, ' +
      once + ', в надежде ' + change + ' и есть безумие.')'''
'''
car = 'машину'
race = 'автогонку'
name_1 = 'Вова'
name_2 = 'Кира'
ticket = 'билеты'
meteorite = 'метеоритом'
spaceship = 'Космическом корабле'
pirat = 'пиратов'

print(name_1 + ' и ' + name_2 + ' мечтали о ' + spaceship +
      ' и представляли себя в качестве ' + pirat +
      '. Однажды они наблюдали за ' + meteorite +
      ' и решили действовать. ' +
      name_1 + ' и ' + name_2 + ' нашли старую ' + car + ' и, раздобыв ' +
      ticket + ' к мечте, начали '
      + race + ' к звездам')

'''

'''name = 'Лара Крофт'
plus = '3+5'
num_float = 782.3
logic = False
num_int = 146

print(type(name))
print(type(plus))
print(type(num_float))
print(type(logic))
print(type(num_int))'''

'''age = int(input('Введите ваш возраст: '))
if age >= 18:
    print('Вы совершеннолетний/совершеннолетняя!')
else :
    print('Вы несовершеннолеиний/несовершеннолетняя!')'''

'''
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
oper = input('Введите оператор: ')
plus = '+'
minus = '-'
mult = '*'
division = '/'
int_division = '//'
module_division = '%'
square = '**'
if oper == plus :
    print(num_1 + num_2)
elif oper == minus :
    print(num_1 - num_2)
elif oper == mult :
    print(num_1 * num_2)
elif oper == division :
    print(num_1 / num_2)
elif oper == int_division :
    print(num_1 // num_2)
elif oper == module_division :
    print(num_1 % num_2)
elif oper == square :
    print(num_1 ** num_2)
else : print('Неверный оператор!')'''

'''num = int(input('Введите число: '))
if num % 2==0 :
    print('Четное')
else : print('Нечетное')'''

'''num = int(input('Введите двузначное число: '))
if num % 11 ==0 :
    print('Да')
else : print('Нет')'''


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
count = 0

if a%2==0 :
    count+=1
if b%2==0 : 
    count+=1
if c%2==0 :
    count+=1
else : print('Error')
print('Количество четных чисел = ', count)


'''
m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))

if m % n == 0 :
    print(m // n)
else : print('Error')
'''
'''
num = int(input('Введите трехзначное число: '))

if num%10 > (num//10)%10 :
    print(num%10)
else : print((num//10)%10)
'''
'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a+b>c and a+c>b and b+c>a :
    if a==b==c :
        print('равносторонний')
    elif a==b or a==c or b==c :
        print('равнобедренный')
    else : print('разносторонний')
    
else : print('Error')
'''

'''
year = int(input('Введите год рождения: '))

animal = year %12

if animal == 0: print('Обезьяна')
elif animal == 1: print('Петух')
elif animal == 2: print('Собака')
elif animal == 3: print('Свинья')
elif animal == 4: print('Крыса')
elif animal == 5: print('Бык')
elif animal == 6: print('Тигр')
elif animal == 7: print('Заяц')
elif animal == 8: print('Дракон')
elif animal == 9: print('Змея')
elif animal == 10: print('Лошадь')
elif animal == 11: print('Овца')
'''

'''
estimation = int(input('Введите оценку: '))

if 0<=estimation<=100 :
    if estimation>=90 :
        print('A')
    elif estimation>=80 :
        print('B')
    elif estimation >=70 :
        print('C')
    elif estimation >= 60 :
        print('D')
    else : print('F')
    
else : print('Error')
'''

'''
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')

concat = str1 + str2

if concat == concat[::-1] :
    print('Строка является палиндромом')
else :
    print('Строка не является палиндромом')
'''
'''
from random import randint
num = randint(1, 100)
count = 0

while True:
    use_num = int(input('Угадайте число от 1 до 100: '))
    count += 1
    if use_num < num :
        print('Ваше число меньше загаданного')
    elif use_num > num :
        print('Ваше число больше загаданного')
    else :
        print('Вы угадали. Число = ', use_num, 'Количество попыток: ', count)
        break
'''







































































































































































































































