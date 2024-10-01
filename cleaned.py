import pandas as pd

# Charger le fichier CSV
file_path = 'top5-players'
data = pd.read_csv(f"{file_path}.csv")

# Supprimer les doublons
data_cleaned = data.drop_duplicates()

# Calculer la moyenne et l'écart type pour les colonnes numériques
numeric_cols = data_cleaned.select_dtypes(include=['float64', 'int64']).columns
mean = data_cleaned[numeric_cols].mean()
std = data_cleaned[numeric_cols].std()

# Définir la règle pour les valeurs aberrantes (3 écarts types de la moyenne)
outliers = (data_cleaned[numeric_cols] < (mean - 3 * std)) | (data_cleaned[numeric_cols] > (mean + 3 * std))

# Filtrer les lignes sans valeurs aberrantes
data_cleaned = data_cleaned[~outliers.any(axis=1)]

# Sauvegarder le fichier nettoyé
data_cleaned.to_csv(f"{file_path}-cleaned.csv")

print(f"Le fichier a été nettoyé et sauvegardé sous {file_path}-cleaned.csv")
