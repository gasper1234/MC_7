import numpy as np
import time
import matplotlib.pyplot as plt

lamb = 0.5
N_0 = 10**6

r_raw = np.random.random_sample(N_0)
theta_raw = np.ones_like(r_raw)
theta = 2*theta_raw-1
r = -lamb*np.log(r_raw)

theta_0 = np.array([])

N_sct = []
N_true_sct = [N_0]
ind = 0
theta_1 = np.array([])
theta_2 = np.array([])
while len(r)>0:
	one_s = np.ones_like(r)
	zero_s = np.zeros_like(r)
	zero_one = np.greater(r, zero_s)*1
	one_zero = np.less(r, one_s)*1
	r = r*one_zero*zero_one
	theta_0 = np.concatenate((theta_0, np.arccos(theta[r == 0])))
	if ind > 0:
		theta_1 = np.concatenate((theta_1, np.arccos(theta[r == 0])))
	if ind > 1:
		theta_2 = np.concatenate((theta_2, np.arccos(theta[r == 0])))
	r = r[r != 0]
	N_sct.append(len(r))
	N_true_sct[-1] -= N_sct[-1]
	N_true_sct.append(N_sct[-1])
	r_raw = np.random.random_sample(len(r))
	# determines direction
	theta = 2*np.random.random_sample(len(r))-1
	r += -lamb*np.log(r_raw)*theta
	ind += 1

print(theta_0)

multi_theta = np.array([theta_0, theta_1, theta_2])

print(N_sct)
print(N_true_sct)
print(np.sum(N_true_sct))
plt.hist(multi_theta, bins = 20, rwidth = 0.9, align='right', label = str(1))
plt.hist([], color='#ff7f0e', label=str(2))
plt.hist([], color='#2ca02c', label=str(3))
plt.legend()
plt.xlabel(r'$N_{sip}$')
plt.ylabel('N')
plt.xticks([0, np.pi/2, np.pi], ['0', r'$\pi/2$', r'$\pi$'])
plt.show()