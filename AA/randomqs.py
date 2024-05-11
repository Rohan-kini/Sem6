import random
c1=0
c2=0

def rquicksort(arr):
    global c1
    if len(arr)<=1:
        return arr
    else:
        pivot=random.choice(arr)
        right=[]
        left=[]
        middle=[]
        for i in range(len(arr)):
            c1+=1
            if arr[i]>pivot:
                right.append(arr[i])
            elif arr[i]<pivot:
                left.append(arr[i])
            else:
                middle.append(arr[i])
        return rquicksort(left) + middle + rquicksort(right)
        

def quicksort(arr):
    global c2
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[]
        right=[]
        for i in range(1,len(arr)):
            c2+=1
            if arr[i]>pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)
        


arr=[random.randint(0,499) for i in range(500) ]
print("Normal Quicksort",quicksort(arr))
print(f"Number of comparisons={c2}")
print("Randomized Quicksort",rquicksort(arr))
print(f"Number of comparsions={c1}")
