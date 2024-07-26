'''
Here, We will take a string.
Then splitting it, we will separate all of it's letter, characters.
'''
Letter_count = 0
Digit_count = 0
text = input("Enter any Text :")
for num in text :
    num  = num.lower()
    if num >= 'a' and num <= 'z':
        Letter_count += 1
    if num >= '0' and num <= '9':
        Digit_count += 1
print(f"There are {Letter_count} letters.") 
print(f"There are {Digit_count} digits.") 