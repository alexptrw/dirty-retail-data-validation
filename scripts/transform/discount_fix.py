def discount_fix(df):
    try:
        df["Discount Applied"] = df["Discount Applied"].apply(lambda x: False if x is None else x)
    except Exception as e:
        print(e)
    return df