## still haven't found a database, so placeholder code in the meantime

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
import warnings

def get_pressure(temp, species = 'h2o'):
    """
    Return pressure based on pressure-temperature curve for H2O or CO2.

    Parameters:
        temp (float): Temperature of planetary atmosphere in K.
        species (str): 'H2O' or 'CO2' -- species from which to calculate the pressure.
    
    Returns:
        pressure (float): Pressure in kPa.
    """
    if species.casefold() == 'h2o':
        # set Antoine equation coefficients -- calibrated in 379 - 573 K range
        # https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=4&Type=ANTOINE&Plot=on#ANTOINE
        if temp >= 376: #high temperature calibration
            a = 3.55959
            b = 643.748
            c = -198.043
        # set Antoine equation coefficients -- calibrated in 256 - 373 K range
        else:
            a = 4.6543
            b = 1435.264
            c = -64.848

        if (temp < 256) or (temp > 573):
            warnings.warn('Temperature outside of calibration range. Approximating P-T relation.')

    if species.casefold() == 'co2':
        # set Antoine equation coefficients -- calibrated in 154 - 196 K range
        # https://webbook.nist.gov/cgi/cbook.cgi?ID=C124389&Mask=4&Type=ANTOINE&Plot=on#ANTOINE
        a = 6.81228
        b = 1301.679
        c = -3.494

        if (temp < 154) or (temp > 196):
            warnings.warn('Temperature outside of calibration range. Approximating P-T relation.')

    if species.casefold() not in ['h2o', 'co2']:
        raise Exception('Specify chemical species -- "H2O" or "CO2"')
    
    logpress = a - (b/(temp + c))
    press = (10**logpress)*u.bar.to(u.kPa)
    
    return press.value

def object_profile(name, species = 'h2o',
                   figsize = (5, 5), color = 'gray', ls = '-', 
                   xlabel = 'x', ylabel = 'intensity', 
                   xscale = 'linear', yscale = 'linear'):
    """
    Return Voigt profile of line based on conditions of specific planet.

    Parameters:
        name (str): Name of planet.
        species (str): 'H2O' or 'CO2' -- species from which to calculate the pressure.
            Passed to get_pressure().

        See matplotlib documentation for following --
            figsize (tuple): Size of plotted figure.
            color (str): Color of plotted profile.
            ls (str): Line style of plotted profile.
            xlabel (str): Label on x-axis of plotted figure.
            ylabel (str): Label on y-axis of plotted figure.
            xscale (str): Scaling of x-axis of plotted figure.
            yscale (str): Scaling of y-axis of plotted figure.
    
    Returns:
        Plot of line profile. 
    """

    props = pd.read_csv('../data/props.txt', header = None, comment = '#', sep = '\t')

    if name.casefold().str.replace(' ', '') not in props.name.str.casefold().str.replace(' ', ''):
        raise Exception('Planet conditions not found. List available planets with list_object.')
    
    if name.casefold().str.replace(' ', '') in props.name.str.casefold().str.replace(' ', ''):
        planet_props = props.loc[props.name.str.casefold().str.replace(' ', '') == name.casefold().str.replace(' ', '')]

        press = get_pressure(planet_props.temp, species)

        x, spec = PLACEHOLDER_VOIGT_FUNCTION(planet_props.temp, press)

        fig = plt.figure(figsize = figsize)
        plt.plot(x, spec, color = color, ls = ls)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.title(planet_props.name)

    

def list_object():
    props = pd.read_csv('../data/props.txt', header = None, comment = '#', sep = '\t')
    for i in props.name:
        print(i)