str = input()

alphabet = []
value = 0
for i in str:
    if(i.isalpha()):
        alphabet.append(i)
    else:
        value += int(i)
alphabet.sort()

if value != 0:
    alphabet.append(str(value))

print(''.join(alphabet))

