import pandas

# Accessing the whole CSV
raw_data = pandas.read_csv("Data_File/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# Squirrel count
gray_Squirrels = len(raw_data[raw_data["Primary Fur Color"] == "Gray"])
cinnamon_Squirrels = len(raw_data[raw_data["Primary Fur Color"] == "Cinnamon"])
black_Squirrels = len(raw_data[raw_data["Primary Fur Color"] == "Black"])

# Creating a dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_Squirrels, cinnamon_Squirrels, black_Squirrels],
}

# DataFrame
data_Frame = pandas.DataFrame(data_dict)

# Converting to CSV
data_Frame.to_csv(path_or_buf="Data_File/Modified_CSV.csv")