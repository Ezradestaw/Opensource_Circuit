import numpy as np

def impedance(component, freq):
    w = 2 * np.pi * freq
    if component["type"] == "resistor":
        return component["value_ohms"]
    if component["type"] == "inductor":
        return 1j * w * component["value_henry"]
    if component["type"] == "capacitor":
        return 1 / (1j * w * component["value_farad"])

def series_impedance(components, freq):
    return sum(impedance(c, freq) for c in components)
