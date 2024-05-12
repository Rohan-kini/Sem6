arr=[8,3,1,9,8,7,3,6]
stack=[]
stack_len=6
unit=[]
operations_count=0

def push(i):
    global operations_count,unit
    stack.append(i)
    operations_count+=1
    unit.append(1)
    print(f"Stack after pushing {i} is {stack}")


def pop():
    global operations_count
    if stack:
        stack.pop()
    operations_count+=1

def multipop(k):
    global operations_count,unit
    no_of_elements=min(k,len(stack))
    for _ in range(no_of_elements):
        pop()
    unit.append(no_of_elements)
    print(f"Stack after multipop is {stack}")

    

for i in arr:
    print(f"Element:{i}")
    if i<=len(stack):
        print(f"As {i} is less than {len(stack)} we perform multipop {i} times")
        multipop(i)
    push(i)

print(f"T(n)={sum(unit)} and num of operations is {operations_count}")
print(f"Time complexity O({sum(unit)//operations_count})")