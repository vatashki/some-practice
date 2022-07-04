change = float(input())

change = int(change * 100)

coin_count = 0
coin_count += change // 200
change %= 200
coin_count += change // 100
change %= 100
coin_count += change // 50
change %= 50
coin_count += change // 20
change %= 20
coin_count += change // 10
change %= 10
coin_count += change // 5
change %= 5
coin_count += change // 2
change %= 2
coin_count += change // 1
change %= 1

print(coin_count)