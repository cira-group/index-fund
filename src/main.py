#!/usr/bin/env python3
import cira
import random
import time

"""
A super simpel index fund, that buy and sells random stocks 
"""

__author__ = "Axel Gard"
__version__ = "0.1.0"
__license__ = "MIT"

cira.alpaca.KEY_FILE = "../test_key.json"

portfolio = cira.Portfolio()
exchange = cira.Exchange()


def main():
    qty = 1 # choose how many stocks should be handled in one session 
    while exchange.is_open:
        for stk in random.choices(exchange.stocks, k=qty):
            stk.buy(1)
        for stk in random.choices(portfolio.owned_stocks, k=qty):
            stk.sell(1)
        time.sleep(60*30) # 30 min timer 

if __name__ == "__main__":
    main()