class DataManager:
    def __init__(self):
        self.data = []

    def load_data(self, csv_file):
        try:
            with open(csv_file, "r") as file:
                header = file.readline()
                for line in file:
                    self.data.append(line.strip().split(","))
            print(f"Data has been loaded from {csv_file}")
        except FileNotFoundError:
            print(f"File '{csv_file}' not found.")
        except Exception as e:
            print(f"An error occurred while loading data: {str(e)}")

    def display_data(self):
        if not self.data:
            print("No data to display.")
            return

        header = self.data[0]
        data = self.data[1:]
        max_lengths = [len(max(col, key=len)) for col in zip(*self.data)]

        print(" | ".join(f"{header[i]:<{max_lengths[i]}}" for i in range(len(header))))
        print("-" * sum(max_lengths))
        for row in data:
            print(" | ".join(f"{row[i]:<{max_lengths[i]}}" for i in range(len(row))))

    def sort_data(self, column_name):
        if not self.data:
            print("No data to sort.")
            return

        header = self.data[0]
        data = self.data[1:]

        if column_name not in header:
            print(f"Column '{column_name}' not found.")
            return

        column_index = header.index(column_name)
        data.sort(key=lambda x: x[column_index])
        self.data = [header] + data
        print(f"Data sorted by '{column_name}'")

    def filter_data(self, column_name, condition):
        if not self.data:
            print("No data to filter.")
            return

        header = self.data[0]
        data = self.data[1:]

        if column_name not in header:
            print(f"Column '{column_name}' not found.")
            return

        column_index = header.index(column_name)
        filtered_data = [header]
        for row in data:
            if row[column_index] == condition:
                filtered_data.append(row)

        self.data = filtered_data
        print(f"Data filtered by '{column_name}' with condition '{condition}'")

    def getData(self):
        if not self.data:
            print("No data available.")
            return None
        return self.data


# Testing the class and its functions

# Creating a DataManager instance
data_manager = DataManager()

# Loading data from a CSV file
data_manager.load_data("./dataset.csv")

# Displaying data in a formatted table
data_manager.display_data()

# Sorting data based on a column name
data_manager.sort_data("StrengthFactor")

# Filtering data based on a condition
data_manager.filter_data("SoldFlag", "1")

# Displaying the filtered data
data_manager.display_data()
