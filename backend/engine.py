import time
from .config import STOCKS, SHORT_MA, LONG_MA, TARGET_PERCENT, STOPLOSS_PERCENT, CHECK_INTERVAL, INITIAL_BALANCE
from .market_data import get_data
from .strategy import moving_average_strategy
from .paper_trade import PaperTrader

trader = PaperTrader(INITIAL_BALANCE)

def scan_once():
    print("\n=== TradeBot Scan ===")

    for stock in STOCKS:
        try:
            df = get_data(stock)

            if df is None or len(df) < LONG_MA:
                print(f"{stock}: HOLD - insufficient data")
                continue

            price = float(df["Close"].iloc[-1])
            signal = moving_average_strategy(df, SHORT_MA, LONG_MA)

            print(f"{stock}: {signal} @ {price:.2f}")

            trader.check(
                stock,
                price,
                TARGET_PERCENT,
                STOPLOSS_PERCENT
            )

            if signal == "BUY":
                trader.buy(stock, price)

            elif signal == "SELL":
                trader.sell(stock, price, "MA crossover SELL")

        except Exception as e:
            print(f"{stock}: Error - {e}")

def run():
    print("TradeBot Engine Started - PAPER TRADING ONLY")

    while True:
        scan_once()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run()
