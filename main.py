import time
import traceback

from config import *
from market_data import get_data
from strategy import moving_average_strategy
from paper_trade import PaperTrader
from logger import write_log

print("===================================")
print("Trading Agent Started...")
print("===================================")

trader = PaperTrader(INITIAL_BALANCE)

while True:

    for stock in STOCKS:

        try:
            print(f"\nChecking {stock}...")

            df = get_data(stock)

        
            

            signal = moving_average_strategy(
                df,
                SHORT_MA,
                LONG_MA
            )

            price = float(df["Close"].iloc[-1])

            print(f"Price  : {price:.2f}")
            print(f"Signal : {signal}")

            if signal == "BUY":
                trader.buy(stock, price)
                write_log(f"{stock} BUY @ {price}")

            elif signal == "SELL":
                trader.sell(stock, price)
                write_log(f"{stock} SELL @ {price}")

            trader.check(
                stock,
                price,
                TARGET_PERCENT,
                STOPLOSS_PERCENT
            )

        except Exception as e:
            print("\nERROR:")
            traceback.print_exc()
            write_log(str(e))

    print("\nWaiting for next scan...\n")
    time.sleep(CHECK_INTERVAL)