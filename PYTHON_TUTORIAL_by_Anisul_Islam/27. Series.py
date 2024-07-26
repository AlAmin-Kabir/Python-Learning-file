#1+2+3+4+...+n
n = int(input('Enter range :'))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x
print(f'The sum is {sum}')
#1+3+5+7+...+n
sum = 0
for x in range(1,n+1,2):
    sum = sum + x
print(f'The sum is {sum}')
#2+4+6+8+...+n
sum = 0
for x in range(2,n+1,2):
    sum = sum + x
print(f'The sum is {sum}')
#1*1+2*2+3*3+...+n
sum = 0
for x in range(1,n+1,1):
    sum = sum + x*x
print(f'The sum is {sum}')
