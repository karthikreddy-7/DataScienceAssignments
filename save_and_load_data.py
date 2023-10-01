# In your main script
from data_manager import DataManager
import json
import time as t

# Create a DataManager instance and perform data operations (loading, filtering, sorting)
df = DataManager()
# Loading data from a CSV file
df.load_data("./dataset.csv")
t.sleep(2000)
# Sorting data based on a column name
df.sort_data("StrengthFactor")
t.sleep(2000)
# Filtering data based on a condition
df.filter_data("SoldFlag", "1")

data = df.getData()


# Save the data to a JSON file
def save_data_to_json(data, json_file):
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


save_data_to_json(data, "filtered_and_sorted_data.json")
