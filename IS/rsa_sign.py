import math
import hashlib

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
    ct=pow(pt,e,n)
    return ct

def decrypt(ct,d,n):
    og=pow(ct,d,n)
    return og

if __name__=="__main__":

    p=int(input("Enter p:"))
    q=int(input("Enter q:"))
    pt=input("Enter pt:")
    n=p*q
    phi=(p-1)*(q-1)
    e=public_key(p,q,phi)
    print(f"e={e}")
    d=private_key(e,phi)
    print(f"d={d}")

    hash_value=hashlib.sha256(pt.encode()).hexdigest()
    print(hash_value)
    hash_int=int(hash_value,16)%n
    signature= (hash_int**d)%n
    print(signature)

    hash_value=hashlib.sha256(pt.encode()).hexdigest()
    print(hash_value)
    hash_int=int(hash_value,16)%n
    decrypted=pow(signature,e,n) ## (signature**e)%n
    print(decrypted)

