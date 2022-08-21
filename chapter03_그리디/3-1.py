n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
		count += n // coin # // 는 n/coin에서 몫을 구함
		n %= coin # % 는 나머지

print(count)