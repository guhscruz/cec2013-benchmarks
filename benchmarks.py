from opfunu.cec_based import cec2017
f3 = cec2017.F32017(ndim=30)

from mealpy import GA, FloatVar

problem = {
    "obj_func": f3.evaluate,
    "bounds": FloatVar(lb=f3.lb, ub=f3.ub),
    "minmax": "min",
}
model = GA.BaseGA(epoch=100, pop_size=50)
gbest = model.solve(problem)
print(f"Solution: {gbest.solution}, Fit: {gbest.target.fitness}")