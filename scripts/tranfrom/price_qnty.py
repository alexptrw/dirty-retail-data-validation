def price_qty_spend(df):
    df["computed_values"] = False

    mask_price = (pd.isna(df["Price Per Unit"])) & (df["Quantity"].notna()) & (df["Total Spent"].notna())
    df.loc[mask_price, "Price Per Unit"] = df.loc[mask_price, "Total Spent"] / df.loc[mask_price, "Quantity"]
    df.loc[mask_price, "computed_values"] = True
    
    mask_total = (pd.isna(df["Total Spent"])) & (df["Price Per Unit"].notna()) & (df["Quantity"].notna())
    df.loc[mask_total, "Total Spent"] = df.loc[mask_total, "Price Per Unit"] * df.loc[mask_total, "Quantity"]
    df.loc[mask_total, "computed_values"] = True
    
    mask_qty = (pd.isna(df["Quantity"])) & (df["Price Per Unit"].notna()) & (df["Total Spent"].notna()) & (df["Price Per Unit"] != 0)
    df.loc[mask_qty, "Quantity"] = df.loc[mask_qty, "Total Spent"] / df.loc[mask_qty, "Price Per Unit"]
    df.loc[mask_qty, "computed_values"] = True
    
    return df