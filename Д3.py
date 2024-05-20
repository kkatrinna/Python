#1
'''
n = int(input('Введите сколько раз нужно возвести 2 в степень: '))
power_two = lambda x: 2**x

num = list(range(n))

powers = list(map(power_two, num))
for i, power in enumerate(powers) :
    print(f'2 в степени {i} равно {power}')
'''

#2
'''
numbers = [13, 36, 52, 65, 48, 78]
num = lambda x: x % 13 == 0

list_num = list(filter(num, numbers))
print('Числа кратные числу 13: ')
for number in list_num :
    print(number)
'''

#3
'''
def summa (a, b) :
    return a+b
def minus (a, b) :
    return a - b
def mult (a, b) :
    return a * b
def div (a, b) :
    return a / b

print(f'Выберите операцию: \n 1.Сложить \n 2.Вычесть \n 3.Умножить \n 4.Делить')
oper = int(input('Выберите действие(1/2/3/4): '))
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if oper == 1 :
    print(f'a + b = {summa(a, b)}')
elif oper == 2 :
    print(f'a - b = {minus(a, b)}')
elif oper == 3 :
    print(f'a * b = {mult(a, b)}')
elif oper == 4 :
    print(f'a / b = {div(a, b)}')
else :
    print('Неверное действие')
'''
#4
'''
import locale 
import calendar
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

year = int(input('Введите год: '))
month = input('Введите месяц: ')

c = calendar.TextCalendar(calendar.MONDAY)

calend = c.formatmonth(year, datetime.strptime(month, '%B').month)
print('Результат: ')
print(calend)
'''


#5
'''
num = [4, 7, 9]
for i in num :
    for j in range(1, 11) :
        print(f'{i} * {j} = {i*j}')
'''

#6
'''
import math
def calculate_area (radius, pi) :
    A = pi*radius**2
    return A
r = float(input('Введите радиус: '))
pi = math.pi
S = calculate_area(r, pi)
print(f'Площадь окружности равна {S}')
'''

#7
'''
def calculate_average(numbers) :
    if len(numbers) == 0 :
        return 0
    summa = sum(numbers)
    average = summa / len(numbers)
    return average

num = [10, 12, 14, 15]
num2 = [2, 5, 6, 4]
aver = calculate_average(num)
aver2 = calculate_average(num2)
print(f"Среднее арифиетическое равно {aver}")
print(f"Среднее арифиетическое равно {aver2}")
'''

#8
'''
def is_prime(number) :
    if number > 0 :
        for i in range(2, int(number*0.5) + 1) :
            if number % i == 0 :
                return False
        return True
    else :
        print('Число не является натуральным')

num = 14
num2 = 17
num3 = 22
print(f'Число {num} простое? {is_prime(num)}')
print(f'Число {num2} простое? {is_prime(num2)}')
print(f'Число {num3} простое? {is_prime(num3)}')
'''

#9
'''
def find_palindromes(words) :
    palindromes = [word for word in words
           if word == word[::-1]]
    return(palindromes)
word_list = ['магазин', 'шалаш', 'лагерь', 'довод']
word_list2 = ['python', 'madam', 'number', 'level']
palindrome = find_palindromes(word_list)
palindrome2 = find_palindromes(word_list2)
print(f'Палиндромы в списке слов: {palindrome}')
print(f'Палиндромы в списке слов: {palindrome2}')
'''

#Часть 2

#1
'''
def calculate_average (*numbers) :
    number = [num for num in numbers if isinstance(num, (int, float))]
    if number :
        aver = sum(number) / len(number)
        print(f'Среднее значение чисел {numbers}: {aver}')
    else :
        return 0
calculate_average(1, 2, 3, 4)
calculate_average(4, 5, 6)
calculate_average(5, 5)
'''

#2
'''
def reverse_words(text) :
    words = text.split()
    rev = words[::-1]
    return ' '.join(rev)
    
   
print(reverse_words('Строка наоборот'))
print(reverse_words('Это перевернутая строка'))
print(reverse_words('Соединение перевернутых слов в предложение'))
'''

#3
'''
def is_palindrome(text) :
    text = ''.join(c for c in text if c.isalnum()).lower()
    rever = text[::-1]
    return rever == text
print(is_palindrome('шалаш и шалаш'))
print(is_palindrome('это строка'))
'''

#4

def find_longest_subsequence (text, text2) :
    a = len(text)
    b = len(text2)

    if not text or not text2 :
        return ' '
    if text[0] == text2[0] :
        return text[0] + find_longest_subsequence(text[1:], text2[1:])
    else :
        return max(find_longest_subsequence(text[1:], text2),
                   find_longest_subsequence(text, text2[1:]), key = len)

text = find_longest_subsequence('hgfdh', 'hffh')
print(text)




    


























































