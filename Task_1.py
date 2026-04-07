import time
import matplotlib.pyplot as plt
import math

# O(1)
def constant_time(n):
    return n * 2

# O(n)
def linear_time(n):
    s = 0
    for i in range(n):
        s += i
    return s

# O(n^2)
def quadratic_time(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += i + j
    return s

# O(log n)
def logarithmic_time(n):
    i = 1
    while i < n:
        i *= 2

sizes = [10, 100, 500, 1000]

const_times = []
linear_times = []
quad_times = []
log_times = []

for n in sizes:
    start = time.time()
    constant_time(n)
    const_times.append(time.time() - start)

    start = time.time()
    linear_time(n)
    linear_times.append(time.time() - start)

    start = time.time()
    quadratic_time(n)
    quad_times.append(time.time() - start)

    start = time.time()
    logarithmic_time(n)
    log_times.append(time.time() - start)

# Plot
plt.plot(sizes, const_times, label="O(1)")
plt.plot(sizes, linear_times, label="O(n)")
plt.plot(sizes, quad_times, label="O(n^2)")
plt.plot(sizes, log_times, label="O(log n)")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.legend()
plt.title("Growth of Algorithms")
plt.show()
