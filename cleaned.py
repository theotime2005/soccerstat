import pandas as pd

file_path = 'top5-players'
data = pd.read_csv(f"{file_path}.csv")

data_cleaned = data.drop_duplicates()

data_cleaned = data_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)

data_cleaned = data_cleaned.dropna()

data_cleaned.to_csv(f"{file_path}-cleaned.csv", index=False)
