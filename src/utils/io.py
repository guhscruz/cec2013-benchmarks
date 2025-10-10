from src.algorithms.mealpy_runner import run_shade
import json
import numpy as np
import os


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def save_json(solution):

    dictionary = {"id": solution[0]["id"],
                "seed": solution[0]["seed"],
                "lb": solution[0].get("lb", None),
                "ub": solution[0].get("ub", None),
                "best_solution": solution[0]["best_solution"],
                "best_fitness": solution[0]["best_fitness"],
                "history": solution[0]["history"],
                "time_seconds": solution[0]["time_seconds"]
                }
    
    id = dictionary["id"]
    seed = dictionary["seed"]

    if not os.path.exists(os.path.join(os.getcwd(), "data/mealpy-shade")):
        os.mkdir("data/mealpy-shade")

    if not os.path.exists(os.path.join(os.getcwd(), f"data/mealpy-shade/F{id}")):
        os.mkdir(f"data/mealpy-shade/F{id}")


    with open(f"data/mealpy-shade/F{id}/function_{id}_seed_{seed}.json", "w") as fp:
        json.dump(dictionary, fp, indent=4, cls=NumpyEncoder)
