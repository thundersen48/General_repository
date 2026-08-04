import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sts



plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (10,7)
mu = 1
sigma = 0.5

# loc - параметр среднего, scale - параметр среднеквадратичного отклонения
norm_rv = sts.norm(loc=mu, scale=sigma)
np.linspace(-1, 3, 100)
x = np.linspace(-1, 3, 100)
norm_cdf = norm_rv.cdf(x)
#plt.figure(figsize=(10,7))
plt.plot(x, norm_cdf)
plt.title('Normal RV CDF')
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$F(x)$', fontsize=16)
plt.show()
