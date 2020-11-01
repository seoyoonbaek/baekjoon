N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), str(name)))

members.sort(key = lambda mem_age : (mem_age[0]))

for member in members:
    print("{0} {1}".format(member[0], member[1]))