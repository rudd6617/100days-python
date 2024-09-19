import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240913.csv")
gray_sqirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_sqirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_sqirrels = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_sqirrels)
print(red_sqirrels)
print(black_sqirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sqirrels, red_sqirrels, black_sqirrels],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
