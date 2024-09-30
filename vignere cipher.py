text = 'SIJKJBZTYSKYZZLAPNAEPAQHFAWGEUWPPPSOPIENNPTXEBWKAQUMFZWHQEZTEPSIAMFXOJMMTIELEQDEYWLOPZQVWMSKHPQTYLATXVGMPVLBCMDRDCJXTSFHHEZHTVLAPPGNDMZHWLOTDQFOZTNXOUSBDQWPLAUEPIJEJDWKJIFQTWMLLJGNEBZXWQTKLZQMSMSMEIUAPLWQEZSVENJHXPWKDXWEWAGNEPWKOMWILBLTNPEXYBLHTBEHCMGOPZLAPMXYZZLTYLEHYMQLSMKIPVLMCGAGRBGXDBSUWQKAPDAWPVUXNWFGPKLBYOLAPPGNDMZHWLLHEPWTEBWFABWWEPWYEAZHHAZHHQEIZZLTYBAMHIKMZPWKTAAMAWKLTJDXEPSMTBOTDVLKZOWKDEZHZZYTYQKXOBZXEPWYEKGNWLKHXMGGPQFMSMETYWJALDWALLSZCCVZPIYTTVKMXIALTMKMPIDBYOXKZULAPTAUCIJRDMWFDTADPIYHZLAYNWFOZTMMPLOTJBGZPBSMSMJBHWMEOTADPBGKPIVFZZWHQUSBDQWLEPGNRPLLMCLLSMOTDDWKJKSKPNMESMJWTIJRAIYXDEWKPMFVCGHMPLOBEPSAZALHQLAYQMJXYBUBAPWKDIFWLALBXMOXYBGGDPWTOIHMPLSGOALKPVYMSMFXOBZXXBZBDWFXWWGDDPSKOJMMTBALCMSEWGHKPBLRPIKREPWELBWKZVWLRMLTWWLMZCYAPZSGJESRHMFXPLLHATSGZCJGPFLLEMHLNWMEOGGNEZQMZOWMLTALEWXMSMEXXJWKDWXKZOWKDPGNDMZHWLSGOUSDPMFJFQJBPASUZCLMSMEBEEGNWLTXRWGWEWCGZEAYEPWKPESLLVQHYMOAZPSWLZWTDWFMZLALWQCXXIALTMOXDPGNWLFHELALNWMGEUSBDQWLEPWHCGLALBLAPBZXQBOTDXSKEWXTYQFLFZSGNMKVLUWBEPWKMCLBQQFWTBZTCLLHMMDBPDWMSILKZOWKDEGNWLZTGMJBDSWWSQKKPXMMLBAHYIFWSQKVSIFVPWXMSMYHGMJGZZKATXWOPVAYSMOTDAZHCBGYXWFXJXWHATWETSWATUUHFTVNDCSEWGXBYLKHXMGGPBGULKCMSMEBWWGDQWJPLZVMZPWTCQFZQZGFJWMCZLAXAAOALBSKPGGNCMSWTVYKTOZM'
ciphertext=['' for j in range(len(text))]
plaintext=['' for k in range(len(text))]
key = [11, 8, 18, 19]
##def tabula_recta(text, key, decipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
##    if decipher == True:
##        numericalCiphertext = ord(text)
##        numericalKey = ord(key)
##        numericalPlaintext = (numericalCiphertext - numericalKey) % 26
##        plaintext = chr(numericalPlaintext)
##        return plaintext
##print(ord("A"))
##
##print(tabula_recta(text, key, decipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
for i in range(len(text)):
    ciphertext[i] = ord(text[i])
print(ciphertext)
for h in range(0, len(text), 4):
    if ciphertext[h] - key[0] < 65:
        ciphertext[h] -= key[0]
        ciphertext[h] += 26
        if ciphertext[h + 1] - key[1] < 65:
            ciphertext[h + 1] -= key[1]
            ciphertext[h + 1] += 26
            if ciphertext[h + 2] - key[2] < 65:
                ciphertext[h + 2] -= key[2]
                ciphertext[h + 2] += 26
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]   
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
            else:
                ciphertext[h + 2] -= key[2]
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                        if ciphertext[h + 9] - key[9] <65:
##                                            ciphertext[h + 9] -= key[9]
##                                            ciphertext[h + 9] +=26
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                        else:
##                                            ciphertext[h + 9] -= key[9]
##                                            if ciphertext[h + 10] - key[10] <65:
##                                                ciphertext[h + 10] -= key[10]
##                                                ciphertext[h + 10] +=26
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                            else:
##                                                ciphertext[h + 10] -= key[10]
##                                                if ciphertext[h + 11] - key[11] <65:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    ciphertext[h + 11] +=26
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                                                else:
##                                                    ciphertext[h + 11] -= key[11]
##                                                    if ciphertext[h + 12] - key[12] <65:
##                                                        ciphertext[h + 12] -= key[12]
##                                                        ciphertext[h + 12] +=26
##                                                    else:
##                                                        ciphertext[h + 12] -= key[12]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
        else:
            ciphertext[h + 1] -= key[1]
            if ciphertext[h + 2] - key[2] < 65:
                ciphertext[h + 2] -= key[2]
                ciphertext[h + 2] += 26
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
            else:
                ciphertext[h + 2] -= key[2]
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
    else:
        ciphertext[h] -= key[0]
        if ciphertext[h + 1] - key[1] < 65:
            ciphertext[h + 1] -= key[1]
            ciphertext[h + 1] += 26
            if ciphertext[h + 2] - key[2] < 65:
                ciphertext[h + 2] -= key[2]
                ciphertext[h + 2] += 26
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
            else:
                ciphertext[h + 2] -= key[2]
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
        else:
            ciphertext[h + 1] -= key[1]
            if ciphertext[h + 2] - key[2] < 65:
                ciphertext[h + 2] -= key[2]
                ciphertext[h + 2] += 26
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
            else:
                ciphertext[h + 2] -= key[2]
                if ciphertext[h + 3] - key[3] < 65:
                    ciphertext[h + 3] -= key[3]
                    ciphertext[h + 3] += 26
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
                else:
                    ciphertext[h + 3] -= key[3]
##                    if ciphertext[h + 4] - key[4] < 65:
##                        ciphertext[h + 4] -= key[4]
##                        ciphertext[h + 4] += 26
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                    else:
##                        ciphertext[h + 4] -= key[4]
##                        if ciphertext[h + 5] - key[5] <65:
##                            ciphertext[h + 5] -= key[5]
##                            ciphertext[h + 5] +=26
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                        else:
##                            ciphertext[h + 5] -= key[5]
##                            if ciphertext[h + 6] - key[6] <65:
##                                ciphertext[h + 6] -= key[6]
##                                ciphertext[h + 6] +=26
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                            else:
##                                ciphertext[h + 6] -= key[6]
##                                if ciphertext[h + 7] - key[7] <65:
##                                    ciphertext[h + 7] -= key[7]
##                                    ciphertext[h + 7] +=26
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
##                                else:
##                                    ciphertext[h + 7] -= key[7]
##                                    if ciphertext[h + 8] - key[8] <65:
##                                        ciphertext[h + 8] -= key[8]
##                                        ciphertext[h + 8] +=26
##                                    else:
##                                        ciphertext[h + 8] -= key[8]
for g in range(len(text)):
    plaintext[g] = chr(ciphertext[g])
for o in range(len(plaintext)):
    print(plaintext[o], end='')
