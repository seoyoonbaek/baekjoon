import sys

n = int(input())

index_list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    index_list.append([x, y])

for i in sorted(index_list):
    print("{0} {1}".format(i[0], i[1]))
