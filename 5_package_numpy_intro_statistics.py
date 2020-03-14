import numpy as np
import os

city = ([1.64   ,   71.78],
        [1.37   ,   63.35],
        [1.6    ,   55.09],
        [2.04   ,   55.09],
        [2.04   ,   68.72],
        [2.01   ,   73.57],
        [1.85   ,   90.02],
        [1.75   ,   78.55])

np_city = np.array(city)

print(np.mean(np_city[:,0]))
print(np.mean(np_city[0,:]))

print(np.median(np_city[:,0]))
print(np.median(np_city[0,:]))

print(np.corrcoef (np_city[:,0], np_city[:,1])  )

print(np.std(np_city[:,0]))
print(np.std(np_city[0,:]))

print(np.sum(np_city[:,0]))
print(np.sum(np_city[:,1]))

print(np.sum(np_city[0,:]))
print(np.sum(np_city[1,:]))
print(np.sum(np_city[2,:]))

print(np.sort(np_city,axis=0))
print(np.sort(np_city,axis=None))

#-------------------------------------#
generate_height = np.round(np.random.normal(1.75,0.2,5000),2)
generate_weight = np.round(np.random.normal(60.32,15,5000),2)
np_city_new = np.column_stack((generate_height,generate_weight))

print(np_city_new)

user=os.path.expandvars("%userprofile%")
np.savetxt(user+"\\Desktop\\5_generated_city.txt",np_city_new)
