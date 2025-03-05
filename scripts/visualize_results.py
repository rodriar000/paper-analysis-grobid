import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Cargar los datos del CSV
df = pd.read_csv("results/resultados.csv")

# 📌 1️⃣ Generar la nube de palabras a partir del Resumen
text = " ".join(str(resumen) for resumen in df["Resumen"].dropna())

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de Palabras - Resúmenes de Artículos")
plt.savefig("results/wordcloud.png")
plt.show()

# 📌 2️⃣ Gráfico de barras con el número de figuras por artículo
plt.figure(figsize=(8,5))
plt.bar(df["PDF"], df["Número de Figuras"], color="skyblue")
plt.xlabel("Artículo")
plt.ylabel("Número de Figuras")
plt.xticks(rotation=45)
plt.title("Número de Figuras por Artículo")
plt.savefig("results/figures_per_article.png")
plt.show()

# 📌 3️⃣ Mostrar los enlaces extraídos
print("\n📌 Enlaces extraídos de los artículos:")
for index, row in df.iterrows():
    if isinstance(row["Enlaces"], str) and row["Enlaces"].strip():
        print(f"- {row['PDF']}: {row['Enlaces']}")

