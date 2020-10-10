n, m = map(int, input().split())

adjs = [[0] for _ in range(n+1)]
visited = [0]*(n+1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adjs[x].append(y) 
    adjs[y].append(x) 

def dfs(v, adjs):
    visited[v] = 1
    for i in adjs[v]:
        if visited[i] == 0:
            dfs(i, adjs)

for i in range(1, n+1):
    if (visited[i]==0):
        count += 1
        dfs(i, adjs)
       

print(count)