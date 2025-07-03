def item_id_fix(df):
    df["Item"] = df["Item"].apply(lambda x: (str(x).split("_")[1] if (not pd.isna(x) and x != 'Na') else x))
    return df