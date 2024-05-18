def encrypt(pt,key):
    ct=''
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in pt:
        if letter in alpha:
            letter_index=(alpha.find(letter)+key)%26
            ct+=alpha[letter_index]
        else:
            ct+=letter
    return ct

def decrypt(ct,key):
    og=''
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in ct:
        if letter in alpha:
            letter_index=(alpha.find(letter)-key)%26
            og+=alpha[letter_index]
        else:
            og+=letter
    return og

if __name__=="__main__":
    pt="hello".upper()
    key=3
    cipher=encrypt(pt,key)
    print(cipher)
    og=decrypt(cipher,key)
    print(og)
