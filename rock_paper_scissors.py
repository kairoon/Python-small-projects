import random
computer_wins = 0
user_wins = 0
options = ['rock','papers','scissors']
while True:
    user_data = input('Type to Rock|papers|Scissors or q for quit ').lower()
    if user_data == 'q':
        break
    if user_data not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print('Computer picked is '+computer_pick+'.')
    if user_data == 'rock' and computer_pick == 'papers':
        print('You got! ')
        user_wins += 1
    elif user_data == 'papers' and computer_pick == 'scissors':
        print('You got! ')
        user_wins += 1
    elif user_data == 'scissors' and computer_pick == 'rock':
        print('You got! ')
        user_wins += 1
    else:
        print('You Lost!')
        computer_wins += 1
print('User Wins '+str(user_wins)+' Times')
print('Computer Wins '+str(computer_wins)+' Times')
print('Good Bye')




