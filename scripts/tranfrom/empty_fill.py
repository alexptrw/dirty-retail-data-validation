def fill_empty_items(df):
    df["Item"] = df["Item"].fillna("Unknown Item")
    return df