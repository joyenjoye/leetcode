
# Before 44min 30s理论, After 例题
def brute_force(T: str, p: str) -> int:
    n = len(T)
    m = len(p)

    i = 0
    j = 0
    while i < n and j < m:
        if T[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0
    if j == m:
        return i-j
    else:
        return -1

##########################
# O(n+m)

# 生成next数组
# O(m)
def generate_next(p: str):
    m = len(p)
    next = [0 for _ in range(m)]  # 初始化数组元素全部为0
    left = 0
    for right in range(1, m):
        while left > 0 and p[left] != p[right]:
            left = next[left-1]

        if p[left] == p[right]:
            left += 1

        next[right] = left
    return next

# p = abbdabbc
# left = 0, right = 1 a!=b left = 0 next[1] = 0
# left = 0, right = 2,a!=b left = 0 next[2] = 0
# left = 0, right = 3,a==a left = 1 next[3] = 1
# left = 1, right = 4,b==b left = 2 next[4] = 2
# left = 2, right = 5,b==b left = 3 next[5] = 3

# O(n)

def kmp(T: str, p: str) -> int:
    n, m = len(T), len(p)
    next = generate_next(p)
    j = 0
    for i in range(n):
        while j > 0 and T[i] != p[j]:
            j = next[j-1]
        if T[i] == p[j]:
            j += 1
        if j == m:
            return i-j+1
    return -1
