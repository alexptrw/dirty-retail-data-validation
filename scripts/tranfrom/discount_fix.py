def discount_fix(df):
    df["Discount Applied"] = df["Discount Applied"].apply(lambda x: False if x is None else x)
    return df