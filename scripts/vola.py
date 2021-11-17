from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
import math
X = []

s =0


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

Y = np.array([20,40,60,80,100,120])

a = np.polyfit(X,Y,4)
n = np.linspace(400, 3100, 2000, True)
yn = a[0]*n**4 + a[1]*n**3 + a[2]*n**2 + a[3]*n +a[4]

plt.plot(n,yn)
plt.scatter(X,Y)

#i = 0
#f = open(r'C:\Users\user\Desktop\волна\data\potop3.txt')
#for line in f:
#    p=int(line)
#    y=a[0]*p**4 + a[1]*p**3 + a[2]*p**2 + a[3]*p +a[4]
#    if (i > 1 and i < 13333):
#        plt.plot(i*3/20000,y, ',r')
#    else:
#        plt.plot(i*3/20000,y, ',b')
#
#    i = i+1
#f.close

plt.show()
