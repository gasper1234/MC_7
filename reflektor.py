import numpy as np
import time
import matplotlib.pyplot as plt

lamb = 0.5
N_0 = 10**8

r_raw = np.random.random_sample(N_0)

# to other distribution
r = -lamb*np.log(r_raw)
one_s = np.ones_like(r)

N_sct = []
N_true_sct = [N_0]
while len(r)>0:
	one_s = np.ones_like(r)
	zero_s = np.zeros_like(r)
	zero_one = np.greater(r, zero_s)*1
	one_zero = np.less(r, one_s)*1
	r = r*one_zero*zero_one
	r = r[r != 0]
	N_sct.append(len(r))
	N_true_sct[-1] -= N_sct[-1]
	N_true_sct.append(N_sct[-1])
	r_raw = np.random.random_sample(len(r))
	# determines direction
	rand_dir = np.random.random_sample(len(r))
	dir_plus = np.greater(rand_dir, np.ones_like(rand_dir)*0.5)*1
	dir_minus = np.less(rand_dir, np.ones_like(rand_dir)*0.5)*(-1)
	r += -lamb*np.log(r_raw)*dir_plus
	r += -lamb*np.log(r_raw)*dir_minus

print(N_sct)
print(N_true_sct)
print(np.sum(N_true_sct))
plt.bar([i-0.25 for i in range(len(N_true_sct))], N_true_sct, width = 0.4, label='bi')

N_sct = []
N_true_sct = [100]

r_raw = np.random.random_sample(N_0)
theta_raw = np.random.random_sample(N_0)
theta = 2*theta_raw-1
r = -lamb*np.log(r_raw)



N_sct = []
N_true_sct = [N_0]
while len(r)>0:
	one_s = np.ones_like(r)
	zero_s = np.zeros_like(r)
	zero_one = np.greater(r, zero_s)*1
	one_zero = np.less(r, one_s)*1
	r = r*one_zero*zero_one
	r = r[r != 0]
	N_sct.append(len(r))
	N_true_sct[-1] -= N_sct[-1]
	N_true_sct.append(N_sct[-1])
	r_raw = np.random.random_sample(len(r))
	# determines direction
	theta = 2*np.random.random_sample(len(r))-1
	r += -lamb*np.log(r_raw)*theta

print(N_sct)
print(N_true_sct)
print(np.sum(N_true_sct))
plt.bar([i+0.25 for i in range(len(N_true_sct))], N_true_sct, width = 0.4, label='iso')
plt.yscale('log')
plt.xlabel(r'$N_{sip}$')
plt.ylabel('N')
plt.legend()
plt.show()