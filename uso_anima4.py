from planifica4 import planifica4
from animacion4 import animacion4
import numpy as np
from inversekinematic4 import inversekinematic4
from directkinematic4 import directkinematic4
from drawrobot3d4 import drawrobot3d4

p1=[ 0.2, 1, 0.48]
p2=[ 0.2, 1, 0.4]
p3=[ 0.26, 1, 0.4]
p4=[ 0.26, 1, 0.48]
p5=[ 0.26, 1, 0.4]
p6=[ 0.3, 1, 0.4]
p7=[ 0.3, 1, 0.48]
p8=[ 0.36, 1, 0.48]
p9=[ 0.36, 1, 0.44]
p10=[ 0.3, 1, 0.44]
p11=[ 0.36, 1, 0.44]
p12=[ 0.36, 1, 0.4]
p13=[ 0.4, 1, 0.4]
p14=[ 0.4, 1, 0.48]
p15=[ 0.46, 1, 0.48]
p16=[ 0.46, 1, 0.4]
p17=[ 0.4, 1, 0.4]

p = np.array([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17])

n=[1, 0, 0]
s=[0, 1, 0]
a=[0, 0, 1]
npuntos=10

q = np.array([0.0 ,  0.0,  0.0,  0.0])
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
al = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, al, alfa)
A04 = directkinematic4(teta, d, al, alfa)

mat_q = [[]] * 4

for i in range(3):
    mat_q = np.concatenate((mat_q, planifica4(p[i], p[i + 1], n, s, a,npuntos, teta, d, al, alfa)), axis=1)

for i in range(5,10):
    mat_q = np.concatenate((mat_q, planifica4(p[i], p[i + 1], n, s, a,npuntos, teta, d, al, alfa)), axis=1)
    
for i in range(12,16):
    mat_q = np.concatenate((mat_q, planifica4(p[i], p[i + 1], n, s, a,npuntos, teta, d, al, alfa)), axis=1)
#print(mat_q)
animacion4(mat_q,teta,d,al,alfa)



