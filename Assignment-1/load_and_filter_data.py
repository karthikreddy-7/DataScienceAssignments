import pandas as pd
import numpy as np

data = pd.read_csv("./dataset.csv")
"""
Removing the columns identified in Task 1 and writing the new dataset to a new CSV file.
"""
data = data.drop(
    ["Order", "File_Type", "SKU_number", "MarketingType", "SoldCount"], axis=1
)
data.to_csv("modified_data.csv", index=False)
