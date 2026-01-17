from scripting.api import CircuitAPI

def voltage_divider_example():
    api = CircuitAPI()

    # Nodes
    api.add_node("GND")
    api.add_node("N1")
    api.add_node("N2")

    # Connections
    api.connect("GND", "N1")
    api.connect("N1", "N2")

    # Components
    api.add_component("V1", "DC_SOURCE", "N2", "GND", 12.0)
    api.add_component("R1", "RESISTOR", "N2", "N1", 1000)
    api.add_component("R2", "RESISTOR", "N1", "GND", 2000)

    # Run DC analysis
    result = api.run_dc()
    print("🔌 DC Result:", result)


def rlc_transient_example():
    api = CircuitAPI()

    api.add_node("GND")
    api.add_node("N1")

    api.connect("GND", "N1")

    api.add_component("V1", "DC_SOURCE", "N1", "GND", 10)
    api.add_component("R1", "RESISTOR", "N1", "GND", 100)
    api.add_component("C1", "CAPACITOR", "N1", "GND", 1e-6)

    time, voltage = api.run_transient(t_stop=0.01, dt=1e-5)

    print("⏱ Time samples:", time[:10])
    print("📈 Voltage samples:", voltage[:10])


if __name__ == "__main__":
    print("▶ Running Voltage Divider Example")
    voltage_divider_example()

    print("\n▶ Running RLC Transient Example")
    rlc_transient_example()
