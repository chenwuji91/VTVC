#-*- coding: UTF-8 -*-
'''
@author: chenwuji
计算只有一列的所有的均值
'''
rootPath = '../data/Final_result_lack_cars/'
import cwj.infocomSimulate.tools as tools
import glob
import numpy as np
import os
import math
def getFileList(filepath):
    flist = glob.glob(filepath + '/*')
    return flist

def countAvg(path):
    fList = getFileList(path)
    for eachF in fList:
        our = []
        if os.path.basename(eachF) == 'count.csv':
            os.remove(eachF)
            continue
        f = open(eachF)
        for eachLine in f:
            eachLine = eachLine.split('\n')[0]
            eachLine1 = eachLine.split(',')
            if eachLine == '':
                break
            our.append(float(eachLine1[0]))
        f.close()
        mean_our = np.mean(our)
        std_our = np.std(our)
        sqrtn = math.sqrt(len(our))
        ourN = std_our / sqrtn
        tools.writeToFile(path+'/count.csv', str(os.path.basename(eachF)) + ',' + str(mean_our) + ',' + str(ourN))

folder_list = getFileList(rootPath)
for eachf in folder_list:
    countAvg(eachf)

