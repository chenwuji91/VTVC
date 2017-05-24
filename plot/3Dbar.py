from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def readFile(filename):
    z_value = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').strip('\n').split(',')
            z_value.append(float(line[1]))
    return z_value

if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    dz = readFile('3d.csv')
    colors = ['navy', 'cornflowerblue',  'yellowgreen', 'darkorange', 'darkred', 'pink']
    #colors = ['navy', 'navy', 'cornflowerblue', 'cornflowerblue',  'yellowgreen', 'yellowgreen']
    hatchs = ['x', '+', "\\", '/', '-', '|']
    fontsize = 14
    xpos = [0, 1]*3
    ypos = [0, 0, 1, 1, 2, 2]
    zpos = [0]*6
    dx = 0.3
    dy = 0.5
    for i in range(len(xpos)):
        ax.bar3d(xpos[i], ypos[i], zpos[i], dx, dy, dz[i], hatch=hatchs[i], color=colors[i])
    ax.set_zlabel('Average AR value', fontsize=fontsize, weight='bold')
    ax.set_xticklabels(['Normal vehicle', '', '', '',  'Suspicious vehicle'], fontsize=fontsize, weight='bold')
    ax.set_yticklabels(['Intensive area', '', 'Medium sparse area', '', 'Sparse area'], fontsize=fontsize, weight='bold')
    ax.set_zticks(np.arange(0, 0.9, 0.1))
    ax.set_zticklabels(np.arange(0, 1, 0.1), fontsize=fontsize, weight='bold')
    # ax.text3D(2.csv., 0.3, -0.6, 'Average AR value', zdir='z', rotation=150, fontsize=fontsize, weight='bold')
    # ax.grid()
    plt.show()
