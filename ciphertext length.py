c = input(":")
number = 0
for i in range(len(c)):
    if c[i] != " ":
        number += 1
print(number)
##for j in range(len(c)):
##    if c[i] != " ":
##        print(c[j], end='')
##    else: print("\n")
##for h in range(0, number, 125):
##    for j in range(125):
##        if j % 5 != 4:
##            print(c[h+j], end = '\t')
##        elif j % 5 == 4:
##            print(c[h+j], end = '\n')
##    print('\n')
