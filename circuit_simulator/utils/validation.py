class CircuitValidator:
    """Validates circuit topology & values"""

    @staticmethod
    def check_open_circuit(nodes, connections):
        """Detect unconnected nodes"""
        connected_nodes = set()
        for a, b in connections:
            connected_nodes.add(a)
            connected_nodes.add(b)

        open_nodes = [n for n in nodes if n not in connected_nodes]
        return open_nodes

    @staticmethod
    def check_short_circuit(connections):
        """Detect short circuits (same node connected)"""
        shorts = []
        for a, b in connections:
            if a == b:
                shorts.append((a, b))
        return shorts

    @staticmethod
    def check_invalid_values(components):
        """Detect invalid component values"""
        errors = []
        for comp in components:
            if comp["value"] <= 0:
                errors.append(f"{comp['name']} has invalid value: {comp['value']}")
        return errors

    @staticmethod
    def validate(circuit):
        """Run all checks"""
        errors = []
        errors += CircuitValidator.check_open_circuit(
            circuit["nodes"], circuit["connections"]
        )
        errors += CircuitValidator.check_short_circuit(
            circuit["connections"]
        )
        errors += CircuitValidator.check_invalid_values(
            circuit["components"]
        )
        return errors
