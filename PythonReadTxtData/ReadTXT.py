#!/usr/bin/env python3
import numpy as np
import h5py

class ReadTxt:
    def __init__(self,fileAddress,energy_in,theta): # energy_in(meV) angle(degree)
        self.skipNum=95
        self.data=np.loadtxt(fileAddress,skiprows=self.skipNum)
        self.enin_exp=energy_in
        self.angle=theta

    def readData(self):
        rowNum=np.nonzero(self.data[:,0]==self.angle)
        rowNum_min=np.min(rowNum)
        rowNum_max=np.max(rowNum)
        enout_exp=self.data[rowNum_min:rowNum_max+1,1]  # meV
        s_exp=self.data[rowNum_min:rowNum_max+1,2]

        hf=h5py.File('DataExperiment.h5','w')
        hf.create_dataset('enout_exp',data=enout_exp*0.001) # eV
        hf.create_dataset('enin_exp',data=np.array([self.enin_exp])*0.001) # eV
        hf.create_dataset('theta_exp',data=np.array([self.angle]))
        hf.create_dataset('s_exp',data=s_exp)
        hf.create_dataset('enout_interp',data=np.linspace(0.0000,np.max(enout_exp)*0.001,400))
        hf.close()
