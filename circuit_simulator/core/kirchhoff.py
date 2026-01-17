import numpy as np

def solve_kcl(G, I):
    """
    Solve nodal equations: G * V = I
    G = Conductance matrix
    I = Current source vector
    """
    return np.linalg.solve(G, I)
