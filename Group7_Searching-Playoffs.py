# Learning Task (Searching)
# Group7_Vargas_DimanarigArjunRashid
# Binary Search (Road to playoffs)

# value to positive infinity
from math import inf

# number of test cases
t = int(input(" "))

# iterations in the given test cases
while t > 0:
    t -= 1
    n, m, k, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    lo = b - 1
    hi = n
    # search for the number of teams that have a
    # non-zero probability of making it to the playoffs.
    while hi - lo > 1:
        i = (lo + hi) // 2
        need = m * (k - (b - 1) - (n - i))

        for j in range(b - 1, i):
            if a[j] > a[i] + m:
                need = inf
            else:
                need -= a[i] + m - a[j]
        if need > 0:
            hi = i
        else:
            lo = i
    print(lo + 1)