import sys
import logging

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b
    
print('Wybierz działanie: 1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie')
while True:
    n = int(input())

    if n == 0:
        print('Dziękujemy za kożystanie z kalkulatora. Nie zapraszamy ponownie.')
        break
    if n == 1:
        print('Podaj 2 liczby:')
        x = int(input())
        y = int(input())
            #dodac logging
    if n == 2:
        print("Podaj 2 liczby:")
        x = int(input())
        y = int(input())
            #dodac logging
    if n == 3:
        print('Podaj 2 liczby:')
        x = int(input())
        y = int(input())
            #dodac logging
    if n == 4:
        print('Podaj 2 liczby:')
        x = int(input())
        y = int(input())
            #dodac logging
    else:
        print('Proszę podać liczbę z zakresu 0-4.')
        break