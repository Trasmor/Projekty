import sys
import logging

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if a == 0 :
        print('Nie można dzielić przez 0!')
        quit()
    else:
        return a / b
    

