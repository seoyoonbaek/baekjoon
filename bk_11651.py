n = int(input())

coor_list = []

for i in range(n):
    x, y = map(int, input().split())
    coor_list.append([x, y])

coor_list.sort(key = lambda x: (x[1], x[0]))

for i in coor_list:
    print('{0} {1}'.format(i[0], i[1]))