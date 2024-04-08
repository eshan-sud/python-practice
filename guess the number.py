def guessing_game():
    import random
    print()
    lower_limit=0
    upper_limit=10
    choosen_number=random.randint(lower_limit,upper_limit+1)
    number_guesses=3
    count_guesses=0
    guessed_number=None
    print(f'''
-----------------------------------------------------------------------
    About the game--
              
You get {number_guesses} guesses to guess the number choosen randomely
Between {lower_limit} to {upper_limit}

If choosen correctly-- you win

If choosen incorrectly-- you lose

If you exceed your number of guesses-- you lose
-----------------------------------------------------------------------

''')
    while guessed_number!=choosen_number:
        if count_guesses==number_guesses:
            print(f'You lose\nYou have reached your limit!\nThe correct number was: {choosen_number}\n')
            break
        try:
            guessed_number=int(input('Enter Your guess: '))
            count_guesses+=1
            print(f'Your number of guesses: {count_guesses}')
            if guessed_number<choosen_number: print('Too Low!!\n\n')
            elif guessed_number>choosen_number: print('Too High!!\n\n')
        except ValueError: 
            print('Invalid Input!\n\n')
    else:
        print('\n\nYou win\nYou guessed correctly!\n\n')


while True:
    print()
    try: play_guessing_game=input('Do you want to play a guessing game: ').lower()
    except ValueError: print('Invalid Input!!')
    if play_guessing_game=='yes': guessing_game()
    elif play_guessing_game=='no': break
    else: print('Invalid Input!!')
