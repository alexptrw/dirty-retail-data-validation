def customer_id_fix(df):
    df["Customer ID"] = df["Customer ID"].apply(lambda x: int(str(x).split("_")[1]))
    return df