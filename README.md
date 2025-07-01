# 📊 Project: Data Quality & Validation on Dirty Retail Sales Data

# 🔍 Step one EDA
Data Source:
        https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning
Started by diving into the data to understand the beast:

    - Checked data types, columns, and null values
    - Spotted high and low cardinality features
    - Got familiar with the structure and quirks of the dataset
Key discoveries:
    - “Quantity” needs to be converted from float to int
    - Dates and boolean columns need proper formatting
    - Average number of nulls across the dataset — not tiny, but manageable. Most nulls cluster in numeric fields that are related.

This groundwork shaped the plan for upcoming transformations and data organization.
Bonus: Took a stab at visualization (one of my first tries!) to quickly spot weird numeric values and outliers.