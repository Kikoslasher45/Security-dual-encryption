
import binascii
# words_to_find = "PqnjhxuDgBpglpcBdjhhp"
# words_to_find= words_to_find.lower()
# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for i in range(0,26):
#     line = ""
#     for x in words_to_find:       
#        index = (alphabet.index(x) + i + 1) % 26
#        line += alphabet[index]       
#     print(line) 
    
# abyusif or marwan moussa

# encrypted_message = "-.-. -- .--. / .---- --... - --- -.- .- ..--- ----- ..--- ...-- /"
# messages = encrypted_message.split("/")
# print(messages)
# from qrtools import QR
# myCode = QR(filename=u"/home/psutton/Documents/Python/qrcodes/qrcode.png")
# if myCode.decode():
#   print myCode.data
#   print myCode.data_type
#   print myCode.data_to_string()
# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","4","5","6","7","8","9"]
# word_to_be_found = "COMPUTERSSQZTFACG"
# cipher = "EABRGIGDHF0ztF0zt"
# word_to_be_found = word_to_be_found.lower()
# cipher = cipher.lower()
# key = ""
# for x in range(0,len(cipher)):
#     index = (alphabet.index(cipher[x]) - alphabet.index(word_to_be_found[x])) % len(alphabet)
#     key += alphabet[index]
# print(key)
#key = cvy
#"EABRGIGDHF0ztF0zt"
# key = "cvycvycvycvycvycv"
# text =""
# for x in range(0, len(cipher)):
#     index = (alphabet.index(
#         cipher[x]) - alphabet.index(key[x])) % len(alphabet)
#     text += alphabet[index]
# print(text)
def hex2bin(s):
    mp = {'0': "0000",'1': "0001",'2': "0010",'3': "0011",'4': "0100",'5': "0101",'6': "0110",'7': "0111",'8': "1000",'9': "1001",'A': "1010",'B': "1011",'C': "1100",'D': "1101",'E': "1110",'F': "1111"}
    bin = ""
    for i in  range(len(s)):
        bin = bin +  mp[s[i]]
    return bin
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)
def bin2hex(s):
    mp = {"0000": '0',"0001": '1',"0010": '2',"0011": '3',"0100": '4',"0101": '5',"0110": '6',"0111": '7',"1000": '8',"1001": '9',"1010": 'A',"1011": 'B',"1100": 'C',"1101": 'D',"1110": 'E',"1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex
def bin2hdec(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3', "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex
S1 = "1010535d406b437871727172797b28216d"
S2 = "1010101010101010101010101010101010"
S1_new = hex2bin(S1.upper())
S2_new = hex2bin(S2.upper())
plaint = ""
for x in range(0,len(S1_new)):
    if S1_new[x] == S2_new[x]:
        plaint += "0"
    else:
        plaint += "1"

