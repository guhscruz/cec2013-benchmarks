from src.utils.stats_parser import JsonParser
import matplotlib.pyplot as plt
import numpy as np

parser = JsonParser(path_dir="data/mealpy-shade")

# Função que queremos plotar
func_name = "F1"

# Busca todos os resultados dessa função (as 30 seeds)
results = parser.get_function_results(func_name)

# Extrai os valores de fitness de cada execução
data_mealpy = [r["best_fitness"] for r in results]

# Cria o boxplot com os dados reais
plt.figure(figsize=(6, 5))
plt.boxplot(data_mealpy, patch_artist=True, boxprops=dict(facecolor="#4C72B0", alpha=0.7))
plt.title(f"Boxplot da {func_name} - Mealpy")
plt.ylabel("Fitness")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()