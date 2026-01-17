from circuit_simulator.core.transient import TransientSolver

def test_rc_charging():
    circuit = {
        "nodes": ["GND","N1"],
        "connections": [("N1","GND")],
        "components": [
            {"name":"V1","type":"DC_SOURCE","n1":"N1","n2":"GND","value":5},
            {"name":"R1","type":"RESISTOR","n1":"N1","n2":"GND","value":1000},
            {"name":"C1","type":"CAPACITOR","n1":"N1","n2":"GND","value":1e-6},
        ]
    }

    solver = TransientSolver(circuit, t_stop=0.01, dt=1e-5)
    t, v = solver.solve()

    assert len(t) > 0
    assert max(v) <= 5.0
