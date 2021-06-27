from matplotlib import pyplot as plt
import seaborn as sns

def plot_sample(sample, bins=20, xlim=(0., 1.), ylim=(0., 10.), element='step'):
    plt.figure(figsize=(10, 6))
    plt.suptitle('Prior Distribution')

    plt.subplot(321)
    plt.plot(sample[:, 0], label='R', color='blue')
    plt.xlabel(''), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(322)
    sns.histplot(sample[:, 0], stat='density', bins=bins, binrange=(0,1),
                label='R', color='blue', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim(ylim)
    plt.legend()

    plt.subplot(323)
    plt.plot(sample[:, 1], label='SR', color='red')
    plt.xlabel(''), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(324)
    sns.histplot(sample[:, 1], stat='density', bins=bins, binrange=(0,1),
                label='SR', color='red', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim(ylim)
    plt.legend()

    plt.subplot(325)
    plt.plot(sample[:, 2], label='SSR', color='green')
    plt.xlabel('iteration'), plt.ylabel('p')
    plt.xlim((0, sample.shape[0])), plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')

    plt.subplot(326)
    sns.histplot(sample[:, 2], stat='density', bins=bins, binrange=(0,1),
                label='SSR', color='green', element=element)
    plt.xlabel('p'), plt.ylabel('pdf')
    plt.xlim(xlim), plt.ylim(ylim)
    plt.legend()

    plt.tight_layout()

    plt.show()
