def palindromes(palindrome):
    
    #Odwrócenie palindromu
    rev = ''.join(reversed(palindrome))
    
    #Sprawdzenie palindromu
    if (palindrome == rev):
        return True
    else:
        return False

#Wypisanie wyniku
palindrome = 'kajak'
result = palindromes(palindrome)

if (result):
    print('Yes')
else:
    print('No')
