import numpy as np
import time
import matplotlib.pyplot as plt

start = time.time()

p_s = []
m_s = []
err_s = []

rho_s = np.linspace(0.02, 5, 4)
# variable rho
for p in range(len(rho_s)):
	rho = rho_s[p]
	N_0 = 10**6
	samp = np.random.random_sample((3, N_0))
	samp_xy = samp[:2]
	samp_r_raw = np.sqrt(np.sum(samp**2, axis=0))
	samp_J = np.sum(samp_xy**2, axis=0)
	samp_r = samp_r_raw**rho

	# true N sphere
	samp_1 = np.sum(samp**rho, axis=0)
	one_s = np.ones_like(samp_1)
	one_zero = np.less(samp_1, one_s)*1
	one_zero_N = np.less(samp_r_raw, one_s)*1
	N = np.sum(one_zero_N)
	# masa
	count = np.sum(one_zero*samp_J)
	print(count/N)


	J = 8*np.pi/(3*(5))
	j = count/N*J
	err = 1/np.sqrt(N) * np.sqrt(abs(count/N-(count/N)**2)) * J
	p_s.append(rho)
	m_s.append(j)
	err_s.append(err)

err_s = np.array(err_s)
m_s = np.array(m_s)
#err_s_abs = err_s/m_s


print(p_s, m_s, err_s)

fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
ax1.errorbar(p_s, m_s, yerr=err_s,fmt='.',capsize=3)
#ax1.set_xscale('log')
#ax2.set_yscale('log')
#ax2.plot(p_s, err_s_abs, 'rx')

ax1.set_xlabel('n')
ax1.hlines(8*np.pi/(3*(5)), 0, rho)
ax1.set_ylabel('J')
#ax2.set_ylabel(r'$\Delta$J / J', color='r')

plt.show()