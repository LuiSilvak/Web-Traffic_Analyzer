# Analisador de Dados de Tráfego Web

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Dados simulados de tráfego web 
data = {
    "Visitor_ID": range(1, 101),
    "Traffic_Source": [
        "Orgânico", "Direto", "Redes Sociais", "Anúncios", "Direto",
        "Orgânico", "Redes Sociais", "Orgânico", "Anúncios", "Direto"
    ] * 10,
    "Page_Visited": [
        "Home", "Sobre", "Contato", "Produtos", "Blog",
        "Home", "Produtos", "Blog", "Home", "Contato"
    ] * 10,
    "Session_Duration": [120, 45, 300, 180, 60, 90, 240, 180, 30, 75] * 10,
    "Visit_Date": pd.date_range(start="2025-01-01", periods=100, freq="D")

}

# Criando o DataFrame
df = pd.DataFrame(data)

# Análise básica
total_visits = df.shape[0]
avg_session_duration = df["Session_Duration"].mean()
traffic_source_count = df["Traffic_Source"].value_counts()
most_visited_pages = df["Page_Visited"].value_counts()

# Exibindo estatísticas básicas
print(f"Total de visitas: {total_visits}")
print(f"Duração média da sessão: {avg_session_duration:.2f} segundos")
print("\n Origem do Tráfego:")
print(traffic_source_count)
print("\n Páginas mais Visitadas:")
print(most_visited_pages)

# Gráfico de barras - Origem do Tráfego
plt.figure(figsize=(8, 6))
traffic_source_count.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Origem do Tráfego")
plt.xlabel("Fonte")
plt.ylabel("Número de Visitas")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Gráfico de barras - Páginas Mais Visitadas
plt.figure(figsize=(8, 6))
most_visited_pages.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Páginas Mais Visitadas")
plt.xlabel("Página")
plt.ylabel("Número de Visitas")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Análise de duração da sessão por origem
session_by_source = df.groupby("Traffic_Source")["Session_Duration"].mean().sort_values(ascending=False)
print("\n Duração Média da Sessão por Origem do Tráfego:")
print(session_by_source)

# Gráfico de barras - Duração média da sessão por origem
plt.figure(figsize=(8,6))
session_by_source.plot(kind="bar", color="green", edgecolor="black")
plt.title("Duração Média da Sessão por Origem")
plt.xlabel("Origem do Tráfego")
plt.ylabel("Duração Média (segundos)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Gráfico de linhas - Tráfego ao longo do tempo
traffic_over_time = df.groupby("Visit_Date")["Visitor_ID"].count()
plt.figure(figsize=(10, 6))
traffic_over_time.plot(kind="line", marker="o", color="blue")
plt.title("Tráfego ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Número de Visitas")
plt.grid()
plt.show()