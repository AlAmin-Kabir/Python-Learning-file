#Giving loan only if have a good credit or has a high income or Do not have any criminal record
has_good_income = False
has_good_credit = True
has_criminal_record = True
if has_good_income or has_good_credit and not has_criminal_record :
    print('Eligible for loan')
else:
    print('Sorry, you are not eligible to get a loan')
'''and = Both Conditions Must True
   or = Atleast one conditions Must True'''