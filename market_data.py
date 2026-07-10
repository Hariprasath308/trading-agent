import yfinance as yf

def get_data(symbol):
    df = yf.download(
        symbol,
        period="3mo",
        interval="1d",
        progress=False,
        auto_adjust=True,
        group_by="column"
    )

    # Flatten MultiIndex columns if present
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    if df.empty:
        raise Exception(f"No data found for {symbol}")

    return df