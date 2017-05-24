#-*- coding: UTF-8 -*-
'''
@author: chenwuji
常用工具类
'''


rootPath = 'tp'
import cwj.infocomSimulate.tools as tools
import glob
import numpy as np
import os
import math
def getFileList(filepath):
    flist = glob.glob(filepath + '/*')
    return flist

def countAvg():
    fList = getFileList(rootPath)
    for eachF in fList:
        our = []
        other1 = []
        other2 = []
        other3 = []
        other4 = []
        fileList = getFileList(eachF)
        for eachFile in fileList:
            #求每个文件的均值
            f = open(eachFile)
            for eachLine in f:
                eachLine = eachLine.split('\n')[0]
                eachLine1 = eachLine.split(',')
                if eachLine == '':
                    break
                our.append(float(eachLine1[0]))
                other1.append(float(eachLine1[1]))
                other2.append(float(eachLine1[2]))
                other3.append(float(eachLine1[3]))
                other4.append(float(eachLine1[4]))
            f.close()

        mean_our = np.mean(our)
        mean_other1 = np.mean(other1)
        mean_other2 = np.mean(other2)
        mean_other3 = np.mean(other3)
        mean_other4 = np.mean(other4)

        std_our = np.std(our)
        std_other1 = np.std(other1)
        std_other2 = np.std(other2)
        std_other3 = np.std(other3)
        std_other4 = np.std(other4)

        sqrtn = math.sqrt(len(our))
        ourN = std_our / sqrtn
        other1N = std_other1 / sqrtn
        other2N = std_other2 / sqrtn
        other3N = std_other3 / sqrtn
        other4N = std_other4 / sqrtn

        tools.writeToFile('tp.csv', str(os.path.basename(eachF)) + ',' + str(mean_our) + ',' + str(ourN) + ',' + str(mean_other1) + ',' + str(other1N) + ','\
                          + str(mean_other2) + ',' + str(other2N) + ',' + str(mean_other3) + ',' + str(other3N) + ',' + str(mean_other4) + ',' + str(other4N))

countAvg()



# def get_data(path):
#     avg_our = []
#     avg_method1 = []
#     avg_method2 = []
#     avg_method3 = []
#     avg_method4 = []
#
#     f = open(path)
#     for eachline in f:
#         list = eachline.split('\r')[0].split('\n')[0].split(':')[1].split(';')
#         avg_our.append(float(list[0]))
#         avg_method1.append(float(list[1]))
#         # avg_method2.append(float(list[2.csv]))
#         avg_method3.append(float(list[3]))
#         # avg_method4.append(float(list[4]))
#     import numpy as np
#     # print np.mean(avg_our),
#     # print np.mean(avg_method1),
#     # print np.mean(avg_method2),
#     # print np.mean(avg_method3),
#     # print np.mean(avg_method4)
#     np.std(avg_our)
#     return np.mean(avg_our),np.mean(avg_method1),np.mean(avg_method2),\
#            np.mean(avg_method3),np.mean(avg_method4)


# import glob
# import os
# def file_list():
#     flist = []
#     f = glob.glob('data/Final_result/*')
#     for f1 in f:
#         if os.path.isfile(f1):
#             flist.append(f1)
#         else:
#             f2 = glob.glob(f1 + '/*')
#             for f3 in f2:
#                 flist.append(f3)
#     return flist
# import tools
# flist = file_list()
# for eachf in flist:
#     # print eachf,
#     # print get_data(eachf)
#     result = str(get_data(eachf))
#     tools.writeToFile('data/Final_result/final.csv', str(eachf)+ ',' + result[1:len(result)-1])