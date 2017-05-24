#-*- coding: UTF-8 -*-
'''
@author: liangbinxin
作图bar-line
'''
import numpy as np
import matplotlib.pyplot as plt
PATH = "C:\\Users\\Administrator\\Desktop\\"
COLORS = (
    'greenyellow','lightpink', 'deepskyblue', 'goldenrod', 'aquamarine', 'blueviolet', 'r', 'brown', 'g', 'b', 'y', 'c', 'm', 'k' )
N = 10
def readFile(filename):
    x = np.arange(7.1, 20.1, 0.1)
    y1 = [] #line
    y2 = [] #bar
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')
            y1.append(float(line[1]))
            y2.append(float(line[2]))
    return x, y1, y2

def line_bar(x,y1,y2,filename):
    #plt.figure(1,figsize=(8, 4))
    fig, ax1 = plt.subplots(figsize=(12, 4.5))
    l, = ax1.plot(x, y1, color='red')
    l.set_antialiased(False)#锯齿效果
    ax1.set_title(filename.split('.')[0])
    ax1.set_xlabel("Time")
    ax1.set_ylabel("percentage of road segments with the \n travel time-costs follow LNDs", color='k')
    ax1.set_xlim(7.0, 20.0)
    ax1.set_ylim(0.9, 1.0)
    ax1.set_yticks((0.900, 0.925, 0.950, 0.975, 1.000))
    ax1.grid()

    ax2 = ax1.twinx()
    for i in range(len(x)):
        ax2.bar(x[i], y2[i], width=0.05, label="speed", edgecolor=COLORS[i/N], color=COLORS[i/N])

    ax2.set_ylabel("Average speeds of road segments", color='k')
    ax2.set_xlim(7.0, 20.0)
    ax2.set_ylim(50.0, 70.0)
    ax2.grid()

    #plt.legend()
    plt.show()
    plt.savefig(filename.split('.')[0]+".pdf")

def line_bar_1(x,y1,y2,filename1,ax1,xylabel=True):
    fontsize = 14
    l, = ax1.plot(x, y1, color='red')
    l.set_antialiased(False)#锯齿效果
    ax1.set_title(filename1.split('.')[0], fontsize=fontsize, weight='bold')
    ax1.set_xlabel("Time", fontsize=fontsize, weight='bold')

    ax1.set_xlim(7.0, 20.0)
    ax1.set_ylim(0.9, 1.0)
    #ax1.set_yticks()
    plt.yticks((0.900, 0.925, 0.950, 0.975, 1.000), weight='bold', fontsize=fontsize)
    plt.xticks(weight='bold', fontsize=fontsize)
    plt.grid()

    ax2 = plt.twinx()

    for i in range(len(x)):
        ax2.bar(x[i], y2[i], width=0.05, label="speed", edgecolor=COLORS[i/N], color=COLORS[i/N])
    if xylabel:
        """
        fontsize = 10
        ax1.set_ylabel("percentage of road segments with the travel time-costs follow LNDs", fontsize=fontsize,
                   color='k')
        ax2.set_ylabel("Average speeds of road segments(km/h)", fontsize=fontsize, color='k')
        """

    ax2.set_xlim(7.0, 20.0)
    ax2.set_ylim(20.0, 40.0)
    ax2.set_yticklabels(np.arange(20, 40), fontsize=fontsize, weight='bold')
    #ax2.set_yticks(range(16, 25, 2.csv))
    ax2.grid()

def weekday_end(filename1,filename2):
    x1, y1, y2 = readFile(filename1)
    x2, y3, y4 = readFile(filename2)
    ax1 = plt.subplot(211)
    line_bar_1(x1, y1, y2, filename1, ax1, xylabel=False)
    ax2 = plt.subplot(212)
    line_bar_1(x2, y3, y4, filename2, ax2)
    plt.subplots_adjust(hspace=0.4, left=0.16)
    fontsize = 14
    plt.text(x=4.7, y=45, s="Percentage of road segments with the travel \n                 time-costs follow LNDs",
             rotation='vertical', fontsize=fontsize, color='k', verticalalignment='center', weight='bold')
    plt.text(x=20.8, y=45, s="Average speeds of road segments(km/h)", rotation='vertical', fontsize=fontsize, color='k',
             verticalalignment='center', weight='bold')
    plt.show()

if __name__ == '__main__':
    filename1 = "weekdays.csv"
    filename2 = "weekends.csv"
    # x, y1, y2 = readFile(filename1)
    # x, y3, y4 = readFile(filename2)
    weekday_end(filename1, filename2)

