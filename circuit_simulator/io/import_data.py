import csv
from pathlib import Path

class ImportManager:

    @staticmethod
    def import_csv(filepath: str):
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError("CSV file not found")

        x, y = [], []
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                x.append(float(row["X"]))
                y.append(float(row["Y"]))

        print(f"📥 Data imported from CSV: {path}")
        return x, y
