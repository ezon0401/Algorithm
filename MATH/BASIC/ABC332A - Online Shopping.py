'''
ABC332A - Online Shopping (https://atcoder.jp/contests/abc332/tasks/abc332_a)

There are N products in the online shop. The quantity and price of products Takahashi will buy is given. 
The shipping fee is free if the price of the products purchased is S yen or above, and K yen otherwise.
Calculate the amount he will pay.
'''

import sys


# 1. TO GET THE INPUT

product_count, min_for_free_shipping, shipping_fee = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

total_price = 0
for product in range(product_count):
    price, quantity = map(int, sys.stdin.readline().split())
    total_price += price * quantity
    
if total_price < min_for_free_shipping:
    total_price += shipping_fee

print(total_price)