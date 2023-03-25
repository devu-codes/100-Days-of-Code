# Fibonacci Numbers
# 0 1 1 2 3 5 8 13 21 34 55
dp = [-1 for i in range(1000)]
dp[0], dp[1] = 0, 1

def fib_bu(n, dp):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(fib_bu(5, dp))

def fib_td(n):

    if (dp[n] < 0):
        if n == 0:
            dp[n] = 0
        elif n == 1:
            dp[n] = 1
        else:
            dp[n] = fib_td(n-1) + fib_td(n-2)
    return dp[n]

print(fib_td(10))