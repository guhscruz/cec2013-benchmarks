from src.benchmarks.function_factory import ProblemFactory
from mealpy import FloatVar, SHADE
import numpy as np
import random
import time

def run_shade(fid, ndim, epoch, pop_size, wf, seed):
    factory = ProblemFactory(ndim=ndim)
    objective, bounds = factory.get_problem(fid=fid)

    lb, ub = bounds
    problem_dict = {
        "obj_func": objective,
        "bounds": FloatVar(lb=lb, ub=ub, name="delta"),
        "minmax": "min",
    }

    results = []

    np.random.seed(seed)
    random.seed(seed)

    inicial_time = time.time()

    model = SHADE.OriginalSHADE(epoch=epoch, pop_size=pop_size, wf=wf)
    best = model.solve(problem_dict, seed=seed)

    best_solution = best.solution
    best_fitness = best.target.fitness

    final_time = time.time()
    execution_time = f"{final_time - inicial_time:.2f}"

    history = model.history.list_global_best_fit 

    results.append({"id": fid,
                    "seed": seed,
                    "lb": lb,
                    "ub": ub,
                    "best_solution": best_solution,
                    "best_fitness": best_fitness,
                    "history": history,
                    "time_seconds": execution_time})

    return results
