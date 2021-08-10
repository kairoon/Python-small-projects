import random
top_of_range=input('Type a number for guessing random number ')
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('Enter digit value for next time')
        quit()
else:
    print('Enter digit value for next time')
    quit()
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    val=input('Enter value for guessing')
    if val.isdigit():
        val=int(val)
    else:
        print('Enter number for next time')
        continue
    if random_number==val:
        print('You got it')
        break
    else:
        if val<random_number:
            print('You entered number is less than')
        else:
            print('You entered number is greater than')
print('You guesses '+str(guesses)+ ' times')