import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 
 
def system(x, t): 
    A = np.array([[8, -5], 
                  [13, -8]]) 
    dxdt = np.dot(A, x) 
    return dxdt 
 
x0_1 = np.array([1,1]) 
x0_2 = np.array([-2,1]) 
x0_3 = np.array([0,-1]) 
x0_4 = np.array([1,2]) 
x0_5 = np.array([2,3]) 
 
t = np.linspace(0, 5, 100) 
 
x1_1, x2_1 = odeint(system, x0_1, t).T 
x1_2, x2_2 = odeint(system, x0_2, t).T 
x1_3, x2_3 = odeint(system, x0_3, t).T 
x1_4, x2_4 = odeint(system, x0_4, t).T 
x1_5, x2_5 = odeint(system, x0_5, t).T 
 
plt.figure(figsize=(12,4)) 
 
plt.subplot(1, 3, 1) 
plt.plot(t, x1_1, label='Set1') 
plt.plot(t, x1_2, label='Set2') 
plt.plot(t, x1_3, label='Set3') 
plt.plot(t, x1_5, label='Set5') 
plt.xlabel('t') 
plt.ylabel('x1(t)') 
plt.legend() 
 
plt.subplot(1, 3, 2) 
plt.plot(t, x2_1, label='Set1') 
plt.plot(t, x2_2, label='Set2') 
plt.plot(t, x2_3, label='Set3') 
plt.plot(t, x2_4, label='Set4') 
plt.plot(t, x2_5, label='Set5') 
plt.xlabel('t') 
plt.ylabel('x22(t)') 
plt.legend() 
 
plt.subplot(1, 3, 3) 
plt.plot(x1_1, x2_1, label='Set1') 
plt.plot(x1_2, x2_2, label='Set2') 
plt.plot(x1_3, x2_3, label='Set3') 
plt.plot(x1_4, x2_4, label='Set4') 
plt.plot(x1_5, x2_5, label='Set5') 
plt.xlabel('x1') 
plt.ylabel('x2') 
plt.legend() 
 
plt.tight_layout() 
plt.show()
