def climbStairs(n):
 steps = []
 steps.append(1)
 steps.append(2)
 for i in range(2, n):
  steps.append(f[i - 1] + f[i - 2])
 return steps[n - 1]
n=3
print(climbStairs(n))
