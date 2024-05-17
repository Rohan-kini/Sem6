import math

def rsa(p,q,pt):
    n=p*q
    phi=(p-1)*(q-1)
    
    e=2
    while e<phi:
        if math.gcd(e,phi)==1:
            break
        e+=1
    print(e)

    d=1
    while True:
        if (d*e)%phi==1:
            break
        d+=1
    print(d)

    print(f"Public key:{(e,n)}")
    print(f"Private key:{(d,n)}")

    c=(pt**e)%n
    print(c)
    de=(c**d)%n
    print(de)


if __name__=="__main__":
    p=int(input("Enter value of p:"))
    q=int(input("Enter value of q:"))
    pt=int(input("Enter value of pt:"))
    rsa(p,q,pt)
