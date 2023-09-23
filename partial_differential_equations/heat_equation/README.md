# Heat Equation Simulations

This repository contains simulations of the heat equation in 1D, 2D, and 3D.

## 1D Heat Equation

The 1D heat equation is described by:

![1D Equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;u}{\partial&space;t}&space;=&space;\alpha&space;\frac{\partial^2&space;u}{\partial&space;x^2})

Here is the simulation result:

![1D Simulation](assets/heat_1d.gif)

## 2D Heat Equation

The 2D heat equation is described by:

![2D Equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;u}{\partial&space;t}&space;=&space;\alpha&space;\left(&space;\frac{\partial^2&space;u}{\partial&space;x^2}&space;&plus;&space;\frac{\partial^2&space;u}{\partial&space;y^2}&space;\right))

Here is the simulation result:

![2D Simulation](assets/heat_2d.gif)

## 3D Heat Equation

The 3D heat equation is described by:

![3D Equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;u}{\partial&space;t}&space;=&space;\alpha&space;\left(&space;\frac{\partial^2&space;u}{\partial&space;x^2}&space;&plus;&space;\frac{\partial^2&space;u}{\partial&space;y^2}&space;&plus;&space;\frac{\partial^2&space;u}{\partial&space;z^2}&space;\right))

Here is the simulation result:

![3D Simulation](assets/heat_3d.gif)

## Methodology

We've employed the explicit finite difference method to numerically solve the heat equation. The stability of the simulations is maintained by adhering to the criterion:

![Stability Criterion](https://latex.codecogs.com/svg.latex?\alpha&space;\frac{dt}{{dx}^2}&space;\leq&space;0.5)

Where:
- \( \alpha \) is the diffusivity coefficient.
- \( dx \) is the spatial step.
- \( dt \) is the temporal step.

## Dependencies

- numpy
- matplotlib
- imageio
- mpl_toolkits.mplot3d

