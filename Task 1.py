import matplotlib.pyplot as plt
import numpy as np
from contextlib import redirect_stdout
import os

if __name__ == '__main__':
    x = np.linspace(-5,5,500)
    y = -20*np.exp(-0.2*np.sqrt(0.5*x**2))-np.exp(0.5*(np.cos(2*np.pi*x)+1))+np.exp(1)+20
    plt.plot(x,y)
    plt.show()

    if 'results' not in os.listdir():
        os.makedirs(os.path.join(os.getcwd(), 'results'))

    with open("results/results.csv", "w", encoding="utf-8") as file:
        for i in range(len(x)):
            file.write('{}, {}, {}\n'.format(i+1,x[i], y[i]))
