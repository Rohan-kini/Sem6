arr=[8,3,1,6,2,4]
stack=[]
len_stack=6
unit=[]
operation_count=0

def push(i):
    global operation_count,unit
    stack.append(i)
    operation_count+=1
    unit.append(1)
    print(f"Stack after pushing {i} is {stack}")

def pop():
    global operation_count
    if stack:
        stack.pop()
        operation_count+=1

def multipop(k):
    global unit
    minimum=min(k,len(stack))
    for _ in range(minimum):
        pop()
    unit.append(minimum)
    print(f"Stack after multipop {minimum} elements is {stack}")

for i in arr:
    print(f"Element {i}-")
    if i<len(stack):
        print(f"As {i} is less that {len(stack)} we perform multipop")
        multipop(i)
    push(i)

print(stack)
print(f"T(n)={sum(unit)} and number of operations is {operation_count}")
print(f"Aggregate analysis is {sum(unit)/operation_count}")
