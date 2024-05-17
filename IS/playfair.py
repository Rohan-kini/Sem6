def create_matrix(key,list=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
    key_letters,completters,matrix=[],[],[]
    for i in key:
        if i not in key_letters:
            key_letters.append(i)
            completters.append(i)
    for i in list:
        if i not in completters:
            completters.append(i)
    while completters!=[]:
        matrix.append(completters[:5])
        completters=completters[5:]
    return matrix

def addbuffer(msg):
    index=0
    while(index<len(msg)-1):
        l1,l2=msg[index],msg[index+1]
        if l1==l2:
            msg=msg[:index+1]+"X"+msg[index+1:]
        index+=2
    if len(msg)%2!=0:
        msg+="X"
    return msg

def indexof(letter,matrix):
    for i in range(5):
        try:
            col=matrix[i].index(letter)
            return i,col
        except:
            continue


def playfair(msg,key,encrypt=True):
    inc=1 if encrypt else -1
    matrix=create_matrix(key)
    msg=msg.replace(" ","")
    msg=addbuffer(msg)
    cipher_text = ''
    for l1,l2 in zip(msg[0::2],msg[1::2]):
        row1,col1=indexof(l1,matrix)
        row2,col2=indexof(l2,matrix)
        if row1==row2:
            cipher_text+=matrix[row1][(col1+inc)%5]+matrix[row2][(col2+inc)%5]
        elif col1==col2:
            cipher_text+=matrix[(row1+inc)%5][col1]+matrix[(row2+inc)%5][col2]
        else:
            cipher_text+=matrix[row1][col2]+matrix[row2][col1]
    return cipher_text


if __name__=="__main__":

    pt=input("Enter plain text:").upper()
    key=input("Enter key:").upper()
    cipher_text=playfair(pt,key)
    print(cipher_text)
    og=playfair(cipher_text,key,encrypt=False)
    print(og)