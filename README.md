# Convex Hulls
Algorithms course at Ecole Polytechnique
Elsa MAILLET, Nadine HAGE CHEHADE

## Project overview
This project aims to implement and test different algorithms for computing the convex hull of a set of points in the 2D plane. We consider the following algorithms:
- the gift-wrapping algorithm
- the sweeping algorithm
- the Kirkpatrick–Seidel algorithm
- the quick hull algorithm
These different methods are tested on randomly generated datasets.

## Files organization
The code is divided into multiple files as follows : 
- `main.py`: the main program where functions can be tested. You can uncomment the desired functions to test them out.
- `datasets.py`: function definitions for datasets A, B, C and D, along with a visualization function
- `utils.py`: contains functions that are called frequently, like the hull visualization function
- `tests.py`: contains test for our different methods and algorithms
- other files each contains the implementation of the algorithm specified by the file name.

## Dependencies
- `numpy`: used to generate points at random and store arrays
- `matplotlib`: used for visualization and video generation
