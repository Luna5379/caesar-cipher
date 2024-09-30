ciphertext = 'HHIZRKHHXHXCFWLWJHICYFPAXFHHZDVZLWJHREXLCGWPPXUWSKEEQTPWDSCAICHHZDHVPQNGAEUCNUAHVQJOVILWJHVZCELPLTLDNNNHRRPTQTAHXQEEUCGZLPRFWQQUGZWAVOWKGZCQKKZNYITMMMASMQWAPRPNIBHKLTRIYYQTTHHUWPLPTHWHKGVITGHAWOAWVDGZHALPJRQTVIOWZGICORHHZDBPBJGKEFJOFWXQLPLTRIFMSKAHWOMYWOBJVXPXTZLEJUEELELPHKBUWKBPYRLPUIORVPLQICQTRVQJHVLENAPTQIPDBZDKKMZRIMEWAOVZAHNACEWEPRLOREGKAHXQBYBJWAPRPNIBHKVPGTHAVINAUQYWAEHHZDWAREFJTHVZVIAHASCCWABUZGICORFJAHTIVMJNVOXBLETHFTLCKBIQRVWOEABOLDYWNAKWFWVMOUATBPXYNGAERRFXAMXQWOLDBOAHGIXMLPKDBYTTQTSKAELTUWMEWALTEMWHVZPTSKEEJNLAFTBQLDHVLPAPAHQCBOAHFGGYXCFWGSBUPXXHMABIVQEECTEEBZMGMSWOXBDDUWLPXRPTGUEATEEXPNHVLEKMDWHAHHUVNGNSAEKOTTLJMGBUBCJHTKNCBJJQVILDWNAMAHJOSKXBKDRRVIIMSSLELPACRRMWBUUGOUATJDMXASZRAMSGYRVJWAHVVCVQCAICUITTAHSGPNBCICPLHHPLSKUIVIUIVDHHDDMGHWKMWKYJSKPLIMLMNGPWDGGZNNTEHKLWEXLPHLTTTESSQTAHVMAWVMWOBJWHFKAWMGGVZHWAAIGZLPALIQGZBYBJKYQTVMVJIUNAMAYRLPVZTKCKLDHHDDCTEEBZKYBLHKBUICFRYWFJAHCAEMWHKOBJGZICJQHVXBWHMEEATEAPVWTBZGAHGIXMLPRRQTOSZAJOFWAWAWRRJDHZSWZDPNBOWOVJFQEFEEMXXQGYIMVJEMPLFWCUZURENSAHCACCGZSJEESAHVGZLPZQKGGZLPQIVJFQKRVQIMBPAGATUACQOPRKLPRERFYRLPBYVMKSWANARFHJICJBMUEMWHJDMXASATLPHLTKNCTTMGMGLWVIAHQCEEGZUGLSVQEEXOEEAHZKLOYWAHCAXKKGVJPIRUWEIXFTTXCNGOGZLPMEAHICNUPWDSCAICTBOSKSANMYBOYFRUMUDONAJPXQSSZNHVXPBPOGVCVMWOVJXFTZTHRRDKBUGIYPASFRSKZNYIVILQFWWWUXHVWAMUTZMAUUUVPTVXSDCAVIAHWOGXVIPYRUMQ'
digrams = ['' for z in range(len(ciphertext)//2)]
print(len(digrams))
plaintext = [' ' for z in range(len(ciphertext))]
for i in range(0, len(ciphertext), 2):
    digrams[i//2] = ciphertext[i] + ciphertext[i+1]
print(digrams)
for i in range(0, len(ciphertext), 2):
    if digrams[i//2] == 'HH':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'IZ':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'RK':
        plaintext[i] = 'y'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'XH':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'k'
    elif digrams[i//2] == 'XC':
        plaintext[i] = 's'
        plaintext[i + 1] = 'f'
    elif digrams[i//2] == 'FW':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'LW':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'JH':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'IC':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'YF':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'PA':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'XF':
        plaintext[i] = 'p'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'ZD':
        plaintext[i] = 'v'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'VZ':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'RE':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'XL':
        plaintext[i] = 'j'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'CG':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'WP':
        plaintext[i] = 'd'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'PX':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'UW':
        plaintext[i] = 's'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'SK':
        plaintext[i] = 'a'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'EE':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'QT':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'PW':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'DS':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'CA':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'HV':
        plaintext[i] = 't'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'NN':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'RR':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'PQ':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'MQ':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'RU':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'NG':
        plaintext[i] = 'u'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'VI':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'JO':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'f'
    elif digrams[i//2] == 'VQ':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'v'
    elif digrams[i//2] == 'AE':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'UC':
        plaintext[i] = 'm'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'NU':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'AH':
        plaintext[i] = 't'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'CE':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'LP':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'LT':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'LD':
        plaintext[i] = 't'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'NH':
        plaintext[i] = 't'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'PT':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'e'
##    elif digrams[i//2] == 'ME':
##        plaintext[i] = 'o'
##        plaintext[i + 1] = 'v'
    elif digrams[i//2] == 'WA':
        plaintext[i] = 's'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'XQ':
        plaintext[i] = 'e'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'GZ':
        plaintext[i] = 'n'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'RF':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'WQ':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'QU':
        plaintext[i] = 'm'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'VO':
        plaintext[i] = 'c'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'WK':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'CQ':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'KK':
        plaintext[i] = 'k'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'MM':
        plaintext[i] = 'm'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'AS':
        plaintext[i] = 'i'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'ZN':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'YI':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'k'
    elif digrams[i//2] == 'TM':
        plaintext[i] = 'a'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'PR':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'PN':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'IB':
        plaintext[i] = 'p'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'HK':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'RI':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'YY':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'FM':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'CC':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'LQ':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'f'
    elif digrams[i//2] == 'TH':
        plaintext[i] = 'f'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'HU':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'WH':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'KG':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'w'
    elif digrams[i//2] == 'TG':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'HA':
        plaintext[i] = 'o'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'WO':
        plaintext[i] = 'e'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'AW':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'w'
    elif digrams[i//2] == 'VD':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'JR':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'ME':
        plaintext[i] = 'u'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'OW':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'ZG':
        plaintext[i] = 's'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'OR':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'GX':
        plaintext[i] = 'p'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'PY':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'j'
    elif digrams[i//2] == 'WW':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'DD':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'TT':
        plaintext[i] = 't'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'UU':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'FJ':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'FX':
        plaintext[i] = 'n'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'AM':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'BU':
        plaintext[i] = 'i'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'MU':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'TZ':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'g'
    elif digrams[i//2] == 'MA':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'UV':
        plaintext[i] = 't'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'BI':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'YR':
        plaintext[i] = 'f'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'BJ':
        plaintext[i] = 't'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'VX':
        plaintext[i] = 't'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'BP':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'GK':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'EF':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'MY':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'm'
##    elif digrams[i//2] == 'LE':
##        plaintext[i] = 'i'
##        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'JU':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'EM':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'UX':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'RV':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'QJ':
        plaintext[i] = 'x'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'LE':
        plaintext[i] = 's'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'NA':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'QI':
        plaintext[i] = 'y'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'PD':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'BZ':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'VJ':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'UI':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'AO':
        plaintext[i] = 'm'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'VP':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'DK':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'SS':
        plaintext[i] = 's'
        plaintext[i + 1] = 'a'
    elif digrams[i//2] == 'KM':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'ZR':
        plaintext[i] = 'h'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'BY':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'x'
    elif digrams[i//2] == 'CT':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'IM':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'EW':
        plaintext[i] = 'm'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'GT':
        plaintext[i] = 't'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'WE':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'LO':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'ZQ':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'IQ':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'KB':
        plaintext[i] = 't'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'LC':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'FT':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'BO':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'AP':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'QC':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'KW':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'UQ':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'w'
    elif digrams[i//2] == 'YW':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'FR':
        plaintext[i] = 't'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'GI':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'YP':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'AL':
        plaintext[i] = 'p'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'DO':
        plaintext[i] = 's'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'JP':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'g'
    elif digrams[i//2] == 'XP':
        plaintext[i] = 'f'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'TI':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'VM':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'JN':
        plaintext[i] = 'f'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'XB':
        plaintext[i] = 't'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'KS':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'FK':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'f'
    elif digrams[i//2] == 'KD':
        plaintext[i] = 'r'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'JQ':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'XM':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'XR':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'EA':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'w'
    elif digrams[i//2] == 'OU':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'g'
    elif digrams[i//2] == 'AT':
        plaintext[i] = 'h'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'XY':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'FQ':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'KR':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'AG':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'g'
    elif digrams[i//2] == 'DW':
        plaintext[i] = 'k'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'MX':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'GY':
        plaintext[i] = 'o'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'JD':
        plaintext[i] = 'p'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'LA':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'BQ':
        plaintext[i] = 'm'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'FG':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'GS':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'MG':
        plaintext[i] = 's'
        plaintext[i + 1] = 'u'
    elif digrams[i//2] == 'MS':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'g'
    elif digrams[i//2] == 'GU':
        plaintext[i] = 's'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'TE':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'EX':
        plaintext[i] = 'l'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'NS':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'f'
    elif digrams[i//2] == 'SG':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'WN':
        plaintext[i] = 'f'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'PL':
        plaintext[i] = 't'
        plaintext[i + 1] = 'w'
    elif digrams[i//2] == 'HW':
        plaintext[i] = 's'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'BC':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'VC':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'YJ':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'LM':
        plaintext[i] = 'k'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'DG':
        plaintext[i] = 'a'
        plaintext[i + 1] = 'd'
    elif digrams[i//2] == 'KY':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'o'
    elif digrams[i//2] == 'IU':
        plaintext[i] = 'w'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'SD':
        plaintext[i] = 'h'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'BL':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'k'
    elif digrams[i//2] == 'VW':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'TB':
        plaintext[i] = 'l'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'KO':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'AC':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'c'
    elif digrams[i//2] == 'MW':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'k'
    elif digrams[i//2] == 'UG':
        plaintext[i] = 'i'
        plaintext[i + 1] = 'm'
    elif digrams[i//2] == 'CU':
        plaintext[i] = 'k'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'ZU':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'v'
    elif digrams[i//2] == 'SJ':
        plaintext[i] = 'b'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'SA':
        plaintext[i] = 'k'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'LJ':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'y'
    elif digrams[i//2] == 'TK':
        plaintext[i] = 'c'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'NC':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'CK':
        plaintext[i] = 'u'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'HL':
        plaintext[i] = 'd'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'OG':
        plaintext[i] = 'w'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'GV':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'ZH':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'AI':
        plaintext[i] = 's'
        plaintext[i + 1] = 'i'
    elif digrams[i//2] == 'HZ':
        plaintext[i] = 'p'
        plaintext[i + 1] = 's'
    elif digrams[i//2] == 'SW':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'OS':
        plaintext[i] = 'k'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'ZA':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'b'
##    elif digrams[i//2] == 'UA':
##        plaintext[i] = 'o'
##        plaintext[i + 1] = 'l'
##    elif digrams[i//2] == 'OP':
##        plaintext[i] = 'k'
##        plaintext[i + 1] = 'b'
    elif digrams[i//2] == 'LS':
        plaintext[i] = 'e'
        plaintext[i + 1] = 'h'
    elif digrams[i//2] == 'XO':
        plaintext[i] = 'g'
        plaintext[i + 1] = 'r'
    elif digrams[i//2] == 'ZK':
        plaintext[i] = 'o'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'AN':
        plaintext[i] = 'n'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'PI':
        plaintext[i] = 'w'
        plaintext[i + 1] = 't'
    elif digrams[i//2] == 'XK':
        plaintext[i] = 'k'
        plaintext[i + 1] = 'n'
    elif digrams[i//2] == 'IX':
        plaintext[i] = 't'
        plaintext[i + 1] = 'p'
    elif digrams[i//2] == 'TX':
        plaintext[i] = 'p'
        plaintext[i + 1] = 'e'
    elif digrams[i//2] == 'CN':
        plaintext[i] = 'r'
        plaintext[i + 1] = 'l'
    elif digrams[i//2] == 'GO':
        plaintext[i] = 'y'
        plaintext[i + 1] = 'i'

    else:
        plaintext[i] = digrams[i//2][0]
        plaintext[i + 1] = digrams[i//2][1]
for i in range(len(plaintext)):
    print(plaintext[i], end= '')
