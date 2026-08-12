from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from market_data import get_data
from strategy import moving_average_strategy
from config import STOCKS, SHORT_MA, LONG_MA

app = FastAPI(title="TradeBot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "TradeBot Backend is running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/stocks")
def stocks():
    results = []

    for stock in STOCKS:
        try:
            df = get_data(stock)

            if df is None or df.empty:
                results.append({
                    "stock": stock,
                    "price": None,
                    "sma20": None,
                    "sma50": None,
                    "signal": "NO DATA"
                })
                continue

            signal = moving_average_strategy(
                df.copy(),
                SHORT_MA,
                LONG_MA
            )

            price = float(df["Close"].iloc[-1])
            sma20 = float(df["Close"].rolling(SHORT_MA).mean().iloc[-1])
            sma50 = float(df["Close"].rolling(LONG_MA).mean().iloc[-1])

            results.append({
                "stock": stock,
                "price": round(price, 2),
                "sma20": round(sma20, 2),
                "sma50": round(sma50, 2),
                "signal": signal
            })

        except Exception as e:
            results.append({
                "stock": stock,
                "price": None,
                "sma20": None,
                "sma50": None,
                "signal": "ERROR"
            })

    return {"stocks": results}

@app.post("/api/scan")
def scan():
    return stocks()
