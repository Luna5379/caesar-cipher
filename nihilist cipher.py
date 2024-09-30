c = input(":")
number = 0
digrams = c.split()
##for z in range(len(digrams)):
##    digrams[z] = int(digrams[z])
print(digrams)
plaintext=['' for k in range(1491)]
for i in range(0, len(digrams)):
    if i % 7 == 0:
        digrams[i] = str(int(digrams[i]) - 55)
    elif i % 7 == 1:
        digrams[i] = str(int(digrams[i]) - 14)
    elif i % 7 == 2:
        digrams[i] = str(int(digrams[i]) - 23)
    elif i % 7 == 3:
        digrams[i] = str(int(digrams[i]) - 45)
    elif i % 7 == 4:
        digrams[i] = str(int(digrams[i]) - 51)
    elif i % 7 == 5:
        digrams[i] = str(int(digrams[i]) - 55)
    elif i % 7 == 6:
        digrams[i] = str(int(digrams[i]) - 44)

for h in range(0, len(digrams)):
    if digrams[h] == '11':
        plaintext[h] = 'z'
    elif digrams[h] == '12':
        plaintext[h] = 'e'
    elif digrams[h] == '13':
        plaintext[h] = 'r'
    elif digrams[h] == '14':
        plaintext[h] = 'o'
    elif digrams[h] == '15':
        plaintext[h] = 'p'
    elif digrams[h] == '21':
        plaintext[h] = 'q'
    elif digrams[h] == '22':
        plaintext[h] = 's'
    elif digrams[h] == '23':
        plaintext[h] = 't'
    elif digrams[h] == '24':
        plaintext[h] = 'u'
    elif digrams[h] == '25':
        plaintext[h] = 'v'
    elif digrams[h] == '31':
        plaintext[h] = 'w'
    elif digrams[h] == '32':
        plaintext[h] = 'x'
    elif digrams[h] == '33':
        plaintext[h] = 'y'
    elif digrams[h] == '34':
        plaintext[h] = 'a'
    elif digrams[h] == '35':
        plaintext[h] = 'b'
    elif digrams[h] == '41':
        plaintext[h] = 'c'
    elif digrams[h] == '42':
        plaintext[h] = 'd'
    elif digrams[h] == '43':
        plaintext[h] = 'f'
    elif digrams[h] == '44':
        plaintext[h] = 'g'
    elif digrams[h] == '45':
        plaintext[h] = 'h'
    elif digrams[h] == '51':
        plaintext[h] = 'i'
    elif digrams[h] == '52':
        plaintext[h] = 'k'
    elif digrams[h] == '53':
        plaintext[h] = 'l'
    elif digrams[h] == '54':
        plaintext[h] = 'm'
    elif digrams[h] == '55':
        plaintext[h] = 'n'
    print(plaintext[h], end='')
print(plaintext)
for o in range(len(plaintext)):
    print(plaintext[o], end='')


##trigrams = ['' for k in range(1488)]
##digrams = ['' for h in range(1488)]
##for i in range(0, 1488, 3):
##    if c[i] != " " and c[i + 1] != " " and c[i + 2] != " ":
##        code = c[i] + c[i + 1] + c[i + 2]
##        trigrams[i] = code
##for j in range(0, 1488, 2):
##    if c[j] != " " and c[j + 1] != " " and c[j + 2] == " ":
##        code = c[j] + c[j + 1]
##        digrams[j] = code
##print(trigrams)
##        number += 1
##print(number)
##for j in range(213):
##    space = 0
##    for d in range(len(c)):
##        if space < 7:
##            if c[d] != " ":
##                print(c[d], end='\t')
##            else:
##                space += 1
##        else:
##            print("\n")
##            break
