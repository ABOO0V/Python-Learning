
# package in Python is a way of structuring Python’s module namespace by using “dotted module names”.
# A package is a collection of Python modules:
# while a module is a single Python file, a package is a directory of Python module(s) containing an additional __init__.py file,
# which distinguishes a package from a directory that just happens to contain a bunch of Python scripts.

import matplotlib.pyplot as plt

# plt is a module in matplotlib library which is used for plotting graphs in Python.
# It is a collection of functions and classes that allow us to create various types of plots and visualizations.


#  data 

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# bar chart
plt.bar(x, y, color='blue', width=0.5)

# line plot
plt.plot(x, y, color='red', marker='o', linestyle='--')

plt.show()