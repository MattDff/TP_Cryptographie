import numpy as np
import matplotlib.pyplot as plt
import string
from random import randint

message = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCML IKWVCQUIQW GRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMY JIMIJUHSFLM NSHKEVMR JNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCM EIFKEGM KIPJIT JJEIGTOCJ ZBLVELWXRJQIVSXVGRLI UVLHXOOJECZMEMKXHFERBSRPAINYMM EWQOVLINDENBAUHAXE NWPVUMTILMBFW VWMW ZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINB VI IAKEVWVRUISGKXREI AMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEW PA KJCCLENIDCFW HEUSRQW HETSTNLMEVUI SWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJIS XGYE USNBARHWV DIFWPWXTMNSVWFRINSRFGOZW"
# Nettoyage du texte
message_clean = "".join([c for c in message.upper() if c.isalpha()])


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


test = IC(message)
print(test)


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


for k in range(1,30):
    a =(np.mean(k_seq(message,k)))
    if a > 0.06 :
        print(a,k)

# Question 3.3
k = 7
list_sept_seq = []
count_modulo = 0

for loop in range(k):
    list_sept_seq.append("")

for i in message:
    list_sept_seq[count_modulo] = list_sept_seq[count_modulo] + i
    count_modulo = (count_modulo + 1) % k

def analyse(seq):
    freq = {}
    for c in seq:
        freq[c] = freq.get(c,0) + 1
    return freq

list_freq = []
for i in list_sept_seq:
    list_freq.append(analyse(i))

freq_fr = {
    'A': 9.42/100, 'B': 1.02/100, 'C': 2.64/100, 'D': 3.39/100, 'E': 15.87/100,
    'F': 0.95/100, 'G': 1.04/100, 'H': 0.77/100, 'I': 8.41/100, 'J': 0.89/100,
    'K': 0.0,    'L': 5.34/100, 'M': 3.24/100, 'N': 7.15/100, 'O': 5.14/100,
    'P': 2.86/100, 'Q': 1.06/100, 'R': 6.46/100, 'S': 7.90/100, 'T': 7.26/100,
    'U': 6.24/100, 'V': 2.15/100, 'W': 0.0,    'X': 0.30/100, 'Y': 0.24/100,
    'Z': 0.32/100
}

# Normalisation des fréquences françaises
total_fr = sum(freq_fr.values())
freq_fr_norm = {k:v/total_fr for k,v in freq_fr.items()}

k = 7
subseqs = [""]*k
for idx, c in enumerate(message_clean):
    subseqs[idx % k] += c

# Fonction pour calculer la fréquence normalisée d'une sous-séquence
def analyse(seq):
    freq = {c:0 for c in string.ascii_uppercase}
    for c in seq:
        if c in freq:
            freq[c] += 1
    total = sum(freq.values())
    if total == 0:
        return freq
    return {c: freq[c]/total for c in string.ascii_uppercase}

# Calcul des fréquences
list_freq = [analyse(seq) for seq in subseqs]

'''
for i in range(7):
    freq_first_seq = analyse(subseqs[i])
    lab = str(i+1) + "ème Séquence"

    # Plot des fréquences
    letters = list(string.ascii_uppercase)
    x = range(len(letters))

    plt.figure(figsize=(15,6))
    plt.bar(x, [freq_first_seq[c] for c in letters], color='skyblue', label=lab)
    plt.plot(x, [freq_fr[c] for c in letters], color='red', marker='o', linestyle='-', linewidth=2, label="Français")
    plt.xticks(x, letters)
    plt.xlabel("Lettres")
    plt.ylabel("Fréquence")
    plt.title("Fréquences des lettres : première sous-séquence vs Français")
    plt.legend()
    plt.show()
'''

def decode(message, key):
    decrypted =""
    key_len = len(key)
    i = 0
    for c in message:
        m = ord(c) - ord('A')
        k = ord(key[i % key_len]) - ord('A')
        decrypted = decrypted + chr((m - k) % 26 + ord('A'))
        i = i + 1
    return decrypted

print(decode(message_clean,"ENSEAIS"))

# Question 3.6
def kasiski(text):
    seq3 = {}
    sortie_Seq = []
    sortie_Pos = []
    for i in range(len(text)-3):
        seq = ""
        for j in range(3):
            seq = seq + text[i+j]
        seq3[seq] = seq3.get(seq,0) + 1
    
    for i in seq3:
        if seq3[i]>1:
            sortie_Seq.append(i)

    for k in sortie_Seq:
        position = []
        for i in range(len(text)-3):
            seq = ""
            for j in range(3):
                seq = seq + text[i+j]
            if seq == k :
                position.append(i)
        sortie_Pos.append(position)
    return sortie_Seq, sortie_Pos


test = "messager tres mesquin d'un village mesopotamien"
test_clean = "".join([c for c in test.upper() if c.isalpha()])

sequence, position = kasiski(test_clean)
print(sequence, position)

def distance(seq, pos):
    sortie = {}
    for i in range(len(pos)) :
        dist = []
        for j in range(len(pos[i])-1) :
            dist.append(pos[i][j+1]-pos[i][j])
        sortie[seq[i]]=dist
    return sortie

print(distance(sequence, position))

sequence, position = kasiski(message_clean)
print(distance(sequence, position))
# On observe beaucoup de multiple de 7 (49, 70, 21, 95, 7, ...)
# Sauf quelques cas particuliers (312, 143, 28, ....)

# Question 3.7
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def OTP(message):
    N = len(message)
    key = ""
    for i in range(N):
        key = key + alphabet[randint(0,25)]
    return key

print(OTP(message_clean))