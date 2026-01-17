import pytest
from circuit_simulator.core.dc_analysis import DCSolver

def test_simple_voltage_divider():
    circuit = {
        "nodes": ["GND", "N1", "N2"],
        "connections": [("N2","N1"),("N1","GND")],
        "components": [
            {"name":"V1","type":"DC_SOURCE","n1":"N2","n2":"GND","value":10},
            {"name":"R1","type":"RESISTOR","n1":"N2","n2":"N1","value":1000},
            {"name":"R2","type":"RESISTOR","n1":"N1","n2":"GND","value":1000},
        ]
    }

    solver = DCSolver(circuit)
    result = solver.solve()

    assert pytest.approx(result["N1"], 0.01) == 5.0
