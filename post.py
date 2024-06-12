import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots


plt.style.use(['science','ieee'])

#importing files 
er = pd.read_csv('err.csv')
surf = pd.read_csv('surface.csv')

#plot residual

plt.plot(er.Iteration[2:], er.Error[2:])
plt.xlabel("Iterations")
plt.ylabel("Residual")
plt.grid()
plt.savefig('err.png')
plt.close()

#plot pressure distribution on the surface

surf['theta'] = np.arctan2(surf.y,surf.x)
surf = surf.sort_values('theta')
p0 = 0.01
cp = 2*(surf.p-p0)
cpf = 1 - 4*np.square(np.sin(surf.theta))

plt.plot(np.degrees(surf.theta), cp)
plt.plot(np.degrees(surf.theta),cpf)
plt.xlabel("$\\theta$ (°)")
plt.ylabel("$c_p$")
plt.title("Pressure distribution along the surface on the cylinder")
plt.grid()
plt.legend(['FreeFEM', 'Potential Flow'])
plt.savefig('p.png')
plt.close()