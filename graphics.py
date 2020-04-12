from matplotlib import pyplot as plt
from matplotlib import style
from math import pi
import numpy as np

class plot(object):
    """docstring for plot."""

    def __init__(self):
        super(plot, self).__init__()
        #self.figure=plt.figure(figsize=(5,5))
        style.use("dark_background")

    def analytical_model(self):
        theta_arr_model=np.linspace(0,2*pi,1000)
        f = lambda x : np.cos(x) - np.cos(3*x) + np.cos(-x) + np.cos(x)
        plt.plot(theta_arr_model/pi, f(theta_arr_model), '--', linewidth = 2,\
                                            color = 'w', label = 'analytical')

    def qiskit_simulation(self, x, y):
        plt.plot(x, y, linewidth = 2, color='r', label = 'simulation')

    def qiskit_quantum_computer(self, x, y):
        plt.scatter(x, y, s=50, marker='o', facecolor='None', color='w', label = 'ibmq')

    def classical_limit(self):
        plt.axhline(2)
        plt.axhline(-2)
        plt.text(0.8,1.5,'$classical$')
        plt.text(0.8,2.3,'$quantum$')

    def show(self):
        plt.xlabel(r'$\theta/\pi$',fontsize=20)
        plt.ylabel(r'$S(\theta)$',fontsize=20)
        plt.legend()
        plt.show()
