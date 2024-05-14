#!/usr/bin/python3
import time

isWinner = __import__('0-prime_game').isWinner

t1 = time.perf_counter()
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

# print("Winner: {}".format(isWinner(5, [4, 5, 1])))

print(time.perf_counter() - t1)
