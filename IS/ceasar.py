def encrypt(key,pt):
    result=""
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in pt:
        if letter in alpha:
            letter_index=(alpha.find(letter)+key)%26
            result+=alpha[letter_index]
        else:
            result+=letter
    return result

def decrypt(key,ct):
    og=""
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in ct:
        if letter in alpha:
            letter_index=(alpha.find(letter)-key)%26
            og+=alpha[letter_index]
        else:
            og+=letter
    return og

        
   
if __name__=="__main__":
    pt="azaz".upper()
    key=3
    ct=encrypt(key,pt)
    print(ct)
    og=decrypt(key,ct)
    print(og)