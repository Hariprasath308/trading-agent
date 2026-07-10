from datetime import datetime

def write_log(message):
    with open("trade_log.txt", "a") as f:
        f.write(f"{datetime.now()} : {message}\n")