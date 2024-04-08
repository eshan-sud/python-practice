def countdown(time_elapse):
    import time
    print('Timer started--')
    for number in range(1,time_elapse+1):
        min,sec = number//60 , number%60
        timer = '{:02d}:{:02d}'.format(min,sec)
        print('\r',timer,end='')
        time.sleep(1)
    print('\rTimer Ended!!')


while True:
    try: start=input('\nDo you want to start a timer: ').lower()
    except ValueError: print('Invalid Input!')
    if start=='yes':
        try:
            time_elapse=int(input('Enter the time to elapse:'))
            countdown(time_elapse=5)
        except: ValueError: print('Invalid Input!')
    elif start=='no': break
    else: print('Invalid Input!')
