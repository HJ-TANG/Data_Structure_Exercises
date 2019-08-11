import numpy as np


def edit_distance(str1, str2):
    dp = np.zeros((len(str1)+1, len(str2)+1))
    for i in range(len(str1)+1):
        dp[i][0] = i
    for j in range(len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                temp = 0
            else:
                temp = 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+temp)
    return dp


print(edit_distance('aaaa', 'aabbc'))
