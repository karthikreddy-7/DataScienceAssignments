"""
Creating a Python class named Product in its own file. This class should have
attributes relevant to the dataset (e.g., SKU_number , SoldFlag , StrengthFactor ,
etc.).
"""


class Product:
    def __init__(self, csv_line):
        # Spliting the CSV line into a list of values
        values = csv_line.strip().split(",")

        # Assigning attributes based on the position of values in the CSV line
        self.SKU_number = int(values[0])
        self.SoldFlag = float(values[1])
        self.ReleaseNumber = int(values[2])
        self.New_Release_Flag = int(values[3])
        self.StrengthFactor = float(values[4])
        self.PriceReg = float(values[5])
        self.ReleaseYear = int(values[6])
        self.ItemCount = int(values[7])
        self.LowUserPrice = float(values[8])
        self.LowNetPrice = float(values[9])

    def __str__(self):
        # Customizing the string representation of the object for easier debugging
        return f"SKU: {self.SKU_number}, SoldFlag: {self.SoldFlag}, StrengthFactor: {self.StrengthFactor}, ..."


# Example
csv_data = "123,0.0,15,1,682743.0,44.99,2015,8,28.97,31.84"
product = Product(csv_data)

# Accessing the variables of the object
print(product.SKU_number)  # Output: 123
print(product.SoldFlag)  # Output: 0.0
