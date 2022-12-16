"""
Sprawdź czy tekst 'aAaAaA' znajduje się w tablicy passwords.
W zależności czy znajduje się czy też nie, wyświetl na ekranie odpowiedni komunikat.
"""

passwords = ['aaAaa', 'aAAAaa', 'aaaaaaA', 'aaaAAAAA', 'aaAAAaa', 'aAaAaA', 'aAaAaAA']

haslo = 'aAaAaA'
haslo1 = 'aAaAaAaaaa'

if haslo in passwords:
    print(f'Haslo "{haslo}" znajduje się na liście.')
else:
    print(f'Haslo "{haslo}" nie znajduje się na liście.')

if haslo1 in passwords:
    print(f'Haslo "{haslo1}" znajduje się na liście.')
else:
    print(f'Haslo "{haslo1}" nie znajduje się na liście.')