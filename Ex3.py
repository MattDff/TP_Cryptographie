import numpy as np

message = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCML IKWVCQUIQW GRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMY JIMIJUHSFLM NSHKEVMR JNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCM EIFKEGM KIPJIT JJEIGTOCJ ZBLVELWXRJQIVSXVGRLI UVLHXOOJECZMEMKXHFERBSRPAINYMM EWQOVLINDENBAUHAXE NWPVUMTILMBFW VWMW ZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINB VI IAKEVWVRUISGKXREI AMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEW PA KJCCLENIDCFW HEUSRQW HETSTNLMEVUI SWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJIS XGYE USNBARHWV DIFWPWXTMNSVWFRINSRFGOZW"
# Nettoyage du texte
message = "".join([c for c in message.upper() if c.isalpha()])


# Question 3.1
def IC(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c,0) + 1
    N = len(text)
    if N < 2:
        return 0
    ic = sum(f*(f-1) for f in freq.values()) / (N*(N-1))
    return ic

'''
test = IC(message)
print(test)
'''

# Question 3.2
def k_seq(text,k):
    list_kIC = []
    list_seq = []
    count_modulo = 0

    for loop in range(k):
        list_seq.append("")

    for i in text:
        list_seq[count_modulo] = list_seq[count_modulo] + i
        count_modulo = (count_modulo + 1) % k

    for i in list_seq:
        list_kIC.append(IC(i))

    return list_kIC


for k in range(1,100):
    a =(np.mean(k_seq(message,k)))
    if a > 0.0768 and a < 0.0798 :
        print(a,k)