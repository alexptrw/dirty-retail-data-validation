def customer_id_fix(df):
    try:
        df["Customer ID"] = df["Customer ID"].apply(lambda x: int(str(x).split("_")[1]))
    except Exception as e:
        print(e)

    return df