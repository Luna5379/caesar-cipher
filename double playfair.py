import math
ciphertext = 'ENEAOTAQKDUQXNIIVBQZRAXNIILOQAXTMNQAUWOHCPGHICAQSCOGYHGNTTWUHPAPARHHKMNNMGPPMLQAGHVQUPILOPSPLAUPWQKGGRFAVBEDRLRAIBAQAIDNRFQDDNUFUMOBAQUVIKEEHHMNQAENEAQONTOVKGSBIHQPENXATUMCOPKZTAOTKPKHPOWHETVBYTWMSLIDSBFADSMDYTBPXTGMSQXNAWFAVBEDRLRASPPBGHFNPFQPXOXTLAMXAQLKNDZPILNWAQSLGKOHVBMIPPTAQAKPYTVGMXAQQUHHXNQOKHQOPNEKXAKZNTQVNLHHEMUHYHGNTTWUHPQUQELSIDSBSGTIIHQPETAKWHNLWMCYVBKPKPWYSLWGDSWUFAWTWHSBVOTLENKZNYWFPYHPNIIDWHSHNAXNVBILNHRSSOKHQOQPLASZWWQEAMAKZPAIHHSBOZKZQFKKLACFXYDTFASNPHSQOBSQLAWMNNMOWCXTWGRTNBVBAQAKIQXNSBWBPHWGKKLAGMMLTNRTWYMANAWQKGVMWHXASQKGXAKERAQRSFVIMWNHUIIQWZENSUWZENIDSPRBQGCMFAWPLAZWAQAIHHSQPNAKMCOPHPMDQKFAUHSKXNVMBYFHAIUMOBAQTGLBSLVBEIWFEAVONBEMFHSBOZVBILNHRSSOKHQZVBHHKCUWIKMDYTBPAEADSQPBGHIDSPFAVBIIMXAQUPTIYNRIXTSZSKSLVBSQXTIKUQIQIIUPVQXNSPRPWZADXOXTVBILKPZWRPQSFADSMAXTMBOPVBAIEMWBSHQGUNMILNDSVBSKVBSXCFTIIBMRMINWSLVBAIIKKNNNQAHNRPQSQGTNNDOWVBAIWHETXTQFDSMBWFQMLAGPKGRTHHVBAIIDOPPHEAGPMLQEXASPFAVBAXRPQSQGUNSLHPXOSSSLKNILKNSLHHELENSPNNSOBYFHSCFAMNUGMDNEVIIPMRSLGKOHQULTRAWFVQTANSWUKPYTVGOWLAXTRAAKIIRPHYWHNBLSWMONWXVBAXKGRSSGNDILWBPHGKOHOMWFLTVMEMWBUWIKXOFEHNLNQOWHEMCPLAXATUHNIQNBEDWYQOAQBYOWIKOQEIAKSLWHLARDRTWHLTVBAQDTOQQNVLSLMAXTLKPSRHLNWGHKOHSIKKLAQFWOYSRKASRSKPAIWZOGYHGNTTWUHHXNQAHHKMOPEINSEAVBSIWYKYNAPKMLIZYTTZNSDTSBPOOHAXSRVBSKVZOWSLKPSGTIIHQPFADSETIIVBSIWYKYNAOROPFLQAKBQOIIENSPOPMXMLQKKZWOOHUMOBAQVZRHHHKMFAVBAXRPQSVBIILSMIONQELTSPOWKPKATTBYHPNBLSWMQPLASZWWTTVBAQVBIDFSEAVBAQHPKQFAWPLAKDUYAQLNUVRPQSETSBVANWAQSLLAFAANNNWOSLNBVBMXMDXLIDMPTLQEWWNBVBALQHHQIDSBETQEMXSLVBSKVBEIQPIIWBMDQDVONBFSEACFTIANSQQHRMIZWHETAKVIKDWMVISKMIZHDHWYQOAQQYXOQAAQWOQHAHCBQOIIWBPHTAQANBLSXTSPLAKDUYAQLNWOPBHPSGQOISWBRAOZNSQABYPBALMILNDSAWRPQSNBLSWMLAETWOOQHNMCOPVBILRHLNWZFAIHQBENSKFAVBICSSSHRAWGQGWMFAVBICSSAKTTOZSLKDXFQHUFWYTGIQWHCEWZWPLAQEAMAKCPPPELKDVYGHXANEVBMQTLQEWWNBVBAXOPHQVBSLMLVBYTTAIAKNIITNQKKGUCKZMFADAIBPMIFEOPKPFBHBSSQGXNOTAKLLSHOGBPIZAIAIWYTGIQCFTIIPWBNDETMDFWSCKDVIIBHPSFSWSKVBMCQHWHKKLANSSNAQMGWQIZHHKFRANBRPUTIQTBOPLTWYIQVBACNHANUCIDSBOFSLFNXNQRXTMDHPSLVBSKGWIKHHXAWYRPWAIDLTWMLAQIQEEAQYHYUWMIPKIISPLASFRBKDTTNAQRWZTAQAVBMCOPLTWUFAANELQAIQGBRASPONSLSQILTNMFSCYTTASFWQWHXTQFDSKPBYIIVBICRPXALLEIAQIIXNXTMNQAXASCOZVBALQNYHSQRPTNVAXTADVBSKCFLLMXAQCHRAHHVBELIKUWHHKYUWIKWHOPHPKXWHTNLLVBALQHKIPAIQLAFAIPELQZWPLAXTIDSPLAXTYTVGQHRIOPXPQZWWWHXTNIISSCWPOHBPUQOQHPMLQAHHKPFNOKMILNKKLAQIQEEAXKHNFIDNWOASQEVZSLVBSKVBSLMLVBYTTANAIAKNIITNQAWZPAIIQPKZOZFAMNRIAKIITHZNELPOWHRSQGWTADAESLEDAKTBWFQMLAAMRBIIQEAMAKYHSSENWFHSRPVMSQLACNWFRISLVBSCNVIQWBFTWBPHQULSAKNBSBVANWAQZWIKMDRSCESKSLEMVHOWKPSBIHQPXAAICYXAWHXTDSMDVBMCISWPFAWPLASFRBYTTAKDUYAQCPQNPPOWRPQSRHIIIDHHDSWOGBSKKHQOFAUHGBKOQERZVBSCQOXMENWMOHMXFNQUOQHHXNTYWYIIMNQAWGLHXTNLXTMNNAQKAQNAWBDSWOTTXNKUGWRPQSUPCPRPQAAQQYRAOMWFLTVMMARFSEHFKDUYNWAQQGUTBPUCLTWOHHKMFAVBAIGBKOFADSETIIHHCDNRSLWGRTKGCYQOLAENSKKZOQEIAKSLIDQPSQFAVPELRTSPQBRFQEMAXNKZNTQAKZSBWBQOLASYQAHHKFKKLASFRBAKTTOZHHFYOPKPWHETSBVANWAQSLHNAKMCTIQROQEIAKSLSKTTFHNBMXKNIIEAQERZHHGFUMOBAQWOQPLASFRBXANDAQVZRHHHKMFAWPKZUVRPQSMAWOIIRPHYVZSSOWNWAQKZUOEIWQSKKHQOFAVBAXRPQSLSMIONQELTSPPPTNQASHBFGKOHVBELRSSOKHNAKKAQRMIZRLVMTLSBOZIDSBRMWOSSQYVBHHWBOZVBSKGHGBKOETKDVTSLWHRQMFHPKOLAMXKNIIEAFBLASBIHQPAEXTAIUMOBAQTAVOIIXNSPOWKPKATTBYHPNBLSTTQAWHNTHHTNHHVBILNHRSSOKHNAWPLANTQGWYSBIHQPVBHHKCCFTIENDSUTILEDASRSNBXOIZISVPIDSWSQLAXTFNNTKDUYAQSGPOQCTTSZWOIDANNSEZNTFHAQEMVHQPADUQENXTTTQAWGWHQUQEAMAKCBFADSQDDSSBTNQAMAXTMBOPKPKDWMKZWMCWMLVMIDSBFADSVBRPHYVBAKMNSFWQKGCYSGTIENPOUQSCVPLKXPXTQYVOYTVFSLRNVGQPQDDSKPIKKNNNQAIKVBMIGNTTWYIDTTVBAQVBIDVBMIACMDOWRAWYFASHNGCHRAYTCPRHWFXNSOKPHBMRIQRLQOVBMIIKVPHWDNAKVOQDYFZPEINSSZOZMLIZIDENDSWUSFRBHHVBILNHRSSOKHOVKPFAKDUYAQCPLAOPGBHHMDWZLLEIHHASQHKLEIPPKPOPCBQOLASZWWCYVBIKNTNDROOTAQNBQUFSCDUQKPAXOPHQPHIEKNENPOLANEETKZQAVBAXQHEHIDMIQEOZHHQUWFOHUVFAXNDSUFHPUVAKRAENSZENWOQNOWKPKOLASFRBWZPZAQQEAMAKZWLAQZADKFRAQUQEAMAKZWFHOKAISEPZKNENQZVPSGNDILWBPHHHTNSOHHQUCYNDHBMRAISSMLUMIDLTRTQOTZOPVBALQHHQWHETLKNDZPEQQZXNSBQOLAENQIWZWHWUIDMNKKAQIKWCTNMFSCQOAQYSQSMCHHSLSUVBIQTNXPXNNBQEQYTNWBPHWOONIQNHSPLAYNXTWHRHXTSZRPWONHPNFLYTYBOPMXAQIDMBAKWHNWMDTLMFSQOPSQUQQONNFSQYQRVBSKSHIQQGTWMDXLVBAIVBAQSCTANTXYSQKDWMLANTQAVBILNHRSSOOPUVKGCEMCOPVBAICYNDSKRSIKVBMRSLAIPHWOTTXNIBOWRMIZVBSXMAXTKDVMVLFANTHFFBHNIIVNNHRSSOKHQOLAOQPNELIPVZRPQSETXOIMTNQOFNNSQAHBMRACFWIIHHWOXMSOKHPOVBSKQFRABPKGTIANEQXASPRNWOASQEVZSKXMWOLKQAENSBMAXNSPQPLASLVLSKKHQGFDGNTTWYIDWOMLIZAQTAQASFRBSYQAAQUVILIDQGVNPHUPNHVBMCWQUQALWQDTMANATHMLWOUPCPPPFARLKP'
##ciphertext = 'TW'
PERIOD = int(input("period:"))
grid1 = [['A', 'B', 'C', 'D', 'E',], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
grid2 = [['M', 'U', 'R', 'D', 'E'], ['A', 'B', 'C', 'F', 'G'], ['H', 'I', 'K', 'L', 'N'], ['O', 'P', 'Q', 'S', 'T'], ['V', 'W', 'X', 'Y', 'Z']]
digrams = ['' for z in range(len(ciphertext)//2)]
period0 = ['' for z in range(len(ciphertext))]
print(len(digrams))
for i in range(0, len(ciphertext), 2):
    digrams[i//2] = ciphertext[i] + ciphertext[i+1]
print(digrams)
def gridCheck(grid1, grid2, letter1, letter2):
##    print(letter1)
##    print(letter2)
    for i in range(5):
        for j in range(5):
            if letter1 == grid2[i][j]:
                Row1 = i
                Column1 = j
##                print(Row1)
##                print(Column1)
    for i in range(5):
        for j in range(5):
            if letter2 == grid1[i][j]:
                Row2 = i
                Column2 = j
##                print(Row2)
##                print(Column2)
    return Row1, Row2, Column1, Column2
plaintext = ['' for j in range(len(ciphertext))]
print(len(plaintext))
for index in range(0, len(plaintext), 2):
    width = len(grid1)
    row1, row2, column1, column2 = gridCheck(grid1, grid2, digrams[index//2][0].upper(), digrams[index//2][1].upper())
    if row1 == row2:
        plaintext[index] = grid2[row1][(column1 + 1) % width]
        plaintext[index + 1] = grid1[row2][(column2 + 1) % width]
        row3, row4, column3, column4 = gridCheck(grid1, grid2, plaintext[index + 1].upper(), plaintext[index].upper())
        if row3 == row4:
            plaintext[index] = grid1[row4][(column4 + 1) % width]
            plaintext[index + 1] = grid2[row3][(column3 + 1) % width]
        else:
            plaintext[index] = grid1[row3][column4]
            plaintext[index + 1] = grid2[row4][column3]
    else:
        plaintext[index + 1] = grid1[row1][column2]
        plaintext[index] = grid2[row2][column1]
        row3, row4, column3, column4 = gridCheck(grid1, grid2, plaintext[index + 1].upper(), plaintext[index].upper())
        if row3 == row4:
            plaintext[index] = grid1[row4][(column4 + 1) % width]
            plaintext[index + 1] = grid2[row3][(column3 + 1) % width]
        else:
            plaintext[index + 1] = grid2[row4][column3]
            plaintext[index] = grid1[row3][column4]
for i in range(0, (len(plaintext) - PERIOD), PERIOD*2):
    period0[i] = plaintext[i]
    period0[i + 1] = plaintext[i + 2]
    period0[i + 2] = plaintext[i + 4]
    period0[i + 3] = plaintext[i + 6]
    period0[i + 4] = plaintext[i + 1]
    period0[i + 5] = plaintext[i + 3]
    period0[i + 6] = plaintext[i + 5]
    period0[i + 7] = plaintext[i + 7]
##for i in range(len(period0)):
##    print(plaintext[i], end='')
##print("")
for i in range(len(period0)):
    print(period0[i], end='')
            
    
##for index in range(0, len(digrams)*2, 2):
##    width = len(grid1)
##    row1, row2, column1, column2 = gridCheck(grid1, grid2, digrams[index//2][0].upper(), digrams[index//2][1].upper())
##    if column1 == column2:
##        plaintext[index] = grid2[(row1 + 1) % width][column1]
##        plaintext[index + 1] = grid1[(row2 + 1) % width][column2]
##        row3, row4, column3, column4 = gridCheck(grid1, grid2, plaintext[index].upper(), plaintext[index + 1].upper())
##        if column3 == column4:
##            plaintext[index+1] = grid2[(row3 + 1) % width][column3]
##            plaintext[index] = grid1[(row4 + 1) % width][column4]
##        elif row3 == row4:
##            plaintext[index + 1] = grid2[row3][(column3 + 1) % width]
##            plaintext[index] = grid1[row4][(column4 + 1) % width]
##        else:
##            plaintext[index + 1] = grid1[row3][column4]
##            plaintext[index] = grid2[row4][column3]
##    elif row1 == row2:
##        plaintext[index] = grid2[row1][(column1 + 1) % width]
##        plaintext[index + 1] = grid1[row2][(column2 + 1) % width]
##        row3, row4, column3, column4 = gridCheck(grid1, grid2, plaintext[index].upper(), plaintext[index + 1].upper())
##        if column3 == column4:
##            plaintext[index + 1] = grid2[(row3 + 1) % width][column3]
##            plaintext[index] = grid1[(row4 + 1) % width][column4]
##        elif row3 == row4:
##            plaintext[index + 1] = grid2[row3][(column3 + 1) % width]
##            plaintext[index] = grid1[row4][(column4 + 1) % width]
##        else:
##            plaintext[index + 1] = grid1[row3][column4]
##            plaintext[index] = grid2[row4][column3]
##    else:
##        plaintext[index] = grid1[row1][column2]
##        plaintext[index + 1] = grid2[row2][column1]
##        row3, row4, column3, column4 = gridCheck(grid1, grid2, plaintext[index].upper(), plaintext[index + 1].upper())
##        if column3 == column4:
##            plaintext[index + 1] = grid2[(row3 + 1) % width][column3]
##            plaintext[index] = grid1[(row4 + 1) % width][column4]
##        elif row3 == row4:
##            plaintext[index + 1] = grid1[row3][(column3 + 1) % width]
##            plaintext[index] = grid2[row4][(column4 + 1) % width]
##        else:
##            plaintext[index + 1] = grid1[row3][column4]
##            plaintext[index] = grid2[row4][column3]
##for i in range(len(plaintext)):
##    print(plaintext[i], end = '')
##
##
##
