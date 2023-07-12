import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from gen_voigt import voigt,generate_voigt_profile

def fit_voigt(x,y,bounds=None):
    if bounds==None:
        popt,pcov =  curve_fit(xdata=x,ydata=y,f = voigt)
        return popt,pcov
    else:
        popt,pcov =  curve_fit(xdata=x,ydata=y,f = voigt,bounds=bounds)
        return popt,pcov

def plot_fit_voigt(x,y,bounds=None):
    popt,pcov = fit_voigt(x,y,bounds=bounds)

    y = generate_voigt_profile(x, dx=popt[0], sigma=popt[1], gamma=popt[2], amplitude=popt[3], noise_std=0)

    # Plot the Voigt profile from parameters
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Intensity')
    plt.title('Voigt Profile from Parameters')
    plt.show()
    return popt, plt