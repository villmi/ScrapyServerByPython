def isMatch(str1, pattern):
    if (str1 is None) or (pattern is None):
        return False
    flag = [(True for i in range(100)) for i in range(100)]

    m = len(str1) + 1
    n = len(pattern) + 1
    for f in flag:
        f[0] = False
    for num in range(1,n):
        if (num >= 2) and (pattern[num - 1] == '*'):
            flag[0][num] = flag[0][num - 2]
        else:
            flag[0][num] = False

    for i in range(1,m):
        for j in range(1,n):
            if j >= 2 and pattern[j - 1] == '*':
                if pattern[j - 2] == str1[i - 1] or pattern[j - 2] == '.':
                    flag[i][j] = flag[i][j - 2] or flag[i - 1][j] or flag[i - 1][j - 2]
                else:
                    flag[i][j] = flag[i][j - 2]
            elif pattern[j -1] == str1[i - 1] or pattern[j - 1] == '.':
                flag[i][j] = flag[i - 1][j - 1]
            else:
                flag[i][j] = False
    return flag[m - 1][n - 1]


