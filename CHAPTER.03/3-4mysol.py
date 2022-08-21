# 내 답안
n, k = map(int, input().split())

result = 0

while n >= k:
    while n%k > 0: # 나머지가 0이 아니면(배수 X) -> 1씩 빼기
        n = n - 1
        result += 1
    n = n//k # 나머지가 0이면 -> 나누기
    result += 1

n = n - 1
result += 1
print(result)