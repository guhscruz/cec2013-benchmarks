from src.algorithms.mealpy_runner import run_shade
import json
import numpy as np
import os


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

solution = run_shade(1, 30, 100, 30, 0.9)

def save_json(solution):

    dictionary = {"id": solution[0]["id"],
                "seed": solution[0]["seed"],
                "lb": solution[0].get("lb", None),
                "ub": solution[0].get("ub", None),
                "best_solution": solution[0]["best_solution"],
                "best_fitness": solution[0]["best_fitness"],
                "history": solution[0]["history"],
                }
    
    id = dictionary["id"]
    seed = dictionary["seed"]

    if not os.path.exists(os.path.join(os.getcwd(), "data/mealpy-shade")):
        os.mkdir("data/mealpy-shade")

    if not os.path.exists(os.path.join(os.getcwd(), f"data/mealpy-shade/function{id}")):
        os.mkdir(f"data/mealpy-shade/function{id}")


    with open(f"data/mealpy-shade/function{id}/function_{id}_seed_{seed}.json", "w") as fp:
        json.dump(dictionary, fp, indent=4, cls=NumpyEncoder)

save_json(solution=solution)