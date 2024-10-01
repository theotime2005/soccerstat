import pandas as pd

file_path = 'C:/Users/Marco Luis/Documents/PROJET SOCCER/top5-players.csv'
data = pd.read_csv(file_path)

data_cleaned = data.drop_duplicates()

data_cleaned = data_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)

data_cleaned = data_cleaned.dropna()

cleaned_file_path = 'C:/Users/Marco Luis/Documents/PROJET SOCCER/top5-players-cleaned.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Le fichier a été nettoyé et sauvegardé sous {cleaned_file_path}")
