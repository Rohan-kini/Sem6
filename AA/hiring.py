import random 

print("Normal Approach")
candidates=[0,1,2,3,4,5,6,7,8,9]
print(candidates)
interviewed_candidates=[]
hird_candidates=[]

for candidate in candidates:
    interviewed_candidates.append(candidate)
    if not hird_candidates or candidate>max(hird_candidates):
        hird_candidates.append(candidate)

firing_cost=len(hird_candidates)-1
print(interviewed_candidates)
print(hird_candidates)
print(f"Firing cost={firing_cost}")


print("Randomized Approach")
candidates=[0,1,2,3,4,5,6,7,8,9]
print(candidates)
interviewed_candidates=[]
hird_candidates=[]

for i in range (len(candidates)):
    selected_candidate=random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)

max_candidate=-1

for candidate in interviewed_candidates:
    if candidate>max_candidate:
        max_candidate=candidate
        hird_candidates.append(candidate)

firing_cost=len(hird_candidates)-1
print(interviewed_candidates)
print(hird_candidates)
print(f"Firing cost={firing_cost}")

