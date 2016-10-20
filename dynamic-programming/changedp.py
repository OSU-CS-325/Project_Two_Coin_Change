#!/usr/bin/python3

def changedp(coinArray, change):
  min_coins_used = [0] * (change + 1)
  min_coins_count = [0] * (change + 1)

  for c in range(change + 1):
    coin_count = c
    latest_coin = 1
    for i in [coin_val for coin_val in coinArray if coin_val <= c]:
      if min_coins_count[c - i] + 1 < coin_count:
        coin_count = min_coins_count[c - i] + 1
        latest_coin = i
    min_coins_count[c] = coin_count
    min_coins_used[c] = latest_coin

  min_count = min_coins_count[change]
  min_used = []
  for each in coinArray:
    min_used.append(0)
  change_iter = change
  while change_iter > 0:
    coin = min_coins_used[change_iter]
    k = 0
    for j in coinArray:
      if coin == j:
        min_used[k] += 1
      k += 1

    change_iter = change_iter - coin

  return min_count, min_used

print(changedp([1, 3, 4], 11))
