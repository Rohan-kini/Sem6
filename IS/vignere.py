def generate(key):
    pad=key
    if len(pt)==len(key):
        pad=key
    else:
        for i in range(len(pt)-len(key)):
            pad+=key[i%len(key)]
    return pad

def encrypt(pt,pad_key):
    cipher_text=""
    for i in range(len(pt)):
        cipher_text+=chr(((ord(pt[i])-65 + ord(pad_key[i])-65)%26)+65)
    return cipher_text

def decrypt(ct,pad_key):
    og=""
    for i in range(len(ct)):
        og+=chr(((ord(ct[i])-65 - ord(pad_key[i])-65)%26)+65)
    return og


if __name__=="__main__":
    pt="gabba"
    pt=pt.upper()
    key="pant"
    pad_key=generate(key)
    pad_key=pad_key.upper()
    print(pt)
    print(pad_key)

    ct=encrypt(pt,pad_key)
    print(ct)
    og=decrypt(ct,pad_key)
    print(og)