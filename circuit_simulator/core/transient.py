import numpy as np
from scipy.integrate import solve_ivp

def rc_response(R, C, V, t_end=1):
    def eq(t, v):
        return (V - v) / (R * C)

    t = np.linspace(0, t_end, 500)
    sol = solve_ivp(eq, [0, t_end], [0], t_eval=t)
    return sol.t, sol.y[0]
