import numpy as np
import time
import matplotlib.pyplot as plt


N_s = []
m_s = []
err_s = []

rho_s = np.linspace(0, 2, 10)
# variable rho
for p in range(2, 9):
	N = 10**p
	samp = np.random.random_sample((3, N))

	# true N sphere
	samp_1 = np.sum(np.sqrt(samp), axis=0)
	one_s = np.ones_like(samp_1)
	one_zero = np.less(samp_1, one_s)*1

	# masa
	count = np.sum(one_zero)


	M = 8
	err = 1/np.sqrt(N) * np.sqrt(count/N-(count/N)**2) * M
	m = count/N*M
	print(m)
	if m > 0:
		N_s.append(N)
		m_s.append(m)
		err_s.append(err)

err_s = np.array(err_s)
m_s = np.array(m_s)
err_s_abs = err_s/m_s

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.errorbar(N_s, m_s, yerr=err_s,fmt='.',capsize=3)
ax1.set_xscale('log')
ax2.set_yscale('log')
ax2.plot(N_s, err_s_abs, 'rx')

ax1.set_xlabel('N')
ax1.set_ylabel('m')
ax2.set_ylabel(r'$\Delta m / m$', color='r')

plt.show()
