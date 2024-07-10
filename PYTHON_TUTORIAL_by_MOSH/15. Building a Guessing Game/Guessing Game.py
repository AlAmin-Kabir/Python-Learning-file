'''
Build a guess game
Conditions.
1. There will have a secret number;
2. You will have 3 chances to guess properly.
'''
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    number = int(input("Guess : "))
    guess_count += 1
    try_left = guess_limit-guess_count
    if(number==secret_number):
        print("You are right!")
        break
    else:
        if(guess_count <3):
            print(f'Wrong! {try_left} try left')
else:
    print("Sorry, you failed.")