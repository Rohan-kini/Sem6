def generate(key,list=["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
    key_items,comp_items,matrix=[],[],[]
    for i in key:
        if i not in key_items:
            key_items.append(i)
            comp_items.append(i)
    for i in list:
        if i not in comp_items:
            comp_items.append(i)
    while comp_items!=[]:
        matrix.append(comp_items[:5])
        comp_items=comp_items[5:]
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
    matrix=generate(key)
    msg=msg.replace(" ","")
    msg=addbuffer(msg)
    ct=''
    for l1,l2 in zip(msg[0::2],msg[1::2]):
        row1,col1=indexof(l1,matrix)
        row2,col2=indexof(l2,matrix)
        if row1==row2:
            ct+=matrix[row1][(col1+inc)%5]+matrix[row2][(col2+inc)%5]
        elif col1==col2:
            ct+=matrix[(row1+inc)%5][col1]+matrix[(row2+inc)%5][col2]
        else:
            ct+=matrix[row1][col2]+matrix[row2][col1]
    return ct

if __name__=="__main__":
    pt="instruments".upper()
    key="monarchy".upper()
    cipher=playfair(pt,key)
    print(cipher)
    og=playfair(cipher,key,encrypt=False)
    print(og)