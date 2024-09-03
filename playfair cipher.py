ciphertext = 'ThepointIadvanceifitneedconfirmationIllprovebyawitnessthatfewwilldisputeApinkofperfectionandtruthinthenationWherefashionandfollyareallofasui'
digrams = ['' for z in range(len(ciphertext)//2)]
for i in range(0, len(ciphertext), 2):
    print(i)
    if (i + 1) <= len(ciphertext) and (i//2) <= len(digrams):
        digrams[i//2] = ciphertext[i] + ciphertext[i + 1]
print(digrams)
currentAlpha = []
g = 0
m = 0
o = 0
def gridCipherCheck(ciphertext, currentAlpha):
    for i in range(len(ciphertext)):
        if ciphertext[i].upper() not in currentAlpha:
            currentAlpha.append(ciphertext[i].upper())
    return currentAlpha
def gridCheck(ciphertext, grid, gridColumn1, gridRow1, letter1, gridColumn2, gridRow2, letter2):
    for i in range(5):
        for j in range(5):
            if letter1 == grid[i][j]:
                gridColumn1 = i
                gridRow1 = j
                for k in range(5):
                    for l in range(5):
                        if letter2 == grid[k][l]:
                            gridColumn2 = k
                            gridRow2 = l
                            return gridColumn1, gridColumn2, gridRow1, gridRow2
##            elif ciphertext[m+g] in grid[i]:
##                gridColumn = i
##                for k in range(5):
##                    if ciphertext[m+o] == grid[i][k]:
##                        gridRow = k
##                        return gridColumn, gridRow
##                    o += 1
##            elif ciphertext[m+g] in grid
##            m +=1
##        g +=1
gridColumn1 = 0
gridRow1 = 0
gridColumn2 = 0
gridRow2 = 0
currentAlpha = gridCipherCheck(ciphertext,currentAlpha)
print(currentAlpha)
print(len(currentAlpha))
grid = [['T', 'R', 'E', 'N', 'D'], ['I', 'G', 'H', 'K', 'L'], ['M', 'O', 'P', 'Q', 'S'], ['U', 'V', 'W', 'X', 'Y'], ['Z', 'A', 'B', 'C', 'F']]
plaintext = ['' for j in range(len(ciphertext))]
for index in range(0, len(ciphertext), 2):
    gridColumn1, gridRow1, gridColumn2, gridRow2 = gridCheck(ciphertext, grid, gridColumn1, gridRow1, ciphertext[index].upper(), gridColumn2, gridRow2, ciphertext[index + 1].upper())
    if gridColumn1 == gridColumn2:
        plaintext[index] = grid[gridColumn1 - 6][gridRow1]
        plaintext[index + 1] = grid[gridColumn2 - 6][gridRow2]
    elif gridRow1 == gridRow2:
        plaintext[index] = grid[gridColumn1][gridRow1 - 6]
        plaintext[index + 1] = grid[gridColumn2][gridRow2 - 6]
    else:
        plaintext[index] = grid[gridColumn2][gridRow1]
        plaintext[index] = grid[gridColumn1][gridRow2]
print(plaintext)
