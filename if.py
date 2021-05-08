number = 23
guess = int(input('Enter an integer : '))
#
if guess == number:
    #new block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    #new block ends here
elif guess < number:
    #Another block
    print ('No, it is a little higher than that')
else:
    print("No, it is a little lower than that")
#
print('Done')
