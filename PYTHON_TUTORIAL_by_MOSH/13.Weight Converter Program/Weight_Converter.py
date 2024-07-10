'''1. Takes a input.
2. Tell if it's kg/Lbs.
3. If kg-convert to Lbs.
4. If Lbs-convert to kg.'''
Weight = float(input('Enter Weight.\n'))
I = input('Kg or Lbs?')
if I=="K":
    Converted = Weight*2.20462
    print('The weight is ',Converted,' lb(s)')
else:
    Converted = Weight*0.453592
    print(f'The weight is ',Converted,' kg(s)')