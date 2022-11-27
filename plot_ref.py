import numpy as np
import time
import matplotlib.pyplot as plt

lamb = 0.5
N_0 = 8
r_raw = np.random.random_sample(N_0)

# to other distribution
r = np.zeros_like(r_raw)

#N_sct = []
#N_true_sct = [100]
scatt_array = [[-1, 0] for _ in range(len(r))]
for _ in range(10):
	r_raw = np.random.random_sample(len(r))
	if scatt_array[0][-1] == 0:
		r += -lamb*np.log(r_raw)
	# determines direction
	else:
		rand_dir = np.random.random_sample(len(r))
		dir_plus = np.greater(rand_dir, np.ones_like(rand_dir)*0.5)*1
		dir_minus = np.less(rand_dir, np.ones_like(rand_dir)*0.5)*(-1)
		r += -lamb*np.log(r_raw)*dir_plus
		r += -lamb*np.log(r_raw)*dir_minus
	for i in range(len(r)):
		if r[i] > 1:
			r[i] = 10000
		if r[i] < 0:
			r[i] = -10000
	for i in range(len(scatt_array)):
		if abs(scatt_array[i][-1]) < 1000:
			scatt_array[i].append(r[i])

print(scatt_array)
for i in range(len(scatt_array)):
	z_s = [i+j*0.19 for j in range(len(scatt_array[i]))]
	plt.plot(scatt_array[i], z_s, color='blue')
	plt.arrow(-0.1, i+0.18, 0.05, 0, shape='full', lw=0, length_includes_head=True, head_width=.2, head_length=.05, color='blue')

plt.vlines(0, 0, len(scatt_array), color='black')
plt.vlines(1, 0, len(scatt_array), color='black')
plt.ylim(0, len(scatt_array))
plt.xlim(-0.2, 1.2)
plt.show()