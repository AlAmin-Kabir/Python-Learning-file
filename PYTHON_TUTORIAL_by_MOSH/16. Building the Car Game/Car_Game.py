'''1
This is a car building game.
Here we will run car
'''
s=0
while True:
    command = input('>').lower()
    if command == 'start':
        if(s == 0):
            print('Car started.')
            s+=1
        else:
            print("Car is already started.")
    elif command == 'stop':
        if(s == 1):
            print('Car stopped.')
            s-=1
        elif(s==0):
            print('Car is already stopped.')
    elif command == 'quit':
        print('Quitting...')
        break
    elif command == 'help':
        print('''
        start - To start the car.
        stop - To stop the car.
        quit - To stop the game.
        ''')
    else:
        print("I did not understand that!")
    