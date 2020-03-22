# Baekjoon Algorithm No.5543
# Input: 햄버거 가격과 음료수 가격
# Output: 조합 중 가장 적은 가격

import sys

burgers = []
beverages = []

for i in range(0, 3):
    burger = sys.stdin.readline()
    burger = int(burger)
    burgers.append(burger)
    
for j in range(0, 2):
    beverage = sys.stdin.readline()
    beverage = int(beverage)
    beverages.append(beverage)

prices = []

for k in burgers:
    for l in beverages:
        price = k + l - 50
        prices.append(price)

prices.sort()
print(prices[0])