import numpy as np
import time
import matplotlib.pyplot as plt

rat = []
lamb_s = []

for lamb in np.linspace(0, 10, 30):
	N_0 = 10**7


	r1_raw = np.random.random_sample(N_0)
	r2_raw = np.random.random_sample(N_0)
	theta_raw = np.random.random_sample(N_0)
	phi_raw = np.random.random_sample(N_0)

	# to other distribution
	r1 = r1_raw**(1/3)
	r2 = -lamb*np.log(r2_raw)
	theta = np.arccos(2*theta_raw - 1)
	phi = phi_raw*2*np.pi

	x = r1 + r2*np.sin(theta)*np.cos(phi)
	y = r2*np.sin(theta)*np.sin(phi)
	z = r2*np.cos(theta)

	one_s = np.ones_like(x)
	one_zero = np.less(x**2 + y**2 + z**2, one_s)*1
	N = np.sum(one_zero)
	print(N/N_0)
	rat.append(N/N_0)
	lamb_s.append(lamb)

plt.plot(lamb_s, rat)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$N/N_0$')
plt.show()