import numpy as np
import time
import matplotlib.pyplot as plt

start = time.time()

p_s = []
m_s = []
err_s = []

rho_s = np.linspace(0.02, 8, 20)
# variable rho
for i in range(len(rho_s)):
	rho = rho_s[i]
	N_0 = 10**7
	samp = np.random.random_sample((3, N_0))
	samp_r_raw = np.sqrt(np.sum(samp**2, axis=0))
	samp_r = samp_r_raw**rho

	# true N sphere
	samp_1 = np.sum(samp**rho, axis=0)
	one_s = np.ones_like(samp_1)
	one_zero = np.less(samp_1, one_s)*1
	one_zero_N = np.less(samp_r_raw, one_s)*1
	N = np.sum(one_zero_N)
	# masa
	count = np.sum(one_zero)


	M = 4*np.pi / (3)
	err = 1/np.sqrt(N) * np.sqrt(abs(count/N-(count/N)**2)) * M
	m = count/N*M
	print(m)
	if m > 0:
		p_s.append(rho)
		m_s.append(m)
		err_s.append(err)

err_s = np.array(err_s)
m_s = np.array(m_s)
err_s_abs = err_s/m_s

fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
ax1.errorbar(p_s, m_s, yerr=err_s,fmt='.',capsize=3)
ax1.hlines(4*np.pi / 3, 0, rho)
#ax1.set_xscale('log')
#ax2.set_yscale('log')
#ax2.plot(p_s, err_s_abs, 'rx')

ax1.set_xlabel('n')
ax1.set_ylabel('m')
#ax2.set_ylabel(r'$\Delta m / m$', color='r')

plt.show()
