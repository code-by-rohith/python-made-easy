from sympy import symbols
from sympy.plotting import plot3d

# Define the symbols
x, y = symbols('x y')

# Define the function
f = x + y

# Plot the function
plot3d(f)