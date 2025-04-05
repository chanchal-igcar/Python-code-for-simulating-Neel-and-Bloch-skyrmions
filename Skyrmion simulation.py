# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:10:38 2024

@author: Chanchal
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the simulation
L = 500  # Grid size (100x100 pixels)
R = 20   # Skyrmion radius (size of the skyrmion)
alpha = 1.0  # Contrast factor for the TEM image
center = (L // 2, L // 2)  # Skyrmion center (center of the grid)

# Create a grid for the simulation
x = np.linspace(-L/2, L/2, L)
y = np.linspace(-L/2, L/2, L)
X, Y = np.meshgrid(x, y)

# Function to generate a Bloch skyrmion magnetization components
def bloch_skyrmion(X, Y, R):
    r = np.sqrt(X**2 + Y**2)  # Radial distance from the center
    theta = np.arctan2(Y, X)  # Angular coordinate
    phi = np.pi * (1 - 2 * (r / R))  # Skyrmion winding angle
    mx = np.cos(phi) * np.cos(theta)  # x-component of magnetization
    my = np.cos(phi) * np.sin(theta)  # y-component of magnetization
    mz = np.sin(phi)  # z-component (out-of-plane)
    return mx, my, mz

# Function to generate a Néel skyrmion magnetization components
def neel_skyrmion(X, Y, R):
    r = np.sqrt(X**2 + Y**2)  # Radial distance from the center
    theta = np.arctan2(Y, X)  # Angular coordinate
    phi = np.pi * (r / R)  # Skyrmion winding angle
    mx = np.cos(phi) * np.cos(theta)  # x-component of magnetization
    my = np.cos(phi) * np.sin(theta)  # y-component of magnetization
    mz = np.sign(X) * np.sin(phi)  # z-component (out-of-plane)
    return mx, my, mz

# Generate Bloch and Néel skyrmion magnetization components
mx_bloch, my_bloch, mz_bloch = bloch_skyrmion(X, Y, R)
mx_neel, my_neel, mz_neel = neel_skyrmion(X, Y, R)

# Plot Bloch skyrmion magnetization directions
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, mx_bloch, my_bloch, mz_bloch, scale=10, cmap='inferno')
plt.title("Bloch Skyrmion - Spin Directions")
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Spin Direction (Z component)')
plt.show()

# Plot Néel skyrmion magnetization directions
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, mx_neel, my_neel, mz_neel, scale=10, cmap='inferno')
plt.title("Néel Skyrmion - Spin Directions")
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Spin Direction (Z component)')
plt.show()

# Simulate the TEM image for Bloch skyrmion (based on the mz component)
tem_image_bloch = alpha * mz_bloch

# Simulate the TEM image for Néel skyrmion (based on the mz component)
tem_image_neel = alpha * mz_neel

# Plot the simulated TEM image for Bloch skyrmion
plt.figure(figsize=(6, 6))
plt.imshow(tem_image_bloch, cmap='inferno', origin='lower')
plt.title("Bloch Skyrmion - TEM Image")
plt.colorbar(label="Intensity")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Plot the simulated TEM image for Néel skyrmion
plt.figure(figsize=(6, 6))
plt.imshow(tem_image_neel, cmap='inferno', origin='lower')
plt.title("Néel Skyrmion - TEM Image")
plt.colorbar(label="Intensity")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
