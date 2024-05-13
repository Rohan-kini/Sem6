doubling_cost=[]
current=1
potential=[]

for i in range(1,11):
    if current<i:
        current*=2
        doubling_cost.append(i-1)
    else:
        doubling_cost.append(0)
    potential.append(2*i-current)

total=[ x+1 for x in doubling_cost]

print("doubling_cost\tIteration\tTotal_cost\tpotential_cost\tamortized_cost")

print(f"{doubling_cost[0]}\t\t{1}\t\t{total[0]}\t\t{potential[0]}\t\t{total[0]+potential[0]}")

for j in range(1,10):
    amortized_cost=total[j]+potential[j]-potential[j-1]
    print(f"{doubling_cost[j]}\t\t{j+1}\t\t{total[j]}\t\t{potential[j]}\t\t{amortized_cost}")


