import string
from itertools import zip_longest
import random
from collections import deque
# import tensorflow as tf
alphabets = [str(i) for i in range(0,10)]

def vegenere_enc(key, plain_text):
    cipher_text = ""
    iterator = 0
    for x in range(0, len(plain_text)):
        index_1 = alphabets.index(key[iterator])
        index_2 = alphabets.index(plain_text[x])
        cipher_text += alphabets[(index_1 + index_2) % len(alphabets)]
        if iterator % len(alphabets) != 0 and iterator != 0:
            iterator += 1
        else:
            iterator = 0
    return cipher_text
# Algorithm Inputs
# key:
# 458315581922090762617144991137579323207626947709916
# plain text:
# 918662314153534663063072149627043133264308188892444
# 087825451810417752116093688296738303740183079359409
# 133617519840627482384049000598543386335853689595949
# 161706013541965170402020219501055436656676613770289
# 102151361791296726998030155004299361495260191688119
# 171181196268309622574023524775460188269874432082999
# 250829216631736363789058388409570990368858152852474
# 286032023422844243294166676310516594391842735108099
#ECB with vegenere 
plaint_text = ["918662314153534663063072149627043133264308188892444",
               "087825451810417752116093688296738303740183079359409",
               "133617519840627482384049000598543386335853689595949",
               "161706013541965170402020219501055436656676613770289",
               "102151361791296726998030155004299361495260191688119",
               "171181196268309622574023524775460188269874432082999",
               "250829216631736363789058388409570990368858152852474",
               "286032023422844243294166676310516594391842735108099"]
key = "458315581922090762617144991137579323207626947709916"
cipher = []
for x in plaint_text:
    cipher.append( vegenere_enc(key,x))
print(cipher)
