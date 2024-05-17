def encrypt(pt,key):
    ct = ''
    temp = len(key) - (len(pt) % len(key))
    if temp==len(key):
        temp = 0
    for i in range(temp):
        pt = pt+'X'
    order = list(key)
    order.sort()
    for i in order:
        index = key.index(i)
        key = key.replace(i,' ',1)
        while index<len(pt):
            ct = ct+pt[index]
            index+= len(key)
    return ct  

def decrypt(ct,key):
    dt = ''
    order = list(key)
    order.sort()
    n=len(ct)
    for i in range(len(ct)):
        dt=dt+' '
    for i in order:
        index = key.index(i)
        key = key.replace(i,' ',1)
        while index<n:
            dt = dt[0:index]+ ct[0] + dt[index+1:]
            index+= len(key)
            ct = ct[1:]
    return dt

pt = input("Enter plain text:").upper().replace(' ','')
key = input("Enter key:").upper().replace(' ','')
ct = encrypt(pt,key)
dt = decrypt(ct,key)
print(f"Plain text: {pt}\nKey: {key}\nEncrypted text: {ct}\nDecrypted text: {dt}")



