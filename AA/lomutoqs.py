import random

def partition_lomuto(arr, low, high):
    if low < high:
        start = low - 1
        pivot = high
        for end in range(low, high):
            if arr[end] <= arr[pivot]:
                start += 1
                arr[start], arr[end] = arr[end], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto(arr, low, p - 1)
        partition_lomuto(arr, p + 1, high)

def partition_lomuto_random(arr, low, high):
    if low < high:
        k = random.randint(low, high)
        arr[k], arr[high] = arr[high], arr[k]
        start = low - 1
        pivot = high
        for end in range(low, high):
            if arr[end] <= arr[pivot]:
                start += 1
                arr[start], arr[end] = arr[end], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto_random(arr, low, p - 1)
        partition_lomuto_random(arr, p + 1, high)



random_array = [random.randint(0, 500) for _ in range(500)]
random_array1=random_array.copy()
partition_lomuto(random_array, 0, len(random_array) - 1)
partition_lomuto_random(random_array1, 0, len(random_array) - 1)