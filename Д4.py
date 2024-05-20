'''
def factorial(n) :
    factorial = n

    for i in range(1, n):
        factorial = factorial * i
    return factorial


def is_prime(n) :
    if  n > 0 :
        for i in range(2, int(n*0.5) + 1) :
            if n % i == 0 :
                return False
        return True

def gcd(a, b ) :
    while b :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return abs(a*b // gcd(a, b))

def is_perfect_square(n) :
    if n < 0 :
        return False
    else :
        a = int(n**0.5)
        return n == a * a
'''
'''
import math as m
class Circle :
    def __init__(self, radius) :
        self.radius = radius
    def area(self) :
        return self.radius**2 * math.pi
    def circumference(self) :
        return 2* math.pi * self.radius

class Rectangle :
    def __init__ (self, width, height) :
        self.width = width
        self.height = height
    def area(self) :
        return self.width * self.height
    def perimeter(self) :
        return (self.width + self.height) * 2

class Triangle :
    def __init__ (self, side1, side2, side3) :
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area (self) :
        p = (self.side1 + self.side2 + self.side3)/2
        s = m.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
        return s
    def perimeter (self) :
        return self.side1 + self.side2 + self.side3
'''

#3
'''
from dataclasses import dataclass

@dataclass
class Time_func (n) :
'''

#5
'''
from dataclasses import dataclass

@dataclass
class Person :
    name: str
    age: int
    amail: str
'''

#7
'''
from dataclsses import dataclass

@dataclass
class  Book :
    title: str
    author: str
    year: int
    isbn: str
'''

#6
'''
from dataclasses import dataclass

@dataclass
class Product :
    name: str
    price: float
    quantity: int
'''

#4
'''
def dubug(func) :
    def wrapper(*args, **wargs) :
        print(f'Название {func.__name__} с аргументами: {args}, {kwargs}')
        res = fumc(*args, *wargs)
        print(f'{func.__name__} вернет: {res}')
        return res
    return wrapper
'''

#3

import time
import functools

def time_func(func) :
    @functools.wraps(func)
    def wrapper(*args, **wargs) :
        start = time.time()
        print(f'Запуск функции {func.__name__}')
        res = func(*args, *wargs)
        end = time.time()
        print(f'Функция {func.__name__} выполнена за {end-start:.6f} секунд')
        return res
    return wrapper

























    
