import csv
import matplotlib.pyplot as plt
from pathlib import Path

class ExportManager:

    @staticmethod
    def export_csv(filepath: str, x, y):
        path = Path(filepath)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["X", "Y"])
            for xi, yi in zip(x, y):
                writer.writerow([xi, yi])

        print(f"📤 Data exported to CSV: {path}")

    @staticmethod
    def export_plot_png(filepath: str, x, y, title="Simulation Result"):
        path = Path(filepath)

        plt.figure()
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel("Time / Frequency")
        plt.ylabel("Voltage / Current")
        plt.grid(True)
        plt.savefig(path, dpi=300)
        plt.close()

        print(f"🖼 Plot exported to PNG: {path}")
