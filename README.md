This code can simulate Lorentz TEM images for Bloch and Néel type of skyrmions and their spin orientation for (Fe,Cr)2B system.

## Skyrmion Simulation and Visualization
This Python script simulates and visualizes two types of magnetic skyrmions — **Bloch** and **Néel** — using NumPy and Matplotlib. Skyrmions are topologically protected spin structures found in magnetic materials and are of great interest in spintronics and magnetic storage technologies.
## Features
**Vector Field Visualization**: Displays the in-plane magnetization components (mx, my) and colors the arrows using the out-of-plane component (mz) for both Bloch and Néel skyrmions.
**Simulated TEM Images**: Generates transmission electron microscopy (TEM)-like images based on the z-component of the magnetization (mz), which reflects how skyrmions might appear in Lorentz TEM imaging.
## Skyrmion Types
**Bloch Skyrmion** Features magnetization that rotates tangentially around the center.
**Néel Skyrmion** Features magnetization that points radially inward or outward.
## Parameters
- `L`: Grid size (pixels)
- `R`: Skyrmion radius
- `alpha`: Contrast factor for TEM image
- `center`: Center position of the skyrmion
## Requirements
- Python 3.x
- NumPy
- Matplotlib
Install the dependencies using:
- bash
**pip install numpy matplotlib
**python skyrmion_simulation.py

**This will generate the following plots:**
**Bloch Skyrmion** - Spin Directions
**Néel Skyrmion** - Spin Directions
**Simulated TEM Image of Bloch Skyrmion**
**Simulated TEM Image of Néel Skyrmion**

**License**
This project is open-source and free to use for educational and research purposes.
