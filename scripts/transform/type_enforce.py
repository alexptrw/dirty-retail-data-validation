import pandas as pd
def type_enforce(df):
    df["Transaction ID"] = df["Transaction ID"].astype("string")
    df["Customer ID"] = df["Customer ID"].astype("string")
    df["Category"] = df["Category"].astype("string")
    df["Item"] = df["Item"].astype("string")
    df["Price Per Unit"] = df["Price Per Unit"].astype("float")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").astype("Int64")
    df["Total Spent"] = df["Total Spent"].astype("float")
    df["Payment Method"] = df["Payment Method"].astype("string")
    df["Location"] = df["Location"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce").astype("datetime64[ns]")
    df["Discount Applied"] = df["Discount Applied"].astype(str).str.lower().map({'true': True, 'false': False, 'nan': None})
    return df