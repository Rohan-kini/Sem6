def encrypt(pt,key):
    pt=pt.upper()
    result=""
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in pt:
        if letter in alpha:
            letter_index=(alpha.find(letter)+key)%26
            result+=alpha[letter_index]
        else:
            result+=letter
    return result


def decrypt(ct,key):
    result=""
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in pt:
        if letter in alpha:
            letter_index=(alpha.find(letter)-key)%26
            result+=alpha[letter_index]
        else:
            result+=letter
    return result
    

if __name__=="__main__":
    pt="toota hai gabba ka ghamand"
    key=3
    ciphertext=encrypt(pt,key)
    print(ciphertext)
    og=decrypt(ciphertext,key)
    print(og)
