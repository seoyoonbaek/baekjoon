N = int(input())
students = []

for _ in range(N):
    name, kor, eng, math = input().split()
    students.append((str(name), int(kor), int(eng), int(math)))

students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in students:
    print("{0}".format(student[0]))