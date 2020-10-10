import sys

n = int(input())

sort_list = [0] * n

for i in range(n):
    sort_list[i] = int(sys.stdin.readline())


for i in sorted(sort_list):
    print(i)
