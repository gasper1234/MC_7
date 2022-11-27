import numpy as np
import time
import matplotlib.pyplot as plt

lamb_s = np.linspace(0.2, 1, 20)
N_0 = 10**6

neg_s = []
pos_s = []
for lamb in lamb_s:
	r_raw = np.random.random_sample(N_0)
	theta_raw = np.random.random_sample(N_0)
	theta = 2*theta_raw-1
	r = -lamb*np.log(r_raw)

	N_sct = []
	N_true_sct = [N_0]
	neg = 0
	pos = 0
	while len(r)>0:
		one_s = np.ones_like(r)
		zero_s = np.zeros_like(r)
		zero_one = np.greater(r, zero_s)*1
		neg += len(zero_one)-np.sum(zero_one)
		one_zero = np.less(r, one_s)*1
		pos += len(one_zero)-np.sum(one_zero)
		r = r*one_zero*zero_one
		r = r[r != 0]
		N_sct.append(len(r))
		N_true_sct[-1] -= N_sct[-1]
		N_true_sct.append(N_sct[-1])
		r_raw = np.random.random_sample(len(r))
		# determines direction
		theta = 2*np.random.random_sample(len(r))-1
		r += -lamb*np.log(r_raw)*theta
	print(pos+neg)
	neg_s.append(neg/N_0)
	pos_s.append(pos/N_0)

plt.plot(lamb_s, neg_s, label='odboj')
plt.plot(lamb_s, pos_s, label='prepust')
plt.legend()
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$N/N_0$')
plt.show()

