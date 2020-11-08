N = int(input())
adjs = []

def dfs(v, adjs, visited):
        visited[v] = True
        curr = adjs[v]
        if visited[curr] == False:
            dfs(curr, adjs, visited)

for i in range(N):
    n = int(input())
    adjs = [0] + map(int, input().split())
    visited = [False for _ in range(n+1)]

    count = 0
            
    for j in range(1, n+1):
        if visited[j] == False:
            dfs(j, adjs, visited)
            count += 1
    
    print(count)

