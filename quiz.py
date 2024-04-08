def quiz():
    dict_ques={
'''
What is the shape of the earth?
    A. Spehere
    B. Geoid
    C. Flat
    D. Circle''':'b. geoid',
'''
What is the largest Organ in the human body?
    A. Liver
    B. Intestine
    C. Skin
    D. Spine''':'c. skin',
'''
Are you human?
  A. Yes
  B. No''':'a. yes'}
    correct_answers=0
    for quesn in dict_ques:
        print(quesn)
        try: ans=input('Ans- ').lower()
        except ValueError: pass
        if ans in dict_ques[quesn]:
            correct_answers+=1
            print(f'Correct answer!\n')
        else: 
            print(f'Incorrect answer!\nYour answer-{ans}\nCorrect answer- {dict_ques[quesn]}')
    print(f'\n\nTotal correct answers= {correct_answers}')


while True:
    try: start=input('\nDo you want to start the quiz?\n>>>').lower()
    except ValueError: print('Invalid Input!\n')
    if start=='yes': quiz()
    elif start=='no': break
    else: print('Invalid Input!\n')
