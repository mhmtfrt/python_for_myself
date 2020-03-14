fam = [1.73, 1.68, 1.71, 1.89]
fam2 = [[1, 1.73], [2, 1.68], [3, 1.71], [4, 1.89]]

print(fam, "\n" , fam2[1] , "\n" , fam2[2:] , "\n")

fam[3] = 1.85
fam = fam + [1.89]
print(fam, "\n") 
del(fam[0])
print(fam, "\n") 

x = ["a","b","c"]
y = x
del(y[1])
print(x,"\n",y,"\n")


x2 = ["a","b","c"]

#t = list(x2)
t = x2[:]
del(t[1])

print(x2,"\n",t,"\n")
