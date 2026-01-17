from circuit_simulator.core.frequency_analysis import FrequencyAnalyzer

def test_frequency_sweep():
    circuit = {
        "nodes": ["GND","N1"],
        "connections": [("N1","GND")],
        "components": [
            {"name":"R1","type":"RESISTOR","n1":"N1","n2":"GND","value":1000},
            {"name":"C1","type":"CAPACITOR","n1":"N1","n2":"GND","value":1e-6},
        ]
    }

    analyzer = FrequencyAnalyzer(circuit)
    freq, gain = analyzer.sweep(10, 1e6)

    assert len(freq) == len(gain)
