#!/usr/bin/python
# -*- coding: utf-8 -*-
# File: planck.py
# Created: 2014-01-17 by gks 
"""
Description: A program that plots the Planck-function in a certain interval
"""
import numpy as np
from pylab import *
from scipy import *
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy import optimize
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm

#---------------------FONT and other graphics------------------------
font = {'family'         : 'serif',
	'weight'         : 'bold',
	'size'	         : 16}
matplotlib.rc('font',**font)
matplotlib.rc('grid',linewidth=1)
matplotlib.rc('xtick.major',width=2)
matplotlib.rc('xtick.major',size=7)
matplotlib.rc('xtick.minor',width=2)
matplotlib.rc('xtick.minor',size=4)
matplotlib.rc('ytick.major',width=2)
matplotlib.rc('ytick.major',size=7)
matplotlib.rc('ytick.minor',width=2)
matplotlib.rc('ytick.minor',size=4)

#-------------------------------------------------

#---------------------DATA------------------------
#Note: in SI units
pi = const.pi 
c = const.c
h = const.h 
k = const.k 
#-------------------------------------------------


def planck(wave, temp):
	"""
        Input: Wavelength values
        Returns: B_nu(wave,temp), the Planck distribution function in SI units
        """
        numer = 2.*h*(c)**2/wave**5
        denom = exp(h*c/(k*temp*wave))-1.
	return numer/denom

#------------Figure Layout--------------
##One Figure
fig = plt.figure()
ax = fig.add_subplot(111)
adjustprops = dict(left=0.19,bottom=0.15,right=0.92,top=0.9,wspace=0.,hspace=0.2)
fig.subplots_adjust(**adjustprops)

ax.set_xlabel(r'$\lambda \, [nm]$',size="x-large")
ax.set_ylabel(r'$B_{\lambda} \, [\mathrm{W \, m^{-2} \, nm^{-1} \, ster^{-1}}]$',size="x-large")
#ax.set_xlim()
#ax.set_ylim()
plt.ticklabel_format(style="sci",scilimits=(2,2),axis="y")


ax.minorticks_on()
ax.grid()

wave = np.linspace(1,1400,1400)
spec_5777 = planck(wave*1e-9,5777)/10**9 #dividing by 10**9 to get nm^-1 in units
spec_7000 = planck(wave*1e-9,7000)/10**9 #dividing by 10**9 to get nm^-1 in units

#PLOT
ax.plot(wave,spec_7000,color="blue",linewidth=3,linestyle="-",label=r"$T_1=7000 \, \mathrm{K}$")
ax.plot(wave,spec_5777,color="red",linewidth=3,linestyle="-",label=r"$T_2=5777 \, \mathrm{K}$")

#---------------------------------------
#-------------------------GRAPHICS
legend(loc='upper right')

#SAVING
fig.show()
#fig.savefig("planck.pdf")
fig.savefig("planck.png")
