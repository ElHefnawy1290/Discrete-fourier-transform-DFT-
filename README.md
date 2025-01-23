# Discrete Fourier Transform (DFT) and Inverse DFT (IDFT) Implementation

## Overview
This project implements the Discrete Fourier Transform (DFT) and its inverse (IDFT) using Python. It includes functionality to compute the magnitude and phase of the DFT, as well as reconstruct signals using the IDFT.

## Features
- Custom implementation of complex number operations.
- Calculation of the twiddle matrix for DFT and IDFT.
- Functions for computing DFT and IDFT.
- Calculation of magnitude and phase of the DFT.
- User input support for signal processing.

## Installation
No external dependencies are required. The implementation uses Python's built-in `math` module.

## Usage
Run the script and choose one of the following options:

1. Compute the Discrete Fourier Transform (DFT).
2. Compute the Inverse Discrete Fourier Transform (IDFT).

### Running the Program
```bash
python filename.py
```

### Example Input & Output
#### DFT Example:
```
Enter 1 or 2
1) DFT
2) IDFT
1
Enter the signal values (space-separated): 1 2 3 4

DFT Result: [(10.0 + 0.0i), (-2.0 + 2.0i), (-2.0 + 0.0i), (-2.0 - 2.0i)]

Magnitude of DFT: [10.0, 2.83, 2.0, 2.83]

Phase of DFT: [0.0, 135.0, 180.0, -135.0]
```

#### IDFT Example:
```
Enter 1 or 2
1) DFT
2) IDFT
2
Enter the signal values (space-separated): (10.0+0.0j) (-2.0+2.0j) (-2.0+0.0j) (-2.0-2.0j)

IDFT Result: [(1.0 + 0.0i), (2.0 + 0.0i), (3.0 + 0.0i), (4.0 + 0.0i)]
```

## Functions
- `dft(input_signal)`: Computes the Discrete Fourier Transform of the input signal.
- `Idft(input_signal)`: Computes the Inverse Discrete Fourier Transform.
- `calculate_twiddle_matrix(N)`: Generates the twiddle matrix for DFT.
- `calculate_twiddle_matrix_star(N)`: Generates the twiddle matrix for IDFT.
- `calculate_magnitude_and_phase(dft_result)`: Computes the magnitude and phase of the DFT result.
- `get_input()`: Gets input from the user for DFT.
- `get_input_Inverse()`: Gets input from the user for IDFT.

## Notes
- The implementation uses a custom `complex` class to handle complex number operations.
- Floating-point precision may affect results slightly.

