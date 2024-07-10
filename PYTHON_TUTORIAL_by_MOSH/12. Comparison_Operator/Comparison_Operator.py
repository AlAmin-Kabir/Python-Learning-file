'''
If name is less than 3 Characters long
    Name must be at least 3 Characters
Otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
Otherwise
    Name looks good!
'''
Name = input("What's your name?\n")
if len(Name)<3:
    print("Too Short.")
    Name = input("What's your name?\n")
elif len(Name)>=50:
    print("Too long.")
    Name = input("What's your name?\n")
else:
    print('Good.')

