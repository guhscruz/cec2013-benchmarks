'''
- Percorrer todas as pastas dentro de data/mealpy-shade
- Para cada função, percorrer todos os json
- Pegar todos os valores importantes
- Fazer todos os calculos necessários
- Retonar valores
'''
import numpy as np
import os
import json

class JsonParser:
    def __init__(self, path_dir="data"):
        self.path_dir = path_dir

    def get_function_results(self, func_name: str):
        json_datas = []
        path = f"{self.path_dir}/{func_name}"

        for file_name in os.listdir(path):
            function_path = os.path.join(path, file_name)
            if os.path.isfile(function_path):
                with open(function_path, 'r', encoding="utf-8") as file:
                    try:
                        data = json.load(file)
                        json_datas.append(data)
                    except json.JSONDecodeError as e:
                        print(f"Erro ao ler {file_name}: {e}")

        return json_datas
    
    def summarize_function(self, func_name: str):
        results = self.get_function_results(func_name)

        best_fitness_values = [l["best_fitness"] for l in results]

        values = {"function": func_name,
                  "mean": np.mean(best_fitness_values),
                  "std": np.std(best_fitness_values),
                  "min": min(best_fitness_values),
                  "max": max(best_fitness_values),
                  "median": np.median(best_fitness_values)}
        
        return values

    def summarize_all(self):
        summaries = []
        for func_name in os.listdir(self.path_dir):
            path_name = os.path.join(self.path_dir, func_name)
            if os.path.isdir(path_name):
                resolution = self.summarize_function(func_name)
                summaries.append(resolution)

        return summaries
        
parser = JsonParser(path_dir="data/mealpy-shade")

results = parser.summarize_all()
print(results)