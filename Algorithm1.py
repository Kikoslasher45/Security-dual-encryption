# alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# def vegenere_enc(key, plain_text):
#     cipher_text = ""
#     iterator = 0
#     for x in range(0, len(plain_text)):
#         index_1 = alphabets.index(key[iterator])
#         index_2 = alphabets.index(plain_text[x])
#         cipher_text += alphabets[(index_1 + index_2) % 26]
#         if iterator % 26 != 0 and iterator != 0:
#             iterator += 1
#         else:
#             iterator = 0
#     print(cipher_text)
#     return cipher_text

# #or

def fence_enc(depth: int, plain_text: str):
    mat = []
    iterator = 0
    text = 0
    added_value = 1
    for x in range(0, len(plain_text)):
        mat.append([])
        for y in range(0, depth):
            if y == iterator:
                mat[x].append(plain_text[text])
                text += 1
            else:
                mat[x].append('_')
        if iterator == 0:
            added_value = 1
        elif iterator == depth - 1:
            added_value = -1
        iterator += added_value
    cipher_text = ""
    for y in range(0, depth):
        for x in range(0, len(plain_text)):
            if mat[x][y] != '_':
                cipher_text += mat[x][y]
    return cipher_text

#plain text:
#53229150475050194141565339280050449081308650241130
#cipher text:
#55383300390110251529312796840494450482101100605455
#key:
#7
plaintext = "53229150475050194141565339280050449081308650241130"
key = 7
cipher = fence_enc(key, plaintext)
print(cipher)
