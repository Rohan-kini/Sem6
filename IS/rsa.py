import math

def public_key(p,q,phi):
    e=2
    while e<phi:
        if math.gcd(e,phi)==1:
            break
        e+=1
        if (e==p or e==q):
            e+=1
    return e

def private_key(e,phi):
    d=1
    while True:
        if (d*e)%phi==1:
            break
        d+=1
    return d

def encrypt(pt,e,n):
    ct=(pt**e)%n
    return ct

def decrypt(ct,d,n):
    og=(ct**d)%n
    return og

if __name__=="__main__":

    p=int(input("Enter p:"))
    q=int(input("Enter q:"))
    pt=int(input("Enter pt:"))
    n=p*q
    phi=(p-1)*(q-1)
    e=public_key(p,q,phi)
    print(f"e={e}")
    d=private_key(e,phi)
    print(f"d={d}")
    ct=encrypt(pt,e,n)
    og=decrypt(ct,d,n)
    print(ct)
    print(og)
