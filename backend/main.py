from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from market_data import get_data
from strategy import moving_average_strategy
from config import STOCKS, SHORT_MA, LONG_MA

app = FastAPI(title="TradeBot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
