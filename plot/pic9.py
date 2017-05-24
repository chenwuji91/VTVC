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
error_config = {'ecolor': '0.3'}
fontsize1=13
fontsizeyaxis=13
fontlegendtext=10
fontlegend=10
fontxaxis=13


def readFile1(filename):
    y1 = [] #line
    y2 = [] #bar
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')
            y1.append(float(line[1]))
            y2.append(float(line[2]))
    x = np.arange(0, 0.6, 0.3)
    return x, y1, y2
def readFile2(filename):
    y1 = [] #line
    y2 = [] #bar
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')
            y1.append(float(line[1]))
            y2.append(float(line[2]))
    x = np.arange(0, 1.5, 0.22)
    return x, y1, y2
def readFile3(filename):
    x = np.arange(7, 20, 1)
    y1 = [] #line
    y2 = [] #bar
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')
            y1.append(float(line[1]))
            y2.append(float(line[2]))
    return x, y1, y2


def line_bar_1(x,y1,y2,ax1):
    ax1.plot(figsize=(8, 6))
    ax1.bar(x[0], y1[0], width=0.07, hatch='x', yerr=y2[0], error_kw=error_config, label='Normal vehicle', color='navy')
    ax1.bar(x[1], y1[1], width=0.07, hatch='+', yerr=y2[1], error_kw=error_config, label='Suspicious vehicle', color='cornflowerblue')
    ax1.set_xlim(-0.1, 0.47)
    ax1.set_ylim(0, 0.87)
    ax1.set_xticks([])

    plt.yticks(weight='bold',fontsize=fontsizeyaxis)
    ax1.set_xlabel('Vehicle type', fontsize=fontxaxis, fontweight='bold')
    ax1.set_ylabel("Average number of query times per road segment                                         ", fontsize=fontsize1, fontweight='bold'  )

    ax1.legend(loc='upper left', prop={'size': fontlegend})
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=fontlegendtext, weight='bold')
    ax1.set_title('(I)', weight='bold')


def line_bar_2(x,y1,y2,ax1):
    ax1.bar(x[0], y1[0], width=0.07, hatch='x', yerr=y2[0], error_kw=error_config, label='Intensive area', color='navy')
    ax1.bar(x[1], y1[1], width=0.07, hatch='+', yerr=y2[1], error_kw=error_config, label='Medium sparse area', color='cornflowerblue')
    ax1.bar(x[2], y1[2], width=0.07, hatch='\\', yerr=y2[2], error_kw=error_config, label='Sparse area', color='yellowgreen')
    ax1.set_xlim(-0.05, 0.55)
    ax1.set_ylim(0.0, 1.05)
    ax1.set_xticks([])
    ax1.set_xlabel('Distribution of video \nsurveillance cameras', fontsize=fontsize1, fontweight='bold')
    ax1.set_ylabel("Average number of query\n times  per road segment", fontsize=fontsize1, fontweight='bold')
#    plt.xticks((0.03, 0.25, 0.46),('Intensive\n area','Half sparse\n area', 'Sparse\n area'), fontsize=fontxaxis, weight='bold')
    ax1.legend(loc='upper left', prop={'size': fontlegend})
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=fontlegendtext, weight='bold')
    plt.yticks(weight='bold', fontsize=fontsizeyaxis)
    ax1.set_title('(II)', weight='bold')


def line_bar_3(x,y1,y2,ax1):
    l = ax1.errorbar(x, y1, color='navy', yerr=y2, ecolor='0.3', linewidth=4, elinewidth=2.3)
    ax1.grid()
    y = ['7:00-\n8:00', '8:00-\n9:00', '9:00-\n10:00', '10:00-\n11:00', '11:00-\n12:00', '12:00-\n13:00',
         '13:00-\n14:00', '14:00-\n15:00', '15:00-\n16:00', '16:00-\n17:00', '17:00-\n18:00', '18:00-\n19:00', '19:00-\n20:00']
    y1 = ['7:00-\n8:00', '9:00-\n10:00', '11:00-\n12:00', '13:00-\n14:00', '15:00-\n16:00', '17:00-\n18:00', '19:00-\n20:00']
    ax1.set_xlabel("Time period", fontsize=fontxaxis, fontweight='bold')
#    ax1.set_ylabel("Average number of query \n times per road segment", fontsize=fontsize1, fontweight='bold', horizontalalignment='right')
    plt.xticks((7, 9, 11, 13, 15, 17, 19), y1, weight='bold', fontsize=13, rotation= 0)
#   plt.xticks((7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), y, weight='bold', fontsize=9, rotation=40)
    plt.yticks((0,0.1,0.2,0.3,0.40, 0.50, 0.60, 0.7,0.80),weight='bold', fontsize=fontsizeyaxis)
    ax1.set_xlim(6.7, 20.0)
    ax1.set_title('(III)', weight='bold')

#    ax1.set_ylim(0.9, 1.0)
#    ax1.set_yticks((0.900, 0.925, 0.950, 0.975, 1.000))
#    plt.grid()


def weekday_end(filename1, filename2, filename3):
    x1, y11, y12 = readFile1(filename1)
    x2, y21, y22 = readFile2(filename2)
    x3, y31, y32 = readFile3(filename3)

    fig = plt.figure()


    ax1 = fig.add_subplot(221)

    line_bar_1(x1, y11, y12, ax1)
    ax2 = fig.add_subplot(222)
    line_bar_2(x2, y21, y22, ax2)
    ax3 = fig.add_subplot(212)
    line_bar_3(x3, y31, y32, ax3)
    plt.subplots_adjust(wspace=0.4, hspace=0.3)

    plt.show()

if __name__ == '__main__':
    filename1 = "img91.csv"
    filename2 = "img92.csv"
    filename3 = "img9.csv"
    weekday_end(filename1, filename2, filename3)

