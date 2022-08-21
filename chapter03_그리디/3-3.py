# min() 함수 이용 답안

n, m = map(int, input().split())

result = 0
# 한줄씩 입력받아서 그 행의 최솟값을 찾기
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value) # result와 min_value 를 비교

print(result)