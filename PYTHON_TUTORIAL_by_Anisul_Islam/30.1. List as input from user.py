#List as input from the user.
'''
Input will be a string.
    Convert in to integer.
    make the sum of the items.
'''
num = input("Enter the text digit :")
NUM = num.split()
sum = 0
for x in NUM:
    sum = sum + int(x)
print(sum)