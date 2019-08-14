tree_num = int(input())

cost = []
for i in range(tree_num):
    ai, bi, ci = input().strip().split()
    ai = int(ai)
    bi = int(bi)
    ci = int(ci)
    cost.append([ai, bi, ci])
cost.append([0, 0, 0])

dp = [[0, 0] for j in range(tree_num+1)]
dp[0][0] = cost[0][0] + cost[0][2]
dp[0][1] = cost[0][1]

for i in range(1, tree_num):
    temp1 = dp[i-1][0] + cost[i][0]
    temp2 = dp[i-1][1] + cost[i][0] + cost[i][2]
    dp[i][0] = min(temp1, temp2)
    temp3 = dp[i-1][1] + cost[i][1]
    temp4 = dp[i-1][0] + cost[i][1] + cost[i][2]
    dp[i][1] = min(temp3, temp4)

min_cost = min(dp[tree_num-1][0], dp[tree_num-1][1])
print(min_cost)