alphabet = [['a', 0],['b', 0],['c', 0],['d', 0],['e', 0],['f', 0],['g', 0],['h', 0],['i', 0],['j', 0],['k', 0],['l', 0],['m', 0],['n', 0],['o', 0],['p', 0],['q', 0],['r', 0],['s', 0],['t', 0],['u', 0],['v', 0],['w', 0],['x', 0],['y', 0],['z', 0]]
ciphertext = input(":")
cipher1 = []
cipher2 = []
cipher3 = []
cipher4 = []
cipher5 = []
cipher7 = []
cipher8 = []
cipher9 = []
for i in range(len(ciphertext)):
    for j in range(0, 26):
        if ciphertext[i].lower() == alphabet[j][0]:
            alphabet[j][1] = alphabet[j][1] + 1
            #print(alphabet[j])
            #print("f")
        #print("g")
    #print("h")

iocA = (alphabet[0][1] / len(ciphertext)) * (alphabet[0][1] / len(ciphertext))
print("iocA = " + str(iocA))
iocB = (alphabet[1][1] / len(ciphertext)) * (alphabet[1][1] / len(ciphertext))
print("iocB = " + str(iocB))
iocC = (alphabet[2][1] / len(ciphertext)) * (alphabet[2][1] / len(ciphertext))
print("iocC = " + str(iocC))
iocD = (alphabet[3][1] / len(ciphertext)) * (alphabet[3][1] / len(ciphertext))
print("iocD = " + str(iocD))
iocE = (alphabet[4][1] / len(ciphertext)) * (alphabet[4][1] / len(ciphertext))
print("iocE = " + str(iocE))
iocF = (alphabet[5][1] / len(ciphertext)) * (alphabet[5][1] / len(ciphertext))
print("iocF = " + str(iocF))
iocG = (alphabet[6][1] / len(ciphertext)) * (alphabet[6][1] / len(ciphertext))
print("iocG = " + str(iocG))
iocH = (alphabet[7][1] / len(ciphertext)) * (alphabet[7][1] / len(ciphertext))
print("iocH = " + str(iocH))
iocI = (alphabet[8][1] / len(ciphertext)) * (alphabet[8][1] / len(ciphertext))
print("iocI = " + str(iocI))
iocJ = (alphabet[9][1] / len(ciphertext)) * (alphabet[9][1] / len(ciphertext))
print("iocJ = " + str(iocJ))
iocK = (alphabet[10][1] / len(ciphertext)) * (alphabet[10][1] / len(ciphertext))
print("iocK = " + str(iocK))
iocL = (alphabet[11][1] / len(ciphertext)) * (alphabet[11][1] / len(ciphertext))
print("iocL = " + str(iocL))
iocM = (alphabet[12][1] / len(ciphertext)) * (alphabet[12][1] / len(ciphertext))
print("iocM = " + str(iocM))
iocN = (alphabet[13][1] / len(ciphertext)) * (alphabet[13][1] / len(ciphertext))
print("iocN = " + str(iocN))
iocO = (alphabet[14][1] / len(ciphertext)) * (alphabet[14][1] / len(ciphertext))
print("iocO = " + str(iocO))
iocP = (alphabet[15][1] / len(ciphertext)) * (alphabet[15][1] / len(ciphertext))
print("iocP = " + str(iocP))
iocQ = (alphabet[16][1] / len(ciphertext)) * (alphabet[16][1] / len(ciphertext))
print("iocQ = " + str(iocQ))
iocR = (alphabet[17][1] / len(ciphertext)) * (alphabet[17][1] / len(ciphertext))
print("iocR = " + str(iocR))
iocS = (alphabet[18][1] / len(ciphertext)) * (alphabet[18][1] / len(ciphertext))
print("iocS = " + str(iocS))
iocT = (alphabet[19][1] / len(ciphertext)) * (alphabet[19][1] / len(ciphertext))
print("iocT = " + str(iocT))
iocU = (alphabet[20][1] / len(ciphertext)) * (alphabet[20][1] / len(ciphertext))
print("iocU = " + str(iocU))
iocV = (alphabet[21][1] / len(ciphertext)) * (alphabet[21][1] / len(ciphertext))
print("iocV = " + str(iocV))
iocW = (alphabet[22][1] / len(ciphertext)) * (alphabet[22][1] / len(ciphertext))
print("iocW = " + str(iocW))
iocX = (alphabet[23][1] / len(ciphertext)) * (alphabet[23][1] / len(ciphertext))
print("iocX = " + str(iocX))
iocY = (alphabet[24][1] / len(ciphertext)) * (alphabet[24][1] / len(ciphertext))
print("iocY = " + str(iocY))
iocZ = (alphabet[25][1] / len(ciphertext)) * (alphabet[25][1] / len(ciphertext))
print("iocZ = " + str(iocZ))

totalIOC = iocA + iocB + iocC + iocD + iocE + iocF + iocG + iocH + iocI + iocJ + iocK + iocL + iocM + iocN + iocO + iocP + iocQ + iocR + iocS + iocT + iocU + iocV + iocW + iocX + iocY + iocZ
print("total = " + str(totalIOC))
#print(alphabet)
#for t in range(2, 9):
for y in range(0, 26):
    alphabet[y][1] = 0
#print(alphabet)
for z in range(1, len(ciphertext), 6):
    if ciphertext[z] != ' ':
        cipher1.append(ciphertext[z])
    if ciphertext[z + 1] != ' ':
        cipher2.append(ciphertext[z + 1])
    if len(ciphertext) > (z+2):
        if ciphertext[z + 2] != ' ':
            cipher3.append(ciphertext[z + 2])
    if len(ciphertext) > (z+3):
        if ciphertext[z + 3] != ' ':
            cipher4.append(ciphertext[z + 3])
    if len(ciphertext) > (z+4):
        if ciphertext[z + 4] != ' ':
            cipher5.append(ciphertext[z + 4])
    if len(ciphertext) > (z+6):
        if ciphertext[z + 6] != ' ':
            cipher7.append(ciphertext[z + 6])
    if len(ciphertext) > (z+7):
        if ciphertext[z + 7] != ' ':
            cipher8.append(ciphertext[z + 7])
    if len(ciphertext) > (z+8):
        if ciphertext[z + 8] != ' ':
            cipher9.append(ciphertext[z + 8])
for x in range(len(cipher1)):
    print(cipher1[x], "")

for h in range(len(cipher1)):
    for g in range(0, 26):
        if cipher1[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc1A = (alphabet[0][1] / len(cipher1)) * (alphabet[0][1] / len(cipher1))
ioc1B = (alphabet[1][1] / len(cipher1)) * (alphabet[1][1] / len(cipher1))
ioc1C = (alphabet[2][1] / len(cipher1)) * (alphabet[2][1] / len(cipher1))
ioc1D = (alphabet[3][1] / len(cipher1)) * (alphabet[3][1] / len(cipher1))
ioc1E = (alphabet[4][1] / len(cipher1)) * (alphabet[4][1] / len(cipher1))
ioc1F = (alphabet[5][1] / len(cipher1)) * (alphabet[5][1] / len(cipher1))
ioc1G = (alphabet[6][1] / len(cipher1)) * (alphabet[6][1] / len(cipher1))
ioc1H = (alphabet[7][1] / len(cipher1)) * (alphabet[7][1] / len(cipher1))
ioc1I = (alphabet[8][1] / len(cipher1)) * (alphabet[8][1] / len(cipher1))
ioc1J = (alphabet[9][1] / len(cipher1)) * (alphabet[9][1] / len(cipher1))
ioc1K = (alphabet[10][1] / len(cipher1)) * (alphabet[10][1] / len(cipher1))
ioc1L = (alphabet[11][1] / len(cipher1)) * (alphabet[11][1] / len(cipher1))
ioc1M = (alphabet[12][1] / len(cipher1)) * (alphabet[12][1] / len(cipher1))
ioc1N = (alphabet[13][1] / len(cipher1)) * (alphabet[13][1] / len(cipher1))
ioc1O = (alphabet[14][1] / len(cipher1)) * (alphabet[14][1] / len(cipher1))
ioc1P = (alphabet[15][1] / len(cipher1)) * (alphabet[15][1] / len(cipher1))
ioc1Q = (alphabet[16][1] / len(cipher1)) * (alphabet[16][1] / len(cipher1))
ioc1R = (alphabet[17][1] / len(cipher1)) * (alphabet[17][1] / len(cipher1))
ioc1S = (alphabet[18][1] / len(cipher1)) * (alphabet[18][1] / len(cipher1))
ioc1T = (alphabet[19][1] / len(cipher1)) * (alphabet[19][1] / len(cipher1))
ioc1U = (alphabet[20][1] / len(cipher1)) * (alphabet[20][1] / len(cipher1))
ioc1V = (alphabet[21][1] / len(cipher1)) * (alphabet[21][1] / len(cipher1))
ioc1W = (alphabet[22][1] / len(cipher1)) * (alphabet[22][1] / len(cipher1))
ioc1X = (alphabet[23][1] / len(cipher1)) * (alphabet[23][1] / len(cipher1))
ioc1Y = (alphabet[24][1] / len(cipher1)) * (alphabet[24][1] / len(cipher1))
ioc1Z = (alphabet[25][1] / len(cipher1)) * (alphabet[25][1] / len(cipher1))
total1IOC = ioc1A + ioc1B + ioc1C + ioc1D + ioc1E + ioc1F + ioc1G + ioc1H + ioc1I + ioc1J + ioc1K + ioc1L + ioc1M + ioc1N + ioc1O + ioc1P + ioc1Q + ioc1R + ioc1S + ioc1T + ioc1U + ioc1V + ioc1W + ioc1X + ioc1Y + ioc1Z
print(total1IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher2)):
    for g in range(0, 26):
        if cipher2[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc2A = (alphabet[0][1] / len(cipher2)) * (alphabet[0][1] / len(cipher2))
ioc2B = (alphabet[1][1] / len(cipher2)) * (alphabet[1][1] / len(cipher2))
ioc2C = (alphabet[2][1] / len(cipher2)) * (alphabet[2][1] / len(cipher2))
ioc2D = (alphabet[3][1] / len(cipher2)) * (alphabet[3][1] / len(cipher2))
ioc2E = (alphabet[4][1] / len(cipher2)) * (alphabet[4][1] / len(cipher2))
ioc2F = (alphabet[5][1] / len(cipher2)) * (alphabet[5][1] / len(cipher2))
ioc2G = (alphabet[6][1] / len(cipher2)) * (alphabet[6][1] / len(cipher2))
ioc2H = (alphabet[7][1] / len(cipher2)) * (alphabet[7][1] / len(cipher2))
ioc2I = (alphabet[8][1] / len(cipher2)) * (alphabet[8][1] / len(cipher2))
ioc2J = (alphabet[9][1] / len(cipher2)) * (alphabet[9][1] / len(cipher2))
ioc2K = (alphabet[10][1] / len(cipher2)) * (alphabet[10][1] / len(cipher2))
ioc2L = (alphabet[11][1] / len(cipher2)) * (alphabet[11][1] / len(cipher2))
ioc2M = (alphabet[12][1] / len(cipher2)) * (alphabet[12][1] / len(cipher2))
ioc2N = (alphabet[13][1] / len(cipher2)) * (alphabet[13][1] / len(cipher2))
ioc2O = (alphabet[14][1] / len(cipher2)) * (alphabet[14][1] / len(cipher2))
ioc2P = (alphabet[15][1] / len(cipher2)) * (alphabet[15][1] / len(cipher2))
ioc2Q = (alphabet[16][1] / len(cipher2)) * (alphabet[16][1] / len(cipher2))
ioc2R = (alphabet[17][1] / len(cipher2)) * (alphabet[17][1] / len(cipher2))
ioc2S = (alphabet[18][1] / len(cipher2)) * (alphabet[18][1] / len(cipher2))
ioc2T = (alphabet[19][1] / len(cipher2)) * (alphabet[19][1] / len(cipher2))
ioc2U = (alphabet[20][1] / len(cipher2)) * (alphabet[20][1] / len(cipher2))
ioc2V = (alphabet[21][1] / len(cipher2)) * (alphabet[21][1] / len(cipher2))
ioc2W = (alphabet[22][1] / len(cipher2)) * (alphabet[22][1] / len(cipher2))
ioc2X = (alphabet[23][1] / len(cipher2)) * (alphabet[23][1] / len(cipher2))
ioc2Y = (alphabet[24][1] / len(cipher2)) * (alphabet[24][1] / len(cipher2))
ioc2Z = (alphabet[25][1] / len(cipher2)) * (alphabet[25][1] / len(cipher2))
total2IOC = ioc2A + ioc2B + ioc2C + ioc2D + ioc2E + ioc2F + ioc2G + ioc2H + ioc2I + ioc2J + ioc2K + ioc2L + ioc2M + ioc2N + ioc2O + ioc2P + ioc2Q + ioc2R + ioc2S + ioc2T + ioc2U + ioc2V + ioc2W + ioc2X + ioc2Y + ioc2Z
print(total2IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher3)):
    for g in range(0, 26):
        if cipher3[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc3A = (alphabet[0][1] / len(cipher3)) * (alphabet[0][1] / len(cipher3))
ioc3B = (alphabet[1][1] / len(cipher3)) * (alphabet[1][1] / len(cipher3))
ioc3C = (alphabet[2][1] / len(cipher3)) * (alphabet[2][1] / len(cipher3))
ioc3D = (alphabet[3][1] / len(cipher3)) * (alphabet[3][1] / len(cipher3))
ioc3E = (alphabet[4][1] / len(cipher3)) * (alphabet[4][1] / len(cipher3))
ioc3F = (alphabet[5][1] / len(cipher3)) * (alphabet[5][1] / len(cipher3))
ioc3G = (alphabet[6][1] / len(cipher3)) * (alphabet[6][1] / len(cipher3))
ioc3H = (alphabet[7][1] / len(cipher3)) * (alphabet[7][1] / len(cipher3))
ioc3I = (alphabet[8][1] / len(cipher3)) * (alphabet[8][1] / len(cipher3))
ioc3J = (alphabet[9][1] / len(cipher3)) * (alphabet[9][1] / len(cipher3))
ioc3K = (alphabet[10][1] / len(cipher3)) * (alphabet[10][1] / len(cipher3))
ioc3L = (alphabet[11][1] / len(cipher3)) * (alphabet[11][1] / len(cipher3))
ioc3M = (alphabet[12][1] / len(cipher3)) * (alphabet[12][1] / len(cipher3))
ioc3N = (alphabet[13][1] / len(cipher3)) * (alphabet[13][1] / len(cipher3))
ioc3O = (alphabet[14][1] / len(cipher3)) * (alphabet[14][1] / len(cipher3))
ioc3P = (alphabet[15][1] / len(cipher3)) * (alphabet[15][1] / len(cipher3))
ioc3Q = (alphabet[16][1] / len(cipher3)) * (alphabet[16][1] / len(cipher3))
ioc3R = (alphabet[17][1] / len(cipher3)) * (alphabet[17][1] / len(cipher3))
ioc3S = (alphabet[18][1] / len(cipher3)) * (alphabet[18][1] / len(cipher3))
ioc3T = (alphabet[19][1] / len(cipher3)) * (alphabet[19][1] / len(cipher3))
ioc3U = (alphabet[20][1] / len(cipher3)) * (alphabet[20][1] / len(cipher3))
ioc3V = (alphabet[21][1] / len(cipher3)) * (alphabet[21][1] / len(cipher3))
ioc3W = (alphabet[22][1] / len(cipher3)) * (alphabet[22][1] / len(cipher3))
ioc3X = (alphabet[23][1] / len(cipher3)) * (alphabet[23][1] / len(cipher3))
ioc3Y = (alphabet[24][1] / len(cipher3)) * (alphabet[24][1] / len(cipher3))
ioc3Z = (alphabet[25][1] / len(cipher3)) * (alphabet[25][1] / len(cipher3))
total3IOC = ioc3A + ioc3B + ioc3C + ioc3D + ioc3E + ioc3F + ioc3G + ioc3H + ioc3I + ioc3J + ioc3K + ioc3L + ioc3M + ioc3N + ioc3O + ioc3P + ioc3Q + ioc3R + ioc3S + ioc3T + ioc3U + ioc3V + ioc3W + ioc3X + ioc3Y + ioc3Z
print(total3IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher4)):
    for g in range(0, 26):
        if cipher4[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc4A = (alphabet[0][1] / len(cipher4)) * (alphabet[0][1] / len(cipher4))
ioc4B = (alphabet[1][1] / len(cipher4)) * (alphabet[1][1] / len(cipher4))
ioc4C = (alphabet[2][1] / len(cipher4)) * (alphabet[2][1] / len(cipher4))
ioc4D = (alphabet[3][1] / len(cipher4)) * (alphabet[3][1] / len(cipher4))
ioc4E = (alphabet[4][1] / len(cipher4)) * (alphabet[4][1] / len(cipher4))
ioc4F = (alphabet[5][1] / len(cipher4)) * (alphabet[5][1] / len(cipher4))
ioc4G = (alphabet[6][1] / len(cipher4)) * (alphabet[6][1] / len(cipher4))
ioc4H = (alphabet[7][1] / len(cipher4)) * (alphabet[7][1] / len(cipher4))
ioc4I = (alphabet[8][1] / len(cipher4)) * (alphabet[8][1] / len(cipher4))
ioc4J = (alphabet[9][1] / len(cipher4)) * (alphabet[9][1] / len(cipher4))
ioc4K = (alphabet[10][1] / len(cipher4)) * (alphabet[10][1] / len(cipher4))
ioc4L = (alphabet[11][1] / len(cipher4)) * (alphabet[11][1] / len(cipher4))
ioc4M = (alphabet[12][1] / len(cipher4)) * (alphabet[12][1] / len(cipher4))
ioc4N = (alphabet[13][1] / len(cipher4)) * (alphabet[13][1] / len(cipher4))
ioc4O = (alphabet[14][1] / len(cipher4)) * (alphabet[14][1] / len(cipher4))
ioc4P = (alphabet[15][1] / len(cipher4)) * (alphabet[15][1] / len(cipher4))
ioc4Q = (alphabet[16][1] / len(cipher4)) * (alphabet[16][1] / len(cipher4))
ioc4R = (alphabet[17][1] / len(cipher4)) * (alphabet[17][1] / len(cipher4))
ioc4S = (alphabet[18][1] / len(cipher4)) * (alphabet[18][1] / len(cipher4))
ioc4T = (alphabet[19][1] / len(cipher4)) * (alphabet[19][1] / len(cipher4))
ioc4U = (alphabet[20][1] / len(cipher4)) * (alphabet[20][1] / len(cipher4))
ioc4V = (alphabet[21][1] / len(cipher4)) * (alphabet[21][1] / len(cipher4))
ioc4W = (alphabet[22][1] / len(cipher4)) * (alphabet[22][1] / len(cipher4))
ioc4X = (alphabet[23][1] / len(cipher4)) * (alphabet[23][1] / len(cipher4))
ioc4Y = (alphabet[24][1] / len(cipher4)) * (alphabet[24][1] / len(cipher4))
ioc4Z = (alphabet[25][1] / len(cipher4)) * (alphabet[25][1] / len(cipher4))
total4IOC = ioc4A + ioc4B + ioc4C + ioc4D + ioc4E + ioc4F + ioc4G + ioc4H + ioc4I + ioc4J + ioc4K + ioc4L + ioc4M + ioc4N + ioc4O + ioc4P + ioc4Q + ioc4R + ioc4S + ioc4T + ioc4U + ioc4V + ioc4W + ioc4X + ioc4Y + ioc4Z
print(total4IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher5)):
    for g in range(0, 26):
        if cipher5[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc5A = (alphabet[0][1] / len(cipher5)) * (alphabet[0][1] / len(cipher5))
ioc5B = (alphabet[1][1] / len(cipher5)) * (alphabet[1][1] / len(cipher5))
ioc5C = (alphabet[2][1] / len(cipher5)) * (alphabet[2][1] / len(cipher5))
ioc5D = (alphabet[3][1] / len(cipher5)) * (alphabet[3][1] / len(cipher5))
ioc5E = (alphabet[4][1] / len(cipher5)) * (alphabet[4][1] / len(cipher5))
ioc5F = (alphabet[5][1] / len(cipher5)) * (alphabet[5][1] / len(cipher5))
ioc5G = (alphabet[6][1] / len(cipher5)) * (alphabet[6][1] / len(cipher5))
ioc5H = (alphabet[7][1] / len(cipher5)) * (alphabet[7][1] / len(cipher5))
ioc5I = (alphabet[8][1] / len(cipher5)) * (alphabet[8][1] / len(cipher5))
ioc5J = (alphabet[9][1] / len(cipher5)) * (alphabet[9][1] / len(cipher5))
ioc5K = (alphabet[10][1] / len(cipher5)) * (alphabet[10][1] / len(cipher5))
ioc5L = (alphabet[11][1] / len(cipher5)) * (alphabet[11][1] / len(cipher5))
ioc5M = (alphabet[12][1] / len(cipher5)) * (alphabet[12][1] / len(cipher5))
ioc5N = (alphabet[13][1] / len(cipher5)) * (alphabet[13][1] / len(cipher5))
ioc5O = (alphabet[14][1] / len(cipher5)) * (alphabet[14][1] / len(cipher5))
ioc5P = (alphabet[15][1] / len(cipher5)) * (alphabet[15][1] / len(cipher5))
ioc5Q = (alphabet[16][1] / len(cipher5)) * (alphabet[16][1] / len(cipher5))
ioc5R = (alphabet[17][1] / len(cipher5)) * (alphabet[17][1] / len(cipher5))
ioc5S = (alphabet[18][1] / len(cipher5)) * (alphabet[18][1] / len(cipher5))
ioc5T = (alphabet[19][1] / len(cipher5)) * (alphabet[19][1] / len(cipher5))
ioc5U = (alphabet[20][1] / len(cipher5)) * (alphabet[20][1] / len(cipher5))
ioc5V = (alphabet[21][1] / len(cipher5)) * (alphabet[21][1] / len(cipher5))
ioc5W = (alphabet[22][1] / len(cipher5)) * (alphabet[22][1] / len(cipher5))
ioc5X = (alphabet[23][1] / len(cipher5)) * (alphabet[23][1] / len(cipher5))
ioc5Y = (alphabet[24][1] / len(cipher5)) * (alphabet[24][1] / len(cipher5))
ioc5Z = (alphabet[25][1] / len(cipher5)) * (alphabet[25][1] / len(cipher5))
total5IOC = ioc5A + ioc5B + ioc5C + ioc5D + ioc5E + ioc5F + ioc5G + ioc5H + ioc5I + ioc5J + ioc5K + ioc5L + ioc5M + ioc5N + ioc5O + ioc5P + ioc5Q + ioc5R + ioc5S + ioc5T + ioc5U + ioc5V + ioc5W + ioc5X + ioc5Y + ioc5Z
print(total5IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher7)):
    for g in range(0, 26):
        if cipher7[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc7A = (alphabet[0][1] / len(cipher7)) * (alphabet[0][1] / len(cipher7))
ioc7B = (alphabet[1][1] / len(cipher7)) * (alphabet[1][1] / len(cipher7))
ioc7C = (alphabet[2][1] / len(cipher7)) * (alphabet[2][1] / len(cipher7))
ioc7D = (alphabet[3][1] / len(cipher7)) * (alphabet[3][1] / len(cipher7))
ioc7E = (alphabet[4][1] / len(cipher7)) * (alphabet[4][1] / len(cipher7))
ioc7F = (alphabet[5][1] / len(cipher7)) * (alphabet[5][1] / len(cipher7))
ioc7G = (alphabet[6][1] / len(cipher7)) * (alphabet[6][1] / len(cipher7))
ioc7H = (alphabet[7][1] / len(cipher7)) * (alphabet[7][1] / len(cipher7))
ioc7I = (alphabet[8][1] / len(cipher7)) * (alphabet[8][1] / len(cipher7))
ioc7J = (alphabet[9][1] / len(cipher7)) * (alphabet[9][1] / len(cipher7))
ioc7K = (alphabet[10][1] / len(cipher7)) * (alphabet[10][1] / len(cipher7))
ioc7L = (alphabet[11][1] / len(cipher7)) * (alphabet[11][1] / len(cipher7))
ioc7M = (alphabet[12][1] / len(cipher7)) * (alphabet[12][1] / len(cipher7))
ioc7N = (alphabet[13][1] / len(cipher7)) * (alphabet[13][1] / len(cipher7))
ioc7O = (alphabet[14][1] / len(cipher7)) * (alphabet[14][1] / len(cipher7))
ioc7P = (alphabet[15][1] / len(cipher7)) * (alphabet[15][1] / len(cipher7))
ioc7Q = (alphabet[16][1] / len(cipher7)) * (alphabet[16][1] / len(cipher7))
ioc7R = (alphabet[17][1] / len(cipher7)) * (alphabet[17][1] / len(cipher7))
ioc7S = (alphabet[18][1] / len(cipher7)) * (alphabet[18][1] / len(cipher7))
ioc7T = (alphabet[19][1] / len(cipher7)) * (alphabet[19][1] / len(cipher7))
ioc7U = (alphabet[20][1] / len(cipher7)) * (alphabet[20][1] / len(cipher7))
ioc7V = (alphabet[21][1] / len(cipher7)) * (alphabet[21][1] / len(cipher7))
ioc7W = (alphabet[22][1] / len(cipher7)) * (alphabet[22][1] / len(cipher7))
ioc7X = (alphabet[23][1] / len(cipher7)) * (alphabet[23][1] / len(cipher7))
ioc7Y = (alphabet[24][1] / len(cipher7)) * (alphabet[24][1] / len(cipher7))
ioc7Z = (alphabet[25][1] / len(cipher7)) * (alphabet[25][1] / len(cipher7))
total7IOC = ioc7A + ioc7B + ioc7C + ioc7D + ioc7E + ioc7F + ioc7G + ioc7H + ioc7I + ioc7J + ioc7K + ioc7L + ioc7M + ioc7N + ioc7O + ioc7P + ioc7Q + ioc7R + ioc7S + ioc7T + ioc7U + ioc7V + ioc7W + ioc7X + ioc7Y + ioc7Z
print(total7IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher8)):
    for g in range(0, 26):
        if cipher8[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc8A = (alphabet[0][1] / len(cipher8)) * (alphabet[0][1] / len(cipher8))
ioc8B = (alphabet[1][1] / len(cipher8)) * (alphabet[1][1] / len(cipher8))
ioc8C = (alphabet[2][1] / len(cipher8)) * (alphabet[2][1] / len(cipher8))
ioc8D = (alphabet[3][1] / len(cipher8)) * (alphabet[3][1] / len(cipher8))
ioc8E = (alphabet[4][1] / len(cipher8)) * (alphabet[4][1] / len(cipher8))
ioc8F = (alphabet[5][1] / len(cipher8)) * (alphabet[5][1] / len(cipher8))
ioc8G = (alphabet[6][1] / len(cipher8)) * (alphabet[6][1] / len(cipher8))
ioc8H = (alphabet[7][1] / len(cipher8)) * (alphabet[7][1] / len(cipher8))
ioc8I = (alphabet[8][1] / len(cipher8)) * (alphabet[8][1] / len(cipher8))
ioc8J = (alphabet[9][1] / len(cipher8)) * (alphabet[9][1] / len(cipher8))
ioc8K = (alphabet[10][1] / len(cipher8)) * (alphabet[10][1] / len(cipher8))
ioc8L = (alphabet[11][1] / len(cipher8)) * (alphabet[11][1] / len(cipher8))
ioc8M = (alphabet[12][1] / len(cipher8)) * (alphabet[12][1] / len(cipher8))
ioc8N = (alphabet[13][1] / len(cipher8)) * (alphabet[13][1] / len(cipher8))
ioc8O = (alphabet[14][1] / len(cipher8)) * (alphabet[14][1] / len(cipher8))
ioc8P = (alphabet[15][1] / len(cipher8)) * (alphabet[15][1] / len(cipher8))
ioc8Q = (alphabet[16][1] / len(cipher8)) * (alphabet[16][1] / len(cipher8))
ioc8R = (alphabet[17][1] / len(cipher8)) * (alphabet[17][1] / len(cipher8))
ioc8S = (alphabet[18][1] / len(cipher8)) * (alphabet[18][1] / len(cipher8))
ioc8T = (alphabet[19][1] / len(cipher8)) * (alphabet[19][1] / len(cipher8))
ioc8U = (alphabet[20][1] / len(cipher8)) * (alphabet[20][1] / len(cipher8))
ioc8V = (alphabet[21][1] / len(cipher8)) * (alphabet[21][1] / len(cipher8))
ioc8W = (alphabet[22][1] / len(cipher8)) * (alphabet[22][1] / len(cipher8))
ioc8X = (alphabet[23][1] / len(cipher8)) * (alphabet[23][1] / len(cipher8))
ioc8Y = (alphabet[24][1] / len(cipher8)) * (alphabet[24][1] / len(cipher8))
ioc8Z = (alphabet[25][1] / len(cipher8)) * (alphabet[25][1] / len(cipher8))
total8IOC = ioc8A + ioc8B + ioc8C + ioc8D + ioc8E + ioc8F + ioc8G + ioc8H + ioc8I + ioc8J + ioc8K + ioc8L + ioc8M + ioc8N + ioc8O + ioc8P + ioc8Q + ioc8R + ioc8S + ioc8T + ioc8U + ioc8V + ioc8W + ioc8X + ioc8Y + ioc8Z
print(total8IOC)

for y in range(0, 26):
    alphabet[y][1] = 0
for h in range(len(cipher9)):
    for g in range(0, 26):
        if cipher9[h].lower() == alphabet[g][0]:
            alphabet[g][1] = alphabet[g][1] + 1
print(alphabet)
ioc9A = (alphabet[0][1] / len(cipher9)) * (alphabet[0][1] / len(cipher9))
ioc9B = (alphabet[1][1] / len(cipher9)) * (alphabet[1][1] / len(cipher9))
ioc9C = (alphabet[2][1] / len(cipher9)) * (alphabet[2][1] / len(cipher9))
ioc9D = (alphabet[3][1] / len(cipher9)) * (alphabet[3][1] / len(cipher9))
ioc9E = (alphabet[4][1] / len(cipher9)) * (alphabet[4][1] / len(cipher9))
ioc9F = (alphabet[5][1] / len(cipher9)) * (alphabet[5][1] / len(cipher9))
ioc9G = (alphabet[6][1] / len(cipher9)) * (alphabet[6][1] / len(cipher9))
ioc9H = (alphabet[7][1] / len(cipher9)) * (alphabet[7][1] / len(cipher9))
ioc9I = (alphabet[8][1] / len(cipher9)) * (alphabet[8][1] / len(cipher9))
ioc9J = (alphabet[9][1] / len(cipher9)) * (alphabet[9][1] / len(cipher9))
ioc9K = (alphabet[10][1] / len(cipher9)) * (alphabet[10][1] / len(cipher9))
ioc9L = (alphabet[11][1] / len(cipher9)) * (alphabet[11][1] / len(cipher9))
ioc9M = (alphabet[12][1] / len(cipher9)) * (alphabet[12][1] / len(cipher9))
ioc9N = (alphabet[13][1] / len(cipher9)) * (alphabet[13][1] / len(cipher9))
ioc9O = (alphabet[14][1] / len(cipher9)) * (alphabet[14][1] / len(cipher9))
ioc9P = (alphabet[15][1] / len(cipher9)) * (alphabet[15][1] / len(cipher9))
ioc9Q = (alphabet[16][1] / len(cipher9)) * (alphabet[16][1] / len(cipher9))
ioc9R = (alphabet[17][1] / len(cipher9)) * (alphabet[17][1] / len(cipher9))
ioc9S = (alphabet[18][1] / len(cipher9)) * (alphabet[18][1] / len(cipher9))
ioc9T = (alphabet[19][1] / len(cipher9)) * (alphabet[19][1] / len(cipher9))
ioc9U = (alphabet[20][1] / len(cipher9)) * (alphabet[20][1] / len(cipher9))
ioc9V = (alphabet[21][1] / len(cipher9)) * (alphabet[21][1] / len(cipher9))
ioc9W = (alphabet[22][1] / len(cipher9)) * (alphabet[22][1] / len(cipher9))
ioc9X = (alphabet[23][1] / len(cipher9)) * (alphabet[23][1] / len(cipher9))
ioc9Y = (alphabet[24][1] / len(cipher9)) * (alphabet[24][1] / len(cipher9))
ioc9Z = (alphabet[25][1] / len(cipher9)) * (alphabet[25][1] / len(cipher9))
total9IOC = ioc9A + ioc9B + ioc9C + ioc9D + ioc9E + ioc9F + ioc9G + ioc9H + ioc9I + ioc9J + ioc9K + ioc9L + ioc9M + ioc9N + ioc9O + ioc9P + ioc9Q + ioc9R + ioc9S + ioc9T + ioc9U + ioc9V + ioc9W + ioc9X + ioc9Y + ioc9Z
print(total9IOC)
totalSubIOC = (total1IOC + total2IOC + total3IOC + total4IOC + total5IOC + total7IOC + total8IOC + total9IOC)/8
print(totalSubIOC)
#print(cipher1)
#print(cipher2)

