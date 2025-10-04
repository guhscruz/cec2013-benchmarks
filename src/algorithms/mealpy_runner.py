from src.benchmarks.function_factory import ProblemFactory
from mealpy import FloatVar, SHADE

factory = ProblemFactory(ndim=30)
objective, bounds = factory.get_problem(fid=1)

problem_dict = {
    "fit_func": objective,
    "lb": bounds[0].tolist(),
    "ub": bounds[1].tolist(),
    "minmax": "min",
}

model = SHADE.OriginalSHADE(epoch=100, pop_size=30, wf=0.9)
best = model.solve(problem_dict)
print("Best solution (mealpy):", best.solution, best.target.fitness)