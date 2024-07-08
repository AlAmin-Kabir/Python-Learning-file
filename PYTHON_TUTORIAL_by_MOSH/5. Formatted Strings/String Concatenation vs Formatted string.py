first = 'Al-Amin'
last = 'Kabir'
#Expected output = Al-Amin [Kabir] is the author.

#Via String Concatenation
message = first + ' [' + last + '] is a coder.'
print(message)

##Via Formatted String
msg = f'{first} [{last}] is a coder.'
print(msg)