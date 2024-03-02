from scipy import constants as constants
import numpy as np
#Define number of points and limits
N=34

epsilon=1.e-10
#start integral close to x=0 because integrand still dierges
a=epsilon
b=1.-epsilon