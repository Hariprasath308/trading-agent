import yfinance as yf


def get_data(stock):
    try:
        df = yf.download(
            stock,
            period="3mo",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            return None

        # Fix yfinance MultiIndex columns
        if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
            df.columns = df.columns.get_level_values(0)

        required = ["Open", "High", "Low", "Close", "Volume"]

        for column in required:
            if column not in df.columns:
                return None

        return df

    except Exception as e:
        print(f"Market data error for {stock}: {e}")
        return None