tesla = [1.73, 1.68, 1.71, 1.89]
vw = [[1, 1.73], [2, 1.68], [3, 1.71], [4, 1.89]]

print(tesla, "\n" , vw[1] , "\n" , vw[2:] , "\n")

tesla[3] = 1.85
tesla = tesla + [1.89]
print(tesla, "\n") 
del(tesla[0])
print(tesla, "\n") 
#------------------------#

benz = ["a","b","c"]
mercedes = benz
del(mercedes[1])
print(benz,"\n",mercedes,"\n")

bmw = ["a","b","c"]

#m_benz = list(bmw)
m_benz = bmw[:]
del(m_benz[1])

print(bmw,"\n",m_benz,"\n")
