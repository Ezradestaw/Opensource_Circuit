from setuptools import setup, find_packages

setup(
    name="opencircuitsimulator",
    version="0.1.0",
    author="Ezra Destaw",
    author_email="ezradestaw@example.com",
    description="Open-source circuit simulator for engineering students",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/OpenCircuitSimulator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "sympy",
        "matplotlib",
        "plotly",
        "pyqt5",
        "numba"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)"
    ],
    python_requires=">=3.9",
)
