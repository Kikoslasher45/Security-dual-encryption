import Algorithm1
import Algorithm2
import Algorithm3

plaintext1 = "86"
key1 = "56"
C1=Algorithm1.one_time_pad_enc(key1, plaintext1)
print("C1: ",C1)

plaintext2 = "17820305457150318"
key2 = 3
C2=Algorithm2.fence_enc(key2, plaintext2)
print("C2: ",C2)

Ya = 141
Xa = 3
k = 5
a = 7
q = 202


chunks=[3,1,2,2,2,3,2,2]
message=""
# process the message in chunks, the size of each one corresponding to its index in the chunks list
for i in range(len(chunks)):
    # get the next chunk
    chunk=C2[:chunks[i]]
    # remove the chunk from the message
    C2=C2[chunks[i]:]
    # decrypt the chunk
    # print("chunk: ",chunk)
    m=str(Algorithm3.elgamal_decrypt( C1, chunk,Xa,q))
    # print("m: ",m)
    message+=m
    
print("Message: ",message)
