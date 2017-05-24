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
    x = np.arange(7, 26.5, 1.5)
    m1avg = [] #方法一的均值
    m1sd = [] #方法一的标准差
    m2avg = []  # 方法2的均值
    m2sd = []  # 方法2的标准差
    m3avg = []  # 方法3的均值
    m3sd = []  # 方法3的标准差
    m4avg = []  # 方法4的均值
    m4sd = []  # 方法4的标准差
    m5avg = []  # 方法5的均值
    m5sd = []  # 方法5的标准差
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')
            m1avg.append(float(line[1]))
            m1sd.append(float(line[2]))
            m2avg.append(float(line[3]))
            m2sd.append(float(line[4]))
            m3avg.append(float(line[5]))
            m3sd.append(float(line[6]))
            m4avg.append(float(line[7]))
            m4sd.append(float(line[8]))
            m5avg.append(float(line[9]))
            m5sd.append(float(line[10]))
    return x, m1avg, m1sd, m2avg, m2sd, m3avg, m3sd, m4avg, m4sd, m5avg, m5sd


def weekday_end(filename1):
    bar_width = 0.25
    opacity = 1
    error_config = {'ecolor': '0.3'}
    y = ['7:00-\n8:00', '8:00-\n9:00', '9:00-\n10:00', '10:00-\n11:00', '11:00-\n12:00', '12:00-\n13:00', '13:00-\n14:00',
         '14:00-\n15:00', '15:00-\n16:00', '16:00-\n17:00', '17:00-\n18:00', '18:00-\n19:00', '19:00-\n20:00']

    x, m1avg, m1sd, m2avg, m2sd, m3avg, m3sd, m4avg, m4sd, m5avg, m5sd = readFile(filename1)
    plt.subplots(figsize=(7, 8))
    plt.barh(x-bar_width*2., m1avg, bar_width, label='RVTR', xerr=m1sd, color='navy', error_kw=error_config, alpha=opacity, hatch='x')
    plt.barh(x- bar_width*1., m2avg, bar_width, label='SDD', xerr=m2sd, color='cornflowerblue', error_kw=error_config, alpha=opacity, hatch='+')
    plt.barh(x- bar_width*0, m3avg, bar_width, label='MDT', xerr=m3sd, color='yellowgreen', error_kw=error_config, alpha=opacity, hatch='\\\\')
    plt.barh(x+ bar_width*1, m4avg, bar_width, label='MTT', xerr=m4sd, color='darkorange', error_kw=error_config, alpha=opacity, hatch='///')
    plt.barh(x+ bar_width*2, m5avg, bar_width, label='MLR', xerr=m5sd, color='darkred', error_kw=error_config, alpha=opacity, hatch='-----')
    plt.ylim(6.1, 26.2)
    plt.yticks(x, y)

    plt.legend(loc=(0.78,0.55),prop={'size': 11})
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=14, weight='bold')
    #

#    plt.title(filename1.split('.')[0])  #标题
    plt.xlabel("Average AR value", fontsize=14, fontweight='bold')
    plt.ylabel("Time period", color='k', fontsize=14, fontweight='bold')
    plt.yticks(x, fontsize=11,rotation=14,weight='bold')
    plt.xticks((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8), weight='bold')
#    fontsize = 13
#    plt.text(x=5.2.csv, y=45, s="Percentage of road segments with the travel \n                 time-costs follow LNDs",
#             rotation='vertical', fontsize=fontsize, color='k', verticalalignment='center')
#    plt.text(x=21, y=45, s="Average speeds of road segments(km/h)", rotation='vertical', fontsize=fontsize, color='k',
#             verticalalignment='center')

    plt.show()

if __name__ == '__main__':
    filename1 = "tp.csv"
    weekday_end(filename1)

