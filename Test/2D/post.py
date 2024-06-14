import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots


plt.style.use(['science','ieee'])

#importing files 
n50er = pd.read_csv('n50/err.csv')
n50surf = pd.read_csv('n50/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

n150er = pd.read_csv('n150/err.csv')
n150surf = pd.read_csv('n150/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

n100er = pd.read_csv('n100/err.csv')
n100surf = pd.read_csv('n100/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

b7er = pd.read_csv('b-7/err.csv')
b7surf = pd.read_csv('b-7/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

b5er = pd.read_csv('b-5/err.csv')
b5surf = pd.read_csv('b-5/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

d10er = pd.read_csv('d10/err.csv')
d10surf = pd.read_csv('d10/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])

d30er = pd.read_csv('d30/err.csv')
d30surf = pd.read_csv('d30/surface.csv', header=0, names=['p','v1','v2','v3','x','y','z'])


#plot residual

plt.plot(n50er.Iteration[3:], n50er.Error[3:])
plt.plot(n100er.Iteration[3:], n100er.Error[3:])
plt.plot(n150er.Iteration[3:], n150er.Error[3:])
plt.xlabel("Iterations")
plt.ylabel("Residual")
plt.grid()
plt.legend(['N-50','N-100','N-150'])
plt.savefig('err-n.png')
plt.close()

plt.plot(b5er.Iteration[3:], b5er.Error[3:])
plt.plot(b7er.Iteration[3:], b7er.Error[3:])
plt.plot(n100er.Iteration[3:], n100er.Error[3:])
plt.xlabel("Iterations")
plt.ylabel("Residual")
plt.grid()
plt.legend(['$\\beta=10^{-5}$','$\\beta=10^{-7}$','$\\beta=10^{-9}$'])
plt.savefig('err-b.png')
plt.close()

plt.plot(d10er.Iteration[3:], d10er.Error[3:])
plt.plot(n100er.Iteration[3:], n100er.Error[3:])
plt.plot(d30er.Iteration[3:], d30er.Error[3:])
plt.xlabel("Iterations")
plt.ylabel("Residual")
plt.grid()
plt.legend(['$10\\times8$','$20\\times12$','$30\\times16$'])
plt.savefig('err-d.png')
plt.close()

#plot pressure distribution on the surface

n50surf['theta'] = np.arctan2(n50surf.y,n50surf.x)
n50surf = n50surf.sort_values('theta')

n150surf['theta'] = np.arctan2(n150surf.y,n150surf.x)
n150surf = n150surf.sort_values('theta')

n100surf['theta'] = np.arctan2(n100surf.y,n100surf.x)
n100surf = n100surf.sort_values('theta')

b5surf['theta'] = np.arctan2(b5surf.y,b5surf.x)
b5surf = b5surf.sort_values('theta')

b7surf['theta'] = np.arctan2(b7surf.y,b7surf.x)
b7surf = b7surf.sort_values('theta')

d10surf['theta'] = np.arctan2(d10surf.y,d10surf.x)
d10surf = d10surf.sort_values('theta')

d30surf['theta'] = np.arctan2(d30surf.y,d30surf.x)
d30surf = d30surf.sort_values('theta')

cpn50 = 2*(n50surf.p-(-0.00050517))
cpf = 1 - 4*np.square(np.sin(n50surf.theta))
cpn150 = 2*(n150surf.p-6.09731e-05)
cpn100 = 2*(n100surf.p-6.39248e-05)
cpb5 = 2*(b5surf.p-(-2.923))
cpb7 = 2*(b7surf.p-(-0.000137))
cpd10 = 2*(d10surf.p-0.0056)
cpd30 = 2*(d30surf.p-0.0067)

plt.plot(np.degrees(n50surf.theta), cpn50)
plt.plot(np.degrees(n100surf.theta), cpn100)
plt.plot(np.degrees(n150surf.theta), cpn150)
plt.plot(np.degrees(n50surf.theta),cpf)
plt.xlabel("$\\theta$ (°)")
plt.ylabel("$c_p$")
plt.legend(['N-50','N-100','N-150', 'Potential Flow'],fontsize=6)
plt.savefig('p_n.png')
plt.close()

plt.plot(np.degrees(n100surf.theta), cpn100)
plt.plot(np.degrees(b7surf.theta), cpb7)
plt.plot(np.degrees(b5surf.theta), cpb5)
plt.plot(np.degrees(n50surf.theta),cpf)
plt.xlabel("$\\theta$ (°)")
plt.ylabel("$c_p$")
plt.legend(['$\\beta=10^{-9}$','$\\beta=10^{-7}$','$\\beta=10^{-5}$', 'Potential Flow'], fontsize=6)
plt.savefig('p_b.png')
plt.close()

plt.plot(np.degrees(d10surf.theta), cpd10)
plt.plot(np.degrees(n100surf.theta), cpn100)
plt.plot(np.degrees(d30surf.theta), cpd30)
plt.plot(np.degrees(n50surf.theta),cpf)
plt.xlabel("$\\theta$ (°)")
plt.ylabel("$c_p$")
plt.legend(['$10\\times8$','$20\\times12$','$30\\times16$', 'Potential Flow'], fontsize=6)
plt.savefig('p_d.png')
plt.close()
