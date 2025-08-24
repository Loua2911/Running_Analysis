import pandas as pd

# 1️⃣ Lire ton CSV actuel (séparateur point-virgule)
df = pd.read_csv("run2025.csv", sep=';')

# 2️⃣ Vérifier les premières lignes
print(df.head())

# 3️⃣ Réécrire le CSV en utilisant des virgules
df.to_csv("run2025_fixed.csv", index=False)

print("Fichier corrigé : run2025_fixed.csv")
