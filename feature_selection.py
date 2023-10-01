import pandas as pd
import numpy as np

data = pd.read_csv("./dataset.csv")
# printing the first 5 rows of dataset
print("The dataset is :")
print(data.head())
print("the information of dataset is :")
data.info()
# Removing unused/unneccessary columns
"""
1.Removing 'Order' as it is just a order counter values and has nothing to do with analysis or prediction
2.Removing 'File_Type' as the active count has null values and can be no use while building model
3.Removing 'SKU_number' as it is a unique identifier for each product'
4.Removing 'MarketingType' as it shows two categories of how product is marketed.
5.Removing 'SoldCount' as it shows the count of product sold and not relevant.
"""
data = data.drop(
    ["Order", "File_Type", "SKU_number", "MarketingType", "SoldCount"], axis=1
)
# printing the dataset after droping unneccessary columns
print("modified dataset is :")
print(data.head())

# For Finding the most important columns we can find the correlation between the soldflag and other columns
correlation_matrix = data.corr()
correlation_with_soldflag = (
    correlation_matrix["SoldFlag"].abs().sort_values(ascending=False)
)
print("The correlation values are:")
print(correlation_with_soldflag)
"""
From the output of the we can observe that 

1. 'ItemCount' has the highest correlation factor and plays a key role in prediction.
2. 'StrengthFactor' also helps in playing a key role in prediction

Hence, the 2 most important columns are 'ItemCount' and 'StrengthFactor'.
"""
