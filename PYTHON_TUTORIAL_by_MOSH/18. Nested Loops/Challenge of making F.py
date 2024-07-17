'''
You have to create an F,
Using the Nested for loop.
'''
x_count = [5,2,5,2,2]
for x in x_count:
    output = ''
    for y in range(x):
        output +='x'
    print(output)
x_count = [5,2,5,2,2]
for x in x_count:
    hi = ('x'*x)
    print(hi)