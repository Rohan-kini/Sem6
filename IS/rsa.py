import math

def public_key(phi):
    e=2
    while e<phi:
        if math.gcd(e,phi)==1:
            break
        e+=1
    return e

def private_key(e,phi):
    d=1
    while True:
        if (d*e)%phi==1:
            break
        d+=1
    return d

if __name__=="__main__":
    msg=17
    p=11
    q=7
    n=p*q
    phi=(p-1)*(q-1)
    e=public_key(phi)
    print(f"Public key:{(e,n)}")
    d=private_key(e,phi)
    print(f"Private key:{(d,n)}")
    encrypt=(msg**e)%n
    print(encrypt)
    decrypt=(encrypt**d)%n
    print(decrypt)


