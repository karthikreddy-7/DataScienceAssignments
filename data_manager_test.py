from data_manager import DataManager

# Create a DataManager instance
df = DataManager()
# Load data from a CSV file
df.load_data("./dataset.csv")
# Display data in a formatted table
df.display_data()
# Filter data based on a condition
df.filter_data("SoldFlag", "1")
# Sort data based on a column name
df.sort_data("StrengthFactor")
# Display the filtered data
# df.display_data()
