#-*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def readFile(filename):
    x = np.arange(1,6,1)
    y1 = []
    y1err = []
    y2 = []
    y2err = []
    y3 = []
    y3err = []
    with open(filename,'r') as f:
        for line in f:
            line = line.split(',')
            y1.append(float(line[1]))
            y1err.append(float(line[2]))
            y1.append(float(line[3]))
            y1err.append(float(line[4]))
            y1.append(float(line[5]))
            y1err.append(float(line[6]))
            y1.append(float(line[7]))
            y1err.append(float(line[8]))
            y1.append(float(line[9]))
            y1err.append(float(line[10]))
    y2 = y1[5:10]
    y2err = y1err[5:10]
    y3 = y1[10:15]
    y3err = y1err[10:15]
    y1 = y1[0:5]
    y1err = y1err[0:5]
    return x, y1, y1err, y2, y2err, y3, y3err

def f(filename1):
    bar_width = 0.125*5/3
    fig, ax = plt.subplots(figsize=(8, 6))
    x, y1, y1err, y2, y2err, y3, y3err = readFile(filename1)
    opacity = 1
    error_config = {'ecolor': '0.3'}  #erroebar的颜色
    rect1 = ax.bar( x + bar_width * 0, y1, bar_width, label = 'Intensive area', color = 'navy', yerr = y1err, error_kw = error_config, alpha = opacity, hatch='x')
    rect2 = ax.bar( x + bar_width * 1, y2, bar_width, label = 'Half sparse area', color = 'cornflowerblue', yerr = y2err, error_kw = error_config, alpha = opacity, hatch='+')
    rect3 = ax.bar( x + bar_width * 2, y3, bar_width, label = 'Sparse area', color = 'yellowgreen', yerr = y3err, error_kw = error_config, alpha = opacity, hatch='\\')
    ax.set_ylabel('Average AR value', fontsize=14, fontweight='bold')
    ax.set_xlabel('Solution', fontsize=14, fontweight='bold')
    ax.set_ylim(0,0.9)
    ax.set_xlim(0.8,5.8)
    ax.set_xticks(x + bar_width * 1.5)
    ax.set_xticklabels(('RVTR','SDD','MDT','MTT','MLR'), fontsize=11, fontweight='bold')
    #ax.set_yticks((0,0.1,0.2.csv,0.3,0.4,0.5,0.6,0.7,0.8,0.9))
    plt.yticks((0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),fontsize = 11, weight = 'bold')

    plt.legend(prop={'size': 9})
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=12, weight='bold')
    plt.show()
    
if __name__ == '__main__':
    filename1 = "img5.csv"
    f(filename1)

