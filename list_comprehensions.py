import pandas as pd

# Given strength factor threshold
strengthfac = int(input("Enter the Strength Factor : "))

# Dataset as a list of dictionaries
data = pd.read_csv("./dataset.csv")

# Create a list of SKU_numbers for products with StrengthFactor greater than the given value
SKUNumbers = [
    sku for sku in data.loc[data["StrengthFactor"] > strengthfac, "SKU_number"]
]
print(f"The list of SKU Numbers where the StrengthFactor is above {strengthfac} is:")
print(SKUNumbers)
