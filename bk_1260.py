import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
adjs = [[0]*(n+1) for i in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adjs[a][b] = 1
    adjs[b][a] = 1


def dfs(v, lines):
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if (lines[v][i] == 1) and (visited_dfs[i] == 0):
            dfs(i, lines)

def bfs(v, lines):
    visited_bfs[v] = 1
    queue = deque([v])
    while queue:
        curr = queue.popleft()
        visited_bfs[curr] = 1
        print(curr, end=" ")
        for i in range(1, n+1):
            if (lines[curr][i] == 1) and (visited_bfs[i] == 0) :
                queue.append(i)
                


dfs(v, adjs)  
print()
bfs(v, adjs)

