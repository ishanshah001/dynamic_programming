dict = {}

def fact(a):
    if a == 1:
        return 1
    if a in dict:
        return dict[a]
    dict[a] = a*fact(a-1)
    return dict[a]

def comb(n, k):
    return fact(n)//(fact(k)*fact(n-k))

def uniquePaths(m, n):
    path_len = m+n-2
    right_choice = m-1
    # down_choice = n-1
    return comb(path_len, right_choice)
        

print(uniquePaths(7,3))
print(uniquePaths(3, 7))

# pascal triangle. binomial