# instagram -> abbas_hz81
# https://github.com/hzabbas
# Goal or nonsense game
import random 
cups = int(input('How many cups ? : '))
chances = int(input('How many chance ? : '))
ai = random.randint(1,cups)
word = 's'
for i in range(chances) :
    if chances - i == 1 :
        word = ''
    print('*'*15)
    print(f'{chances - i} chances left .')
    user_gueses = int(input(f'gueses [1-{cups}] : '))
    if user_gueses == ai :
        print('You gussed right !')
        break
    else :
        print('wrong guessed')
print('*'*15)
if user_gueses == ai :
    print('you won !')
else:
    print(f'you lost .sorry ! Correct answer -> {ai}')