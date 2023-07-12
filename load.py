import numpy as np
import pandas as pd
import astropy.io.fits as fits


def file_read(filepath):
    #load a .csv file and output a dataframe with wavelength and intensity information
    spectrum  = pd.read_csv(filepath, header=[0])
    # print()
    spectrum.columns.values[0] = 'Wavenumber'
    spectrum.columns.values[1] = 'Intensity'
    return spectrum

