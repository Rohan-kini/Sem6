def encrypt(pt,key):
    ct=''
    for i in range(len(pt)):
        ct+=chr((((ord(pt[i])-65)+(ord(key[i])-65))%26)+65)
    return ct

def decrypt(ct,key):
    og=''
    for i in range(len(ct)):
        og+=chr((((ord(ct[i])-65)-(ord(key[i])-65))%26)+65)
    return og

def padding(pt,key):
    pad=key
    if len(pt)==len(key):
        pad=key
    else:
        for i in range(len(pt)-len(key)):
            pad+=key[i%len(key)]
    return pad

if __name__=="__main__":
    pt="hello".upper()
    print(pt)
    key="hi"
    pad_key=padding(pt,key).upper()
    cipher=encrypt(pt,pad_key)
    print(cipher)
    og=decrypt(cipher,pad_key)
    print(og)