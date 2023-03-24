import math
def compute_sqrt(N, precision):
    start = 0 
    end = N

    ans = 1
    while start <= end: 
        mid = end - (end - start) // 2

        if mid * mid == N:
            ans = mid
            break
        elif mid * mid > N:
            end = mid - 1
        else:
            ans = mid
            start = mid +1
    increment = 0.1 
    for i in range(precision):
        while ans * ans <= N:
            ans += increment 
        ans -= increment 
        increment = (increment/10) 
    return ans 


# Test Case
N = 39 
print(compute_sqrt(39, 2))
print('%.2f' %math.sqrt(39))