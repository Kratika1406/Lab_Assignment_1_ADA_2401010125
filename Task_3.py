import time

# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Fibonacci Recursive
calls = 0
def fib_recursive(n):
    global calls
    calls += 1
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Fibonacci DP
def fib_dp(n):
    dp = [0,1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

n = 20

# Recursive
calls = 0
start = time.time()
fib_recursive(n)
rec_time = time.time() - start

# DP
start = time.time()
fib_dp(n)
dp_time = time.time() - start

print("Recursive calls:", calls)
print("Recursive time:", rec_time)
print("DP time:", dp_time)
