import numpy as np

# # Take one
# def buy_and_sell_stock_once(prices):
#     daily_profit = list(np.subtract(prices[1:], prices[:-1]))
#     print(daily_profit)
#     max_profit = 0
#     max_profit_so_far = 0
#     for i in daily_profit:
#         max_profit_so_far = max(0, max_profit_so_far + i)
#         max_profit = max(max_profit, max_profit_so_far)
#         print(max_profit_so_far, max_profit)
#     return max_profit

def buy_and_sell_stock_once(prices):
    max_profit, min_so_far = 0.0, float('inf')
    for i in range(len(prices)):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_so_far)
        print(min_so_far, max_profit)
    return max_profit

def main():
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print('The max profit is: {0}'.format(buy_and_sell_stock_once(prices)))

if __name__ == '__main__':
    main()
