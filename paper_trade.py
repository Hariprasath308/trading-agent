from logger import write_log

class PaperTrader:

    def __init__(self, balance):
        self.balance = balance
        self.position = {}

    def buy(self, stock, price):

        if stock in self.position:
            return

        if self.balance >= price:
            self.position[stock] = price
            self.balance -= price

            print(f"BUY {stock} @ {price}")
            write_log(f"BUY {stock} @ {price}")

    def sell(self, stock, price, reason=""):

        if stock not in self.position:
            return

        buy_price = self.position.pop(stock)
        profit = price - buy_price

        self.balance += price

        print(f"SELL {stock} @ {price}")
        print(f"Profit = {profit:.2f}")
        print(f"Reason : {reason}")

        write_log(
            f"SELL {stock} @ {price} | "
            f"Profit: {profit:.2f} | "
            f"Reason: {reason}"
        )

    def check(self, stock, current_price, target, stoploss):

        if stock not in self.position:
            return

        buy = self.position[stock]

        target_price = buy * (1 + target / 100)
        stop_price = buy * (1 - stoploss / 100)

        if current_price >= target_price:
            print("Target Hit")
            self.sell(stock, current_price, "Target Hit")

        elif current_price <= stop_price:
            print("Stop Loss Hit")
            self.sell(stock, current_price, "Stop Loss Hit")