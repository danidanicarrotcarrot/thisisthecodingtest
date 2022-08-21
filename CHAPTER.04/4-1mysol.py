n = int(input())
x, y = 1, 1
plan = list(input().split())

for i in plan :
    
    if i == 'R': # 오른쪽으로 이동 시 + 1
        y += 1
        if y == n+1 :
            y -= 1 # n+1을 넘어가면 y - 1
    
    if i == 'L':
        y -= 1 # 왼쪽으로 이동 시 y - 1
        if y == 0 :
            y += 1 # 0보다 작아지면 + 1

    if i == 'D':
        x += 1 # 밑으로 이동 시 x + 1
        if y == n+1 :
            y -= 1 # n+1 보다 커지면 - 1

    if i == 'U':
        x -= 1 # 위로 이동 시 x - 1
        if x == 0 :
            x += 1 # 0보다 작아지면 + 1

print(x, y)