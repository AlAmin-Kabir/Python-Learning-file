print("Now break")
#Break
i = 1
while i<=4:
    if i == 3:
        break
    print(i)
    i += 1
print("Now continue")
#Continue
j = 1
while j<=4:
    print(j)
    j = j + 1
    if j == 3:
        continue
    