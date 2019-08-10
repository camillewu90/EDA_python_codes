import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Creat a function that output a ECDF function when inputing a np.array
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1,1+n)/n
    return x,y

# Test data
data = np.array([4,3,5,32,5,65,66,77,46,2])

# Unpack the x and y from the ecdf function
x,y = ecdf(data)

# set the seaborn default style
sns.set()

# Plot the ECDF plot
_ = plt.plot(x, y, marker='.', linestyle = 'none')
_ = plt.xlabel('x')
_ = plt.ylabel('ECDF')
plt.show()
