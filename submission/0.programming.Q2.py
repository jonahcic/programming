import numpy as np
import matplotlib.pyplot as plt

# parts 1-7

x1 = np.linspace(0, 1, 50)
y1 = np.log(x1)
z1 = np.exp(x1)
plt.scatter(x1, y1, label="Natural Log")
plt.scatter(x1, z1, label="Exponential")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="lower right")
plt.title("Natural Log and Exponential Functions")
plt.show()

# parts 8-12

x2 = np.linspace(-6.5, 6.5, 100)
y2 = np.sin(x2)
z2 = np.cos(x2)
plt.plot(x2, y2, label="Sine")
plt.plot(x2, z2, label="Cosine")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="lower left")
plt.title("Sine and Cosine")
plt.show()

