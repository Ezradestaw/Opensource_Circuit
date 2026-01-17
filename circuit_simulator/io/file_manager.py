import json
from pathlib import Path

class FileManager:
    @staticmethod
    def save_circuit(filepath: str, circuit_data: dict):
        path = Path(filepath)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(circuit_data, f, indent=4)
        print(f"✅ Circuit saved to {path}")

    @staticmethod
    def load_circuit(filepath: str) -> dict:
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError("Circuit file not found")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"📂 Circuit loaded from {path}")
        return data
