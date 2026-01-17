import pytest
from circuit_simulator.core.ac_analysis import ACSolver

def test_ac_rl_circuit():
    circuit = {
        "nodes": ["GND", "N1"],
        "connections": [("N1","GND")],
        "components": [
            {"name":"V1","type":"AC_SOURCE","n1":"N1","n2":"GND","value":1},
            {"name":"R1","type":"RESISTOR","n1":"N1","n2":"GND","value":100},
        ]
    }

    solver = ACSolver(circuit, frequency=1000)
    result = solver.solve()

    assert "magnitude" in result
    assert "phase" in result
