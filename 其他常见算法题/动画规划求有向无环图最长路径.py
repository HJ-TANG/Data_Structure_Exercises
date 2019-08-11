import numpy as np


# adj_matrix[i][j]有值表示节点i到节点j之间有路径，且距离为adj_matrix[i][j]
adj_matrix = [
    [0, 0.1, 0, 0.5, 0.7, 1.0],
    [0, 0, 0.1, 0, 0.7, 0],
    [0, 0, 0, 0.1, 0, 0],
    [0, 0, 0, 0, 0.1, 0.6],
    [0, 0, 0, 0, 0, 0.1],
]
adj_matrix = np.array(adj_matrix)


def getDP(adj):
    # 以下代码块可求任意两个节点间的最短路径
    # dp = np.zeros((len(adj_matrix), len(adj_matrix[0])))
    # for i in range(len(dp)):
    #     dp[i][i+1] = adj_matrix[i][i+1]
    # for i in range(0, len(dp)):
    #     for j in range(i+2, len(dp[0])):
    #         not_null = np.flatnonzero(adj[:, j])  # 提取去第j列非零的元素，即节点j跟哪几个节点直接相连
    #         print(not_null)
    #         print([dp[i][n]+adj[n][j] for n in not_null])
    #         dp[i][j] = max(dp[i][j-1]+dp[j-1][j], max([dp[i][n]+adj[n][j] for n in not_null if i <= n < j]))

    dp = np.zeros(len(adj_matrix[0]))
    dp[1] = 0.1
    for j in range(2, len(dp)):
        not_null = np.flatnonzero(adj[:, j])  # 提取去第j列非零的元素，即节点j跟哪几个节点直接相连
        dp[j] = max(dp[j-1]+adj[j-1][j], max([dp[n]+adj[n][j] for n in not_null if 0 <= n < j]))
    print(dp)


getDP(adj_matrix)

