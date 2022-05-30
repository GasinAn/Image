from scipy import stats
from matplotlib import pyplot as plt

def make_figure(figsize=(6, 6), dpi=800, mu=100, sigma=3, loc=0, scale=100):
    n = stats.poisson.rvs(mu, size=1)[0]
    x = stats.uniform.rvs(size=n)
    y = stats.uniform.rvs(size=n)
    s = stats.lognorm.rvs(sigma, loc=loc, scale=scale, size=n)
    c = stats.uniform.rvs(size=(n, 3))

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot()
    ax.scatter(x, y, s=s, c=c, edgecolors=None)

    ax.axis('square')
    ax.set_axis_off()

    plt.savefig('5.png', dpi=dpi, bbox_inches='tight', pad_inches=0)

if __name__ == '__main__':
    make_figure()
