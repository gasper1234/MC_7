import numpy as np
import time
import matplotlib.pyplot as plt

lamb_s =  [0.2, 0.6, 1, 1.4]

fig, ax = plt.subplots(2, 2)

for k in range(len(lamb_s)):
	N_0 = 10**6//2
	lamb = lamb_s[k]

	r1_raw = np.random.random_sample(N_0)
	r2_raw = np.random.random_sample(N_0)
	theta_1_raw = np.random.random_sample(N_0)
	phi_1_raw = np.random.random_sample(N_0)
	theta_raw = np.random.random_sample(N_0)
	phi_raw = np.random.random_sample(N_0)

	# to other distribution
	r1 = r1_raw**(1/3)
	r2 = -lamb*np.log(r2_raw)
	theta = np.arccos(2*theta_raw - 1)
	phi = phi_raw*2*np.pi
	theta_1 = np.arccos(2*theta_raw - 1)
	phi_1 = phi_raw*2*np.pi

	x = r1*np.sin(theta_1)*np.cos(phi_1) + r2*np.sin(theta)*np.cos(phi)
	y = r1*np.sin(theta_1)*np.sin(phi_1) + r2*np.sin(theta)*np.sin(phi)
	z = r1*np.cos(theta_1) + r2*np.cos(theta)

	one_s = np.ones_like(x)
	one_zero = np.less(x**2 + y**2 + z**2, one_s)*1
	N = np.sum(one_zero)

	x_0 = []
	z_0 = []
	for i in range(len(y)):
		if y[i] < 0.01 and y[i] > -0.01:
			if x[i]**2 + z[i]**2 < 1:
				x_0.append(x[i])
				z_0.append(z[i])

	print(len(x_0))
	circle_x = np.linspace(-1, 1, 100)
	circle_z_max = np.sqrt(np.ones_like(circle_x)-circle_x**2)
	circle_z_min = -np.sqrt(np.ones_like(circle_x)-circle_x**2)


	ax[k//2][k%2].plot(x_0, z_0, 'x')
	ax[k//2][k%2].plot(circle_x, circle_z_min, 'r-')
	ax[k//2][k%2].plot(circle_x, circle_z_max, 'r-')
	ax[k//2][k%2].set_title(r'$\lambda = $'+str(lamb))
	ax[k//2][k%2].axis('equal')
plt.show()