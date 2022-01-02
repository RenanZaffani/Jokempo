#Jokempo Program

from random import choice
from time import sleep

print('Welcome to tha game JOKEMPO!')
sleep(1)

user = str(input('Stone, paper or scissors? ')).upper().strip()
sleep(1)

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')

Stone = 'Stone'
Paper = 'Paper'
Scissors = 'Scissors'
list1 = [Stone, Paper, Scissors]
computer = choice(list1)

if computer == Stone and user == 'Stone':
    print(f'Draw! I chose {computer}.')
if computer == Stone and user == 'Paper':
    print(f'You won! I chose {computer}.')
if computer == Stone and user == 'Scissors':
    print(f'You lose! I chose {computer}.')
if computer == Paper and user == 'Stone':
    print(f'You lose! I chose {computer}.')
if computer == Paper and user == 'Paper':
    print(f'Draw! I chose {computer}.')
if computer == Paper and user == 'Scissors':
    print(f'You won! I chose {computer}.')
if computer == Scissors and user == 'Stone':
    print(f'You won! I chose {computer}.')
if computer == Scissors and user == 'Paper':
    print(f'You lose! I chose {computer}.')
if computer == Scissors and user == 'Scissors':
    print(f'Draw! I chose {computer}.')
