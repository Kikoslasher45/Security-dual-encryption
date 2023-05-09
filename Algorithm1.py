import string
from itertools import zip_longest
import random
from collections import deque
# import tensorflow as tf
alphabets = [str(i) for i in range(0,10)]

def one_time_pad_enc(key, plain_text):
    cipher_text = ""
    for x in range(0, len(plain_text)):
        index_1 = alphabets.index(key[x])
        index_2 = alphabets.index(plain_text[x])
        cipher_text += alphabets[(index_1 + index_2) % len(alphabets)]
    return cipher_text
