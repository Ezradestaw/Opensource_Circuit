import numpy as np

def nodal_analysis(nodes, components):
    size = len(nodes)
    G = np.zeros((size, size))
    I = np.zeros(size)

    node_index = {n: i for i, n in enumerate(nodes)}

    for c in components:
        if c["type"] == "resistor":
            n1, n2 = c["nodes"]
            g = 1 / c["value_ohms"]
            i, j = node_index[n1], node_index[n2]
            G[i, i] += g
            G[j, j] += g
            G[i, j] -= g
            G[j, i] -= g

    V = np.linalg.solve(G[1:,1:], I[1:])
    return V
