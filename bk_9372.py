T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a] = b
        graph[b] = a
    
    print(N-1)