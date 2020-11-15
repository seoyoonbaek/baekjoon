N = int(input())

colors = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = colors[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if colors[i][j] != color:
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    check(color)

def check(color):
    global white, blue
    if color == 0:
        white += 1
        return 
    else:
        blue += 1
        return

cut(0, 0, N)
print(white)
print(blue)