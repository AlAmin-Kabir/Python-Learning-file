'''Price of a house is $1M
If buyer has good credit,
    They need to put down 10%
Otherwise
    They need to put down 20%
Print the down payment'''
a = 1000000

x = input('Do you have a good credit?\n')

if x=='Yes':
    print("Your downpayment is",int(a*.1))
else:
    print("Your downpayment is",int(a*.2))


