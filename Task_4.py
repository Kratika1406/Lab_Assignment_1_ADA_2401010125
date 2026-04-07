calls1 = 0
def func1(n):
    global calls1
    calls1 += 1
    if n <= 1:
        return 1
    return func1(n//2) + n

calls2 = 0
def func2(n):
    global calls2
    calls2 += 1
    if n <= 1:
        return 1
    return func2(n//2) + func2(n//2) + n

import time

n = 1024

start = time.time()
func1(n)
time1 = time.time() - start

start = time.time()
func2(n)
time2 = time.time() - start

print("Func1 calls:", calls1, "Time:", time1)
print("Func2 calls:", calls2, "Time:", time2)
