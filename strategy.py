

def calculate_signal(df):
    df['price_vs_cost'] = (df['price'] - df['avg_cost']) / df['avg_cost'] * 100
    df["within_5pct"] = (df["price_vs_cost"] > -5) &(df["price_vs_cost"] < 5)
    df["is_reduce"] = df["holder_count"].shift(1) - df["holder_count"] > 0
    df["broker_appeared"] = (df["broker_id"] == "元大").astype(int)
    df["continuous_3"] = df["broker_appeared"].rolling(3).sum()
    df["enter_signal"] = (df["within_5pct"]) & (df["is_reduce"]) &(df["continuous_3"] == 3)
    return df
