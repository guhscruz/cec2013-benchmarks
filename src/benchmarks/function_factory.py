from opfunu.cec_based import cec2013
import numpy as np

class ProblemFactory:
    def __init__(self, ndim=30):
        self.ndim = ndim

    def get_problem(self, fid):
        function = getattr(cec2013, f'F{fid}2013')
        f = function(ndim=self.ndim)
        
        def objective(x):
            return f.evaluate(np.array(x))
        
        lb, ub = -100, 100
        bounds = (np.full(self.ndim, lb), np.full(self.ndim, ub))

        return objective, bounds