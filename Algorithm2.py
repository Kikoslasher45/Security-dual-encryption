
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
