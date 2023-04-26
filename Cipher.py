plaintext_alphabet = "abcdefghijklmnopqrstuvwxyz" 
ciphertext_alphabet = "ZGLEIYMAXDHROPKWTQNSCVUBJF" ##replace with given ciphertext

encode_trans = str.maketrans(plaintext_alphabet, ciphertext_alphabet)
decode_trans = str.maketrans(ciphertext_alphabet, plaintext_alphabet)

def subst_encode(s):
    return s.translate(encode_trans)

def subst_decode(s):
    return s.translate(decode_trans)

print(subst_decode("PXLI MKXPM DCPXKQ AZLHIQ"))  ##replace with given ciphertext to decode
