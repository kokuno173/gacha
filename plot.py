import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def plot_sample(sample, bins=20, xlim=(0., 1.), element='step'):
    bin_min = np.round(np.sort(sample, axis=0)[int(0.001*sample.shape[0])], decimals=2)
    bin_min = np.floor(bin_min*10)/10
    bin_max = np.round(np.sort(sample, axis=0)[int(0.999*sample.shape[0])], decimals=2)
    bin_max = np.ceil(bin_max*10)/10

    hist_max = []
    for i in range(sample.shape[1]):
        hist = np.histogram(sample[:, i], bins=bins, range=(bin_min[i], bin_max[i]), density=True)
        hist_max.append(np.max(hist[0]))
    hist_max = max(hist_max)
    if hist_max <= 5:
        hist_max = np.ceil(hist_max)
    elif hist_max <= 10:
        hist_max = np.ceil(hist_max/2)*2
    elif hist_max <= 20:
        hist_max = np.ceil(hist_max/5)*5
    else:
        hist_max = np.ceil(hist_max/10)*10
    

    plt.figure(figsize=(10, 6))
    plt.suptitle('Prior Distribution')

    plt.subplot(321)
    plt.plot(sample[:, 0], label='R', color='blue')
    plt.xlabel(''), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(322)
    sns.histplot(sample[:, 0], stat='density', bins=bins, binrange=(bin_min[0], bin_max[0]),
                label='R', color='blue', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim((0, hist_max))
    plt.legend()

    plt.subplot(323)
    plt.plot(sample[:, 1], label='SR', color='red')
    plt.xlabel(''), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(324)
    sns.histplot(sample[:, 1], stat='density', bins=bins, binrange=(bin_min[1], bin_max[1]),
                label='SR', color='red', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim((0, hist_max))
    plt.legend()

    plt.subplot(325)
    plt.plot(sample[:, 2], label='SSR', color='green')
    plt.xlabel('iteration'), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(326)
    sns.histplot(sample[:, 2], stat='density', bins=bins, binrange=(bin_min[2], bin_max[2]),
                label='SSR', color='green', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim((0, hist_max))
    plt.legend()

    plt.tight_layout()

    plt.show()
