import pandas as pd

file_path = 'top5-players'
data = pd.read_csv(f"{file_path}.csv")

data_cleaned = data.drop_duplicates()

data_cleaned = data_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data_cleaned.drop(['Rk'], axis=1, inplace=True)

data_cleaned = data_cleaned.dropna()

def remove_outliers(df, column_name):
    # Calculer l'écart-type de la colonne
    std_dev = df[column_name].std()
    
    # Filtrer les lignes où la valeur est entre -écart-type et +écart-type
    filtered_df = df[(df[column_name] >= -std_dev) & (df[column_name] <= std_dev)]
    
    return filtered_df


check_column=["G-PK", "G+A", "Ast"]
for column in check_column:
    data_cleaned = remove_outliers(data_cleaned, column)

data_cleaned.to_csv(f"{file_path}-cleaned.csv", index=False)
