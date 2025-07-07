import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))


from transform.type_enforce import type_enforce
from transform.customer_id import customer_id_fix
from transform.discount_fix import discount_fix
from transform.empty_fill import fill_empty_items
from transform.item_id import item_id_fix
from transform.price_qnty import price_qty_spend


def main():
    print("Loading Data...\n")
    df = pd.read_csv(r"../data/raw/retail_store_sales.csv")
    print(f"Data loaded: {len(df)} rows\n")

    print("==================================\n Applying tranformations\n")
    df = type_enforce(df)
    print("==================================\n Fixing customer id \n")
    df = customer_id_fix(df)
    print("==================================\n Fixing item id\n")
    df = item_id_fix(df)
    print("==================================\n Fixing price, quantity, total inconsistencies where possbile\n")
    df = item_id_fix(df)
    print("==================================\n Fixing discount inconsisteny\n")
    df = discount_fix(df)
    print("==================================\n Fixing empty fields\n")
    df = fill_empty_items(df)
    print(" ***\n Tranformation completed")




if __name__ == "__main__":
    cleaned_df = main()