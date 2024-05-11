arr=[8,3,1,9,8,7,3,6]
stack=[]
stack_len=8
unit=[]
operations_count=0

def push(i):
    global operations_count, unit
    stack.append(i)
    unit.append(1)
    operations_count+=1
    print(f"Stack is {stack} after pushing {i}")

def pop():
    global operations_count
    if stack:
        stack.pop()
        operations_count+=1

def multipop(k):
    global operations_count, unit
    no_of_elements=min(k,len(stack))
    for _ in range (no_of_elements):
        pop()
    print(f"The stack is {stack} after popping {no_of_elements} element")
    unit.append(no_of_elements)


for i in arr:
    print(f"Element {i}:")
    if i<=len(stack):
        print(f"As i is less than {len(stack)} we mulipop {i} elements from stack")
        multipop(i)
    push(i)


print(f"T(n)={sum(unit)} and number of operations is {operations_count}")
