import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

if __name__ == "__main__":    
    print('Wybierz działanie: 1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie')
    while True:
        n = float(input())
        if n == 1:
            print('Podaj 1 liczbę:')
            x = float(input())
            print('Podaj 2 liczbę:')
            y = float(input())
            print(dodawanie(x,y))
            break    
        elif n == 2:
            print('Podaj 1 liczbę:')
            x = float(input())
            print('Podaj 2 liczbę:')
            y = float(input())
            print(odejmowanie(x,y))
            break 
        elif n == 3:
            print('Podaj 1 liczbę:')
            x = float(input())
            print('Podaj 2 liczbę:')
            y = float(input())
            print(mnozenie(x,y))
            break 
        elif n == 4:
            print('Podaj 1 liczbę:')
            x = float(input())
            print('Podaj 2 liczbę:')
            y = float(input())
            if y == 0:
                print('Dziekujemy za korzystanie z kalkulatora. Nie zapraszamy ponownie.')
            print(dzielenie(x,y))
            break 
        else:
            print('Proszę podać liczbę z zakresu 1-4.')
            break