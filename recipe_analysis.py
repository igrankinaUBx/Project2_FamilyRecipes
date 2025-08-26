import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('family_recipes.csv')
ingredients_series = df['ingredients'].str.split(';').explode().str.strip()
counts = ingredients_series.value_counts().head(10)
plt.figure(figsize=(10,5))
counts.plot(kind='bar')
plt.title("Top 10 most frequent ingredients")
plt.xlabel("Ingredient")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
