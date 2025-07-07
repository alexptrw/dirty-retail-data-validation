import pandas as pd

def item_id_fix(df):
   
   for row in df.itertuples():
        try:
            if pd.isna(row.Item) or row.Item == 'Na':
                df.at[row.Index, 'Item'] = str(row.Item).split("_")[1]
        except Exception as e:
            print(f"Error processing row {row.Item} {row.Index}: {e}")
        return df
    # try:
    #     df["Item"] = df["Item"].apply(lambda x: (str(x).split("_")[1] if (not pd.isna(x) and x != 'Na') else x))
    
    # except Exception as e:
    #     print(e)
    