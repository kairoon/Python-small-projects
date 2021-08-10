print('Welcome to our quize game')
playing=input('Do u want to play ')
if playing.lower() != 'yes':
    quit()
print('Lets play')
score=0
answer=input('What does CPU stands for? ').lower()
if answer == 'central processing unit':
    print('Correct! ')
    score+=1
else:
    print('Incorrect')
answer=input('What does GPU stands for? ').lower()
if answer == 'graphics processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect')
answer=input('What does RAM stands for? ').lower()
if answer == 'random access memory':
    print('correct')
    score+=1
else:
    print('Incorrect! ')
print('Yoy got '+str(score)+' questions')
print('you got '+str((score/3)*100)+'%.')

