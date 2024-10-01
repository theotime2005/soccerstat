import pandas as pd

# Charger le fichier CSV
file_path = 'top5-players.csv'
data = pd.read_csv(file_path)

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
cleaned_file_path = 'top5-players-cleaned.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Le fichier a été nettoyé et sauvegardé sous {cleaned_file_path}")
