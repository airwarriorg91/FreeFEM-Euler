# FreeFEM-Euler
This repository contains code to solve the incompressible inviscid Euler equations using the artificial compressibility method. The code is implemented in FreeFEM and supports both 2D and 3D computations. For 2D computations, the geometry is created directly in FreeFEM, while for 3D computations, GMSH-generated meshes are imported.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [2D Computations](#2d-computations)
  - [3D Computations](#3d-computations)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this code, you need to have FreeFEM and GMSH installed on your system.

1. **FreeFEM Installation**
   - Follow the instructions on the [FreeFEM website](https://freefem.org/download.html) to install FreeFEM.

2. **GMSH Installation (for 3D computations)**
   - Follow the instructions on the [GMSH website](https://gmsh.info/) to install GMSH.

## Usage
### Important parameters
1. **Domain Size**: The computational domain should be big enough such that the far-field boundary condition is achieved and the boundaries don't interfere with the flow near the object.

2. **Mesh Refinement**: The mesh should be small enough near the body wall so that the flow can be computed accurately and solution doesn't diverge.

3. **Artificial Compressibility**: An appropriate value of artificial compressibility should be choosen so that the solution converges quickly. Generally, the value of $\beta$ exists between 0 and 1. The default value of $\beta$ is $10^{-9}$. (For more details and convergence study, refer to the [report](https://github.com/airwarriorg91/FreeFEM-Euler/blob/master/Test/report/report.pdf).
### 2D Computations

For 2D computations, the geometry and mesh are created within the FreeFEM script. You can find the 2D script in the `2D` directory.

1. Navigate to the `2D` directory:
   ```sh
   cd 2D
   ```

2. Run the FreeFEM script:
   ```sh
   FreeFem++ solver2D.edp
   ```

### 3D Computations

Will be updated soon.

## Examples

### 2D Example

A sample 2D computation is provided in the `2D` directory. The script `Solver2D.edp` demonstrates how to set up and solve the flow around a cylinder. The results are saved in VTK format for visualization. The code is tested for different values of N (number of points on cylinder surface), $\beta$ (Artificial compressibility) and domain
size. The detailed [report](https://github.com/airwarriorg91/FreeFEM-Euler/blob/master/Test/report/report.pdf) for the test along with the visualization files are present in the `Test/2D` directory.

![The steady state solution for flow around a cylinder computed using the code](/Test/2D/n50/cyl.png)

### 3D Example

Will be updated soon.

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or new features, please submit a pull request. Ensure that your code follows the existing style and include appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the sections to better fit the specifics of your repository. If you have any additional information or examples, you can include them in the relevant sections.
