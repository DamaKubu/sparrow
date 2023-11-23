import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
from scipy import stats
# Two-sided inverse Students t-distribution
from scipy.stats import t

# plt.figure()
# plt.subplot(311) #subplot(nrows, ncols, index, **kwargs)
# plt.scatter(x, y, s=0.0001)
# plt.subplot(312)

def plotLinearFit(x,y,xlabel='xlabel',ylabel='ylabel',s=0.05):
	# p - probability, df - degrees of freedom
	tinv = lambda p, df: abs(t.ppf(p/2, df))
	ts = tinv(0.05, len(x)-2)

	res = stats.linregress(x, y)
	Nuokrypis = f"slope (95%): {res.slope:.6f} +/- {ts*res.stderr:.6f} \n
	 intercept (95%): {res.intercept:.6f} +/- {ts*res.intercept_stderr:.6f}\n
	  using Students two-sided t-distribution"
	  
	plt.scatter(x,y,s,label='original data')
	plt.plot(x, res.intercept + res.slope*x, 'r', label=Nuokrypis)
	plt.legend()
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()



