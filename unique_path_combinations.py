import math

def uniquePaths(m, n):
    path_len = m+n-2
    right_choice = m-1
    # down_choice = n-1
    return math.comb(path_len, right_choice)

print(uniquePaths(7,3))
print(uniquePaths(3, 7))

# pascal triangle. binomial