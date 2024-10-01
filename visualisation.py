import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = 'C:/Users/Marco Luis/Documents/PROJET SOCCER/top5-players.csv'
data = pd.read_csv(file_path)

# Nombre de joueurs par position
position_count = data['Pos'].value_counts()

# Nombre de joueurs par nation
nation_count = data['Nation'].value_counts()

# Création des visualisations
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Visualisation des positions
position_count.plot(kind='bar', ax=axes[0], color='skyblue')
axes[0].set_title('Nombre de joueurs par position')
axes[0].set_xlabel('Position')
axes[0].set_ylabel('Nombre de joueurs')

# Visualisation des nations
nation_count.plot(kind='bar', ax=axes[1], color='lightgreen')
axes[1].set_title('Nombre de joueurs par nation')
axes[1].set_xlabel('Nation')
axes[1].set_ylabel('Nombre de joueurs')

plt.tight_layout()
plt.show()
