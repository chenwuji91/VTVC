#-*- coding: UTF-8 -*-
'''
@author: liangbinxin
作图bar-line
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf
y = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']


def readFile(filename):
    method = [[],[],[]]
    errorbar = [[],[],[]]
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').strip('\r').split(',')
            for i, value in enumerate(line[1:]):
                if i % 2:
                    errorbar[i/2].append(float(value))
                else:
                    method[i/2].append(float(value))
    return method, errorbar


if __name__ == "__main__":
    labels = ['Sparse', 'Medium sparse', 'Intensive']
    colors = ['navy', 'cornflowerblue', 'yellowgreen']
    markers = ['p', 'D', 'o']
    linestyles = ['dashed', '-', '--']
    method, yerr = readFile('fig8-2.csv')
    x = range(1, 10)
    fig, ax = plt.subplots(figsize=(8, 6))
    lines = []
    for i in range(len(method)):
        l, e, b = ax.errorbar(x, method[i], elinewidth=2.3, linewidth=4, marker=markers[i], markersize=8, color=colors[i],  yerr=yerr[i], ls=linestyles[i])
        lines.append(l)
    fontsize = 14

    plt.xticks((1,2,3,4,5,6,7,8,9), y, weight='bold')
    #ax.set_xticks(range(1, 11))
    ax.set_xlim(0, 10)
    plt.yticks(np.arange(0., 0.81, 0.1), weight='bold')
    #ax.set_yticks(np.arange(0., 0.8, 0.1))

    pr = mf.FontProperties(weight='bold', size=fontsize)
    ax.legend(lines, labels, prop=pr, bbox_to_anchor=(0.967, 0.11), numpoints=2, columnspacing=0.8, ncol=5)
#    ax.text(x=1.8, y=0.75, s="weekends                          weekdays", fontsize=fontsize, rotation='horizontal', verticalalignment='top', weight='bold')
    ax.set_xlabel("Percentage", fontsize=fontsize, weight='bold')
    ax.set_ylabel("Query Times", fontsize=fontsize, weight='bold')
    ax.grid()
    plt.show()
    plt.savefig('fig2.eps')





