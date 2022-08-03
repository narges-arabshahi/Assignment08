import random
options = ['Rock', 'Paper', 'Scissor']
scores = {'user': 0 , 'computer': 0}
for i in range (5):
    computer_select = random.choice(options)
    user_select = input ('play the game: ')
    user_select = user_select.capitalize()
    if user_select == computer_select:
        print('Equal')
    elif user_select == 'Rock':
        if computer_select == 'Scissor':
            print('user wins')
            scores['user'] += 1
        elif computer_select == 'Paper':
            print('computer wins')
            scores['computer'] += 1
    elif user_select == 'Scissor':
        if computer_select == 'Rock':
            print('computer wins')
            scores['computer'] += 1
        elif computer_select == 'Paper':
            print('user wins')
            scores['user'] += 1
    elif user_select == 'Paper':
        if computer_select == 'Rock':
            print('user wins')
            scores['user'] += 1
        elif computer_select == 'Scissor':
            print('computer wins')
            scores['computer'] += 1
    else:
        print('Invalid input')

if scores['computer'] > scores['user']:
    print('computer is winner ', scores['computer'])
else :
    print('user is winner ', scores['user'])