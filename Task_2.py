import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sizes = [100, 500, 1000, 5000]

linear_times = []
binary_times = []

for n in sizes:
    arr = sorted(random.sample(range(10000), n))
    
    key_best = arr[0]
    key_avg = arr[n//2]
    key_worst = -1

    # Linear
    start = time.time()
    linear_search(arr, key_avg)
    linear_times.append(time.time() - start)

    # Binary
    start = time.time()
    binary_search(arr, key_avg)
    binary_times.append(time.time() - start)

# Plot
plt.plot(sizes, linear_times, label="Linear Search")
plt.plot(sizes, binary_times, label="Binary Search")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.title("Search Comparison")
plt.show()
