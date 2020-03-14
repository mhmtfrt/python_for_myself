#python3 get-pip.py
#pip3 install numpy

import numpy

intel = numpy.array(["core","pentium","atom","xeon"])

import numpy as np

amd = np.array(["ryzen","threadripper","fx"])

from numpy import array

nvidia = array(["geforce","quadro","jetson"])

print(intel)
print(amd)
print(nvidia)

#--------------------------------------------------------#
import numpy as np

height = [1.73, 1.89, 1.70, 1.82]
weight = [85, 92 , 80, 80]
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height**2

r_bmi = [round(num, 2) for num in bmi]

print(bmi)
print(r_bmi)
print(bmi>25)
print(bmi[bmi>25])
#--------------------------------------------------------#

print(height + weight)
print(np_height + np_weight)
