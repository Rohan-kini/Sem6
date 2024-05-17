a=6
b=4
g=int(input("Enter g value:"))
p=int(input("Enter p value:"))

print("Calculating XA...")
XA=(g**a)%p
print(XA)

print("Calculating XB...")
XB=(g**b)%p
print(XB)

AK=(XB**a)%p
BK=(XA**b)%p

print(AK)
print(BK)