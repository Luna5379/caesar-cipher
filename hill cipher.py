ciphertext = "HHIZRKHHXHXCFWLWJHICYFPAXFHHZDVZLWJHREXLCGWPPXUWSKEEQTPWDSCAICHHZDHVPQNGAEUCNUAHVQJOVILWJHVZCELPLTLDNNNHRRPTQTAHXQEEUCGZLPRFWQQUGZWAVOWKGZCQKKZNYITMMMASMQWAPRPNIBHKLTRIYYQTTHHUWPLPTHWHKGVITGHAWOAWVDGZHALPJRQTVIOWZGICORHHZDBPBJGKEFJOFWXQLPLTRIFMSKAHWOMYWOBJVXPXTZLEJUEELELPHKBUWKBPYRLPUIORVPLQICQTRVQJHVLENAPTQIPDBZDKKMZRIMEWAOVZAHNACEWEPRLOREGKAHXQBYBJWAPRPNIBHKVPGTHAVINAUQYWAEHHZDWAREFJTHVZVIAHASCCWABUZGICORFJAHTIVMJNVOXBLETHFTLCKBIQRVWOEABOLDYWNAKWFWVMOUATBPXYNGAERRFXAMXQWOLDBOAHGIXMLPKDBYTTQTSKAELTUWMEWALTEMWHVZPTSKEEJNLAFTBQLDHVLPAPAHQCBOAHFGGYXCFWGSBUPXXHMABIVQEECTEEBZMGMSWOXBDDUWLPXRPTGUEATEEXPNHVLEKMDWHAHHUVNGNSAEKOTTLJMGBUBCJHTKNCBJJQVILDWNAMAHJOSKXBKDRRVIIMSSLELPACRRMWBUUGOUATJDMXASZRAMSGYRVJWAHVVCVQCAICUITTAHSGPNBCICPLHHPLSKUIVIUIVDHHDDMGHWKMWKYJSKPLIMLMNGPWDGGZNNTEHKLWEXLPHLTTTESSQTAHVMAWVMWOBJWHFKAWMGGVZHWAAIGZLPALIQGZBYBJKYQTVMVJIUNAMAYRLPVZTKCKLDHHDDCTEEBZKYBLHKBUICFRYWFJAHCAEMWHKOBJGZICJQHVXBWHMEEATEAPVWTBZGAHGIXMLPRRQTOSZAJOFWAWAWRRJDHZSWZDPNBOWOVJFQEFEEMXXQGYIMVJEMPLFWCUZURENSAHCACCGZSJEESAHVGZLPZQKGGZLPQIVJFQKRVQIMBPAGATUACQOPRKLPRERFYRLPBYVMKSWANARFHJICJBMUEMWHJDMXASATLPHLTKNCTTMGMGLWVIAHQCEEGZUGLSVQEEXOEEAHZKLOYWAHCAXKKGVJPIRUWEIXFTTXCNGOGZLPMEAHICNUPWDSCAICTBOSKSANMYBOYFRUMUDONAJPXQSSZNHVXPBPOGVCVMWOVJXFTZTHRRDKBUGIYPASFRSKZNYIVILQFWWWUXHVWAMUTZMAUUUVPTVXSDCAVIAHWOGXVIPYRUMQ"

##for i in range(0, len(ciphertext), 2):
##    ct1 = ord(ciphertext[i]) - 65
##    ct2 = ord(ciphertext[i + 1]) - 65
##    plain1 = chr(65 + (26 + ct1 - ct2) % 26)
##    plain2 = chr(65 + ct2)
##    print(plain1, end="")
##    print(plain2, end="")

##matrix = [[1, 1], [1, 2]]
for i in range(0, len(ciphertext), 2):
    ct1 = (ord(ciphertext[i]) - 65) + 26
    ct2 = (ord(ciphertext[i + 1]) - 65) + 26
    pt2 = ct2 - ct1
    pt1 = ct1 - pt2
    plain1 = chr(65 + (pt1 % 26))
    plain2 = chr(65 + (pt2 % 26))
    print(plain1, end="")
    print(plain2, end="")
