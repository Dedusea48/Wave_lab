from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
import math
X = []

s =0
X.append(0)

f = open(r'C:\Users\user\Desktop\волна\data\20mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close
s =0
f = open(r'C:\Users\user\Desktop\волна\data\40mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close
s =0
f = open(r'C:\Users\user\Desktop\волна\data\60mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close
s =0
f = open(r'C:\Users\user\Desktop\волна\data\80mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close
s =0
f = open(r'C:\Users\user\Desktop\волна\data\100mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close
s =0
f = open(r'C:\Users\user\Desktop\волна\data\120mm.txt')
for line in f:
    s = s + int(line)
X.append(s/2000)
f.close

Y = np.array([0,20,40,60,80,100,120])

M = np.array([
    [0,0,0,0,0,0,1],
    [X[1]**6,X[1]**5,X[1]**4, X[1]**3, X[1]**2, X[1], 1],
    [X[2]**6,X[2]**5,X[2]**4, X[2]**3, X[2]**2, X[2], 1],
    [X[3]**6,X[3]**5,X[3]**4, X[3]**3, X[3]**2, X[3], 1],
    [X[4]**6,X[4]**5,X[4]**4, X[4]**3, X[4]**2, X[4], 1],
    [X[5]**6,X[5]**5,X[5]**4, X[5]**3, X[5]**2, X[5], 1],
    [X[6]**6,X[6]**5,X[6]**4, X[6]**3, X[6]**2, X[6], 1]
    ])
a = np.linalg.solve(M, Y)

n = np.linspace(0, 3100, 1000, True)
yn =a[0]*n**6 + a[1]*n**5 + a[2]*n**4 + a[3]*n**3 + a[4]*n**2 + a[5]*n +a[6]
plt.plot(n, yn)

plt.scatter(X,Y)

#i = 0
#f = open(r'C:\Users\user\Desktop\волна\data\potop2.txt')
#for line in f:
#    p=int(line)
#    y=a[0]*p**4 + a[1]*p**3 + a[2]*p**2 + a[3]*p +a[4]
#    plt.plot(i*3/20000,y, ',b')
#    i = i+1
#    if (i>200000/6):
#        break
#
#f.close

plt.show()