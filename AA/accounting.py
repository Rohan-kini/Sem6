push_amor_cost=2
push_actual_cost=1

pop_amor_cost=0
pop_actual_cost=1


def push(stack,n,cost,credit):
    for i in range(n):
        stack.append(i)
        if push_amor_cost>push_actual_cost:
            cost+=push_amor_cost
            credit+=(push_amor_cost-push_actual_cost)
            print(f"Credits Earned:{credit}")
        else:
            cost+=push_amor_cost
            credit-=push_actual_cost
            print(f"Credit Consumed:{credit}")
    return stack,cost,credit

def multipop(stack,n,cost,credit):
    for i in range(n):
        m=int(input("Enter number of elements to be popped:"))
        k=min(m,len(stack))
        for j in range(k):
            stack.pop()
            if pop_amor_cost>pop_actual_cost:
                 cost+=pop_amor_cost
                 credit+=(pop_amor_cost-pop_actual_cost)
                 print(f"Credits Earned:{credit}")
            else:
                 cost+=pop_amor_cost
                 credit-=pop_actual_cost
                 print(f"Credit Consumed:{credit}")
    return stack,cost,credit
    

stack=[]
cost=0
op=0
credit=0

n=int(input("Enter number of elements to be pushed:"))
op+=n
stack,cost,credit=push(stack,n,cost,credit)
print(f"Stack after push opration:{stack}")
print(f"Cost is {cost}")
print(f"Credit is :{credit}")

n=n=int(input("Enter number of times multipop needs to be performed:"))
op+=n
stack,cost,credit=multipop(stack,n,cost,credit)
print(f"Stack after multipop opration:{stack}")
print(f"Cost is {cost}")
print(f"Credit is :{credit}")


print(f"Accounting analysis:{cost/op}")

