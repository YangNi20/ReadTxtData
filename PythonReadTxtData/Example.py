#!/usr/bin/env python3
import numpy as np
import h5py
from ReadTXT import ReadTxt
#default units:
#energy eV
#wavelength angstrom
#time second
#wavenumber angstrom^-1
#angle degree

read15=ReadTxt('/home/ni/ReadData/X4sGetSubent.txt',55.0,15.0) # energy_in(meV) angle(degree)
read15.readData()
hf=h5py.File('DataExperiment.h5','r')
print(hf['enout_exp'].value)
