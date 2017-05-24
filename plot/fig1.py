#-*- coding: UTF-8 -*-
'''
@author: liangbinxin
作图bar-line
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf

def readFile(filename):
    method = [[],[],[],[],[]]
    errorbar = [[],[],[],[],[]]
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
    labels = ['RVTR', 'SDD', 'MDT', 'MST', 'MLR']
    colors = ['navy', 'cornflowerblue', 'yellowgreen', 'darkorange', 'darkred']
    markers = ['p', 'D', 'o', 's', '^' ]
    linestyles = ['dashed', '-', '--', '-.', ':']
    method, yerr = readFile('img1.csv')
    x = range(1, 11)
    fig, ax = plt.subplots(figsize=(8, 6))
    lines = []
    for i in range(len(method)):
        l, e, b = ax.errorbar(x, method[i], elinewidth=2.3, linewidth=4, marker=markers[i], markersize=8, color=colors[i],  yerr=yerr[i], ls=linestyles[i])
        lines.append(l)
    fontsize = 14

    plt.xticks(range(1, 11), weight='bold')
    #ax.set_xticks(range(1, 11))
    ax.set_xlim(0, 11)
    plt.yticks(np.arange(0., 0.81, 0.1), weight='bold')
    #ax.set_yticks(np.arange(0., 0.8, 0.1))
    ax.axvspan(0.5, 5.5, facecolor='c', edgecolor='c', alpha=0.25)
    ax.axvspan(5.5, 10.5, facecolor='pink', edgecolor='pink', alpha=0.25)

    pr = mf.FontProperties(weight='bold', size=fontsize)
    ax.legend(lines, labels, prop=pr, bbox_to_anchor=(0.98, 0.12), numpoints=2, columnspacing=0.8, ncol=5)
    ax.text(x=1.8, y=0.75, s="weekends                          weekdays", fontsize=fontsize, rotation='horizontal', verticalalignment='top', weight='bold')
    #ax.set_title("  weekends                               weekdays", fontsize=fontsize)
    ax.set_xlabel("Day", fontsize=fontsize, weight='bold')
    ax.set_ylabel("Average AR value", fontsize=fontsize, weight='bold')
    ax.grid()
    plt.show()





