def rock_paper_scissors():
    import random
    choices=['Rock','Paper','Scissors']
    comp=random.choice(choices)
    try: 
        player=input("\nPlayer's choice: ").lower().capitalize()
        if player not in choices: print('Invalid Input!\n')
    except ValueError: print('Invalid Input!')
    lose=f"\nYou Lose!\nYour choice- {player}\ncomputer's choce- {comp}"
    win=f"\nYou win!\nYour choice- {player}\ncomputer's choce- {comp}"
    draw=f"You have Drawn!\nYour choice- {player}\ncomputer's choce- {comp}"
    if comp=='Rock':
        if player=='Paper': print(win)
        elif player=='Scissors': print(lose)
        elif player=='Rock': print(draw)
    elif comp=='Scissors':
        if player=='Rock': print(win)
        elif player=='Paper': print(lose)
        elif player=='Scissors': print(draw)
    elif comp=='Paper':
        if player=='Scissors': print(win)
        elif player=='Rock': print(lose)
        elif player=='Paper': print(draw)


while True:
    try: start=input('Do you want to play Rock, Paper, Scissors: ').lower()
    except: ValueEroor: print('Invalid Input!\n')
    if start=='yes': rock_paper_scissors()
    elif start=='no': break
    else: print('Invalid Input!\n')
