from collections import deque

n = int(input())

adjs = [[0]*(n+1) for i in range(n+1)]
visited_bfs = [0]*(n+1)
group = [0]*(n+1)

def bfs(v, lines):
    visited_bfs[v] = 1
    group[v] = 1
    queue = deque([v])
    while queue:
        curr = queue.popleft()
        visited_bfs[curr] = 1
        
        for i in range(1, n+1):
            if (lines[curr][i] == 1) and (visited_bfs[i] == 0):
                visite
                d_bfs[i] = 1
                
                if group[curr] == 1:
                    group[i] = 0
                else:
                    group[i] = 1

                queue.append(i)
            
            if visited_bfs[i] == 1:
                if group[curr]==group[i]:
                    return False
    return True

