import numpy
import matplotlib.pyplot as plt
import scipy.stats

mu = 0
sigma = 1
samples_size = [30, 50, 100, 500]
count_of_experiments = 1000

samples_var = []

for  i, samples_size in enumerate(samples_size):
    samples_var =  numpy.zeros(count_of_experiments)    
    for j in range (count_of_experiments):
        samples = numpy.random.normal(mu, sigma, samples_size)
        samples_var[j]=(numpy.var(samples, ddof=1))
    
    plt.subplot(1, 3, 1)
    plt.hist(samples_var, bins=30, density=True, label=str(samples_size))
    plt.title('Выборочная дисперсия')
    plt.xlabel('Значение')
    plt.ylabel('Частота')

    x = numpy.linspace(min(samples_var), max(samples_var), 100)
    y = scipy.stats.norm.pdf(x, loc= sigma**2, scale=numpy.sqrt((2*sigma**4)/samples_size))
    
    plt.plot(x, y, color='red')



plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()