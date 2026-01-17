from circuit_simulator.core.dc_analysis import DCSolver
from circuit_simulator.core.ac_analysis import ACSolver
from circuit_simulator.core.transient import TransientSolver
from circuit_simulator.io.file_manager import FileManager
from circuit_simulator.utils.validation import CircuitValidator


class CircuitAPI:
    """
    High-level Python API for programmatic circuit simulation.
    Users can create circuits, run DC/AC/Transient analysis, and export results.
    """

    def __init__(self):
        self.circuit = {
            "nodes": [],
            "connections": [],
            "components": []
        }

    # -------- Circuit Construction -------- #

    def add_node(self, node_name: str):
        if node_name not in self.circuit["nodes"]:
            self.circuit["nodes"].append(node_name)

    def connect(self, node_a: str, node_b: str):
        self.circuit["connections"].append((node_a, node_b))

    def add_component(self, name: str, comp_type: str, node_a: str, node_b: str, value: float):
        self.circuit["components"].append({
            "name": name,
            "type": comp_type,
            "n1": node_a,
            "n2": node_b,
            "value": value
        })

    # -------- Validation -------- #

    def validate(self):
        errors = CircuitValidator.validate(self.circuit)
        if errors:
            raise ValueError(f"Circuit validation failed: {errors}")
        return True

    # -------- Simulation Methods -------- #

    def run_dc(self):
        self.validate()
        solver = DCSolver(self.circuit)
        return solver.solve()

    def run_ac(self, frequency=1000):
        self.validate()
        solver = ACSolver(self.circuit, frequency)
        return solver.solve()

    def run_transient(self, t_stop=1.0, dt=1e-3):
        self.validate()
        solver = TransientSolver(self.circuit, t_stop, dt)
        return solver.solve()

    # -------- File I/O -------- #

    def save(self, filename: str):
        FileManager.save_circuit(filename, self.circuit)

    def load(self, filename: str):
        self.circuit = FileManager.load_circuit(filename)
