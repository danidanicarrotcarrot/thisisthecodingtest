n,m,k = map(int, input().split()) # 공백으로 구분해서 입력받음
num = list(map(int, input().split()))

num.sort() # 리스트 자체를 정렬, 오름차순 # 새롭게 정렬한 리스트를 반환하는 함수는 sorted()
first = num[n-1] # 제일 큰 수
second = num[n-2] # 그 다음 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break # m이 0이라면 반복문 탈출
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)