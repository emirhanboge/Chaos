# Heat Equation Simulations

This repository contains simulations of the heat equation in 1D, 2D, and 3D.

## 1D Heat Equation

The 1D heat equation is described by:

![1D Equation](https://latex.codecogs.com/svg.latex?\bg_white\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2})

Here is the simulation result:

![1D Simulation](assets/heat_1d.gif)

## 2D Heat Equation

The 2D heat equation is described by:

![2D Equation](https://latex.codecogs.com/svg.latex?\bg_white\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right))

Here is the simulation result:

![2D Simulation](assets/heat_2d.gif)

## 3D Heat Equation

The 3D heat equation is described by:

![3D Equation](https://latex.codecogs.com/svg.latex?\bg_white\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right))

Here is the simulation result:

![3D Simulation](assets/heat_3d.gif)

## Methodology

We've employed the explicit finite difference method to numerically solve the heat equation. The stability of the simulations is maintained by adhering to the criterion:

![Stability Criterion](https://latex.codecogs.com/svg.latex?\bg_white\alpha \frac{dt}{{dx}^2} \leq 0.5)

Where:
- \( \alpha \) is the diffusivity coefficient.
- \( dx \) is the spatial step.
- \( dt \) is the temporal step.

## Dependencies

- numpy
- matplotlib
- imageio
- mpl_toolkits.mplot3d

