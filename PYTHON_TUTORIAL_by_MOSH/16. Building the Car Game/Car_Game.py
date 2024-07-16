'''1
This is a car building game.
Here we will run car
'''
a=0
while True:
    command = input('>').lower()
    if command == 'start':
        if(a == 0):
            print('Car started.')
            a+=1
        else:
            print("Car is already started.")
    elif command == 'stop':
        print('Car stopped.')
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
    