h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for z in range(60):

            time = str(i) + str(j) + str(z)
            if time.count('3') > 0: # count 함수 사용
                count += 1

print(count)