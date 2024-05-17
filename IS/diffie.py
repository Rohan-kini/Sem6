p=int(input("Enter p value:"))
g=int(input("Enter g value:"))

a=6
b=4

print("p and g will be common between both alice and bob")

print("Calculate XA")
XA=(g**a)%p
print("Calculate XB")
XB=(g**b)%p

print(XA)
print(XB)

AK=(XB**a)%p
BK=(XA**b)%p

if (AK==BK):
    print("message send successful")
else:
    print("error")