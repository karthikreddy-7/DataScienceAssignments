# In your main script
from data_manager import DataManager
import json
import pickle

# Create a DataManager instance and perform data operations (loading, filtering, sorting)
df = DataManager()
# Loading data from a CSV file
df.load_data("./dataset.csv")
# Filtering data based on a condition
df.filter_data("SoldFlag", "1")
# Sorting data based on a column name
df.sort_data("StrengthFactor")
data = df.getData()


# Save the data to a JSON file
def save_data_to_json(data, json_file):
    header = data[0]
    data = data[1:]
    json_data = []
    for row in data:
        row_dict = {}
        for i, value in enumerate(row):
            header_name = header[i]
            row_dict[header_name] = value
        json_data.append(row_dict)

    with open(json_file, "w") as file:
        json.dump(json_data, file, indent=4)


save_data_to_json(data, "filtered_and_sorted_data.json")


# loading and saving the data using pickle module:
# saving
pickle_file = "filtered_and_sorted_data.pkl"
file = open(pickle_file, "wb")
pickle.dump(data, file)
# loading
file2 = open(pickle_file, "rb")
pickledata = pickle.load(file2)
print(f"Data loaded using Pickle is : {pickledata}")
