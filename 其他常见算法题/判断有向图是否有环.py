import sys
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True  # 将该节点标记为访问过
        recStack[v] = True

        for neighbour in self.graph[v]:  # 遍历所有该节点指向的节点
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False


for line in sys.stdin:
    G = eval(line)

    graph = Graph(len(G))
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == 1:
                graph.addEdge(i, j)
    if graph.isCyclic():
        print(1)
    else:
        print(0)
