import matplotlib.pyplot as plt
import numpy as np
import math
from math import exp as e
from math import pi as pi

x = np.linspace(-3,3,5000)
y = []

xo = np.linspace(0,1,25)
yo = [e(i)-1 for i in xo]
x1 = [1,3]
y1 = [e(1)-1,e(1)-1]

for t in x:
	ima = 1.3867495867890338
	for n in range(1,101):
		wolfram = (2/3)*math.cos(n*t*(2*pi/3))*((e(1)*n*(2*pi/3)*math.sin(n*(2*pi/3))+e(1)*math.cos(n*(2*pi/3))-1)/(n*n*(2*pi/3)*(2*pi/3)+1) - math.sin(n*(2*pi/3))/(n*(2*pi/3)) + ((e(1) - 1)*(math.sin(3*n*(2*pi/3)) - math.sin(n*(2*pi/3))))/(n*(2*pi/3))) + (2/3)*math.sin(n*t*(2*pi/3))*(((1 - (e(1) - 1)*n*n*(2*pi/3)*(2*pi/3))*math.cos(n*(2*pi/3)) + e(1)*n*(2*pi/3)*math.sin(n*(2*pi/3)) - 1)/(n*n*n*(2*pi/3)*(2*pi/3)*(2*pi/3)+n*(2*pi/3))+(2*(e(1) - 1)*math.sin(n*(2*pi/3))*math.sin(2*n*(2*pi/3)))/(n*(2*pi/3)))
		ima = ima + wolfram
	y.append(ima)
	ima = 1.3867495867890338

plt.plot(xo,yo, x1,y1, x,y)
plt.title("n=100")
plt.ylabel("f(t)")
plt.xlabel("t")
plt.grid()
plt.savefig('demo.png', bbox_inches='tight')