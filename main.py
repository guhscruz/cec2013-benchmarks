from src.algorithms.mealpy_runner import run_shade
from src.utils.io import save_json
from src.experiments.parameters import cec2013_params
import numpy as np
import random

for id, params in cec2013_params.items():
    for seed in range(30):
        np.random.seed(seed)
        random.seed(seed)

        results = run_shade(fid=id, 
                            ndim=params["ndim"], 
                            epoch=params["epoch"], 
                            pop_size=params["pop_size"], 
                            wf=params["wf"],
                            seed=seed)
        
        save_json(solution=results)