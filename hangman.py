human=[
'''
|_____________
|
|
|
|
|
|
|
| 
''',

'''
|_____________
|            |
|
|
|
|
|
|
|
''',

'''
|_____________
|            |
|            |
|
|
|
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|
|
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|            |
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|           /|
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|           /|\
|
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|           /|\
|            |
|
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|           /|\
|            |
|           /
|
''',

'''
|_____________
|            |
|            |
|            |
|            0
|           /|\
|            |
|           / \
|
'''
]
#Plays the game
def play_game():
    def update_word():
        new_word=''
        for character in word:
            if character in list_letters or character in vowels:
                new_word+=character
            else:
                new_word+='_'
        return new_word


    import random
    list_words=['rat','cat','bat','shack','mat','cake']
    word=random.choice(list_words).lower()
    list_letters=[]
    vowels='aeiou'
    guesses=0
    limit_guesses=10
    print(f'''
------------------------------------------------------------
    About the game--

    You get {limit_guesses} tries to guess the word choosen at
    random and save the human from his death!

    If choosen correctly in those {limit_guesses} tries, the
    human survives and you Win!

    If exceeded the number of tries, the human dies and you
    Lose!
------------------------------------------------------------
''')
    #Generates the new_word to be shown to user
    new_word=update_word()
    #Takes input from user and checks if character is in choosen word
    while guesses<limit_guesses:
        print(f'''
------------------------------------------------------------

    {human[guesses]}
    The word is {new_word}
        
    Letters Used--
    {list_letters}
            
    Number Of Guesses left--
    {limit_guesses-guesses}
    
------------------------------------------------------------
''')
        letter=input('Enter a letter: ').lower()
        if letter not in list_letters: list_letters.append(letter)
        if letter in word:
            #Updated version of the new_word
            new_word=update_word()
            #Checks if the player has won
            if new_word==word:
                print(f'''
\tYou win!!\n\tYou guessed correctly\n\tThe word was-- {word}''')
                break
        else: 
            guesses+=1
    #Else block
    else:
        print(f'''
        {human[guesses]}

\tYou Lose!\n\tYou exeeded your guesses\n\tThe word was-- {word}''')


#Asks user for starting the game
while True:
    try: play_hangman_game=input('Do you want to play a game called Hangman: ').lower()
    except ValueError: print('Invalid Input!\n')
    if play_hangman_game=='yes': play_game()
    elif play_hangman_game=='no': break
    else: print('Invalid Input!\n')
