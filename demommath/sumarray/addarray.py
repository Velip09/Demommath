# Import the NumPy library with the alias 'np'
import numpy as np
# Define a function 'add_num' that takes two parameters 'u' and 'v'
def add_num(u,v):                      # Use NumPy's sum function to add 'u' and 'v' element-wise along axis 0
      return np.sum([u, v], axis=0)

