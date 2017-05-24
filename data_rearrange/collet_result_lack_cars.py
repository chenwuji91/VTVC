#-*- coding: UTF-8 -*-
'''
@author: chenwuji
路段评分程序
'''
import os
import cwj.infocomSimulate.evaluateRoute as er
import cwj.infocomSimulate.tools

sep = os.path.sep
import glob
def getFileList(filepath):
    flist =  glob.glob(filepath + sep + '*')
    return flist


def read_our_method(other_method_root):
    flist1 = glob.glob('../data_lack_cars/' + other_method_root + '/*')
    flist = []
    one_result_set = {}
    for eachlist in flist1:
        if os.path.isfile(eachlist):
            read_our_result(eachlist, one_result_set)
        f1 = glob.glob(eachlist + '/*')
        flist = flist + f1

    # print flist
    for each_file in flist:
        # print each_file
        read_our_result(each_file, one_result_set)
    return one_result_set

def read_our_result(filename_of_one, resultSet):

    print filename_of_one
    f = open(filename_of_one)
    init_query_times = 0
    for eachline in f:
        if len(eachline.split(',')) < 2:
            continue
        eachline = eachline.split('\n')[0].split('\r')[0]
        fileName = eachline.split(',real path:')[0]
        realPatht = eachline.split(',real path:')[1].split(',predict path:')[0]
        predictPatht = eachline.split(',real path:')[1].split(',predict path:')[1].split(',query times:')[0]
        query_times = int(eachline.split(',query times:')[1].split(',')[0])
        query_times = query_times - init_query_times
        init_query_times = int(eachline.split(',query times:')[1].split(',')[0])

        finalScore = eachline.split(',real path:')[1].split(',predict path:')[1].split(',final score:')[1]

        realPatht = realPatht.split(',')
        realPath = []
        for eachl in realPatht:
            eachl = eachl.split('\'')[1]
            realPath.append(eachl)

        predictPatht = predictPatht.split(',')
        predictPath = []
        for eachl in predictPatht:
            eachl = eachl.split('\'')[1]
            predictPath.append(eachl)
        resultSet.setdefault(fileName,(realPath, predictPath,query_times, finalScore))

    f.close()

def get_file_date(one_file_path, result_set):
    f = open(one_file_path)
    basename = os.path.basename(one_file_path)
    time = ''
    for eachline in f:

        if len(eachline.split(',')) > 2:
            time = eachline.split(',')[2].split('\"time\": \"')[1].split('\"')[0]
            break
    result_set.setdefault(basename, time)


def collect_file_date():
    flist = glob.glob('../data/Result/proto_data/*')
    one_result_set = {}
    for each_file in flist:
        get_file_date(each_file, one_result_set)
    return one_result_set


dict_all = {}
num_list = ['10','20','30','40','50','60','70','80','90']
for each_num in num_list:
    dict_all.setdefault(each_num,read_our_method(each_num))
     # our_method = read_our_method('our_method')
# date_dict = collect_file_date()
# print len(our_method)
# print len(date_dict)


def removeDir():
    import os
    import shutil
    rootdir = '../data/Final_result'
    filelist = os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join(rootdir, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print filepath + " removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            print "dir " + filepath + " removed!"

# removeDir()





def classify_result_by_date():
    for eachl in dict_all:
        our_method = dict_all.get(eachl)
        for each_method in our_method:
             # try:
                our = er.evaluateFunc(our_method.get(each_method)[0], our_method.get(each_method)[1])
                query_times = float(our_method.get(each_method)[2])/float(len(our_method.get(each_method)[0]))
                our = our[0]/float(len(our_method.get(each_method)[0])) * our[0]/float(len(our_method.get(each_method)[1]))
                cwj.infocomSimulate.tools.makeDir('../data/Final_result_lack_cars/'+ eachl + '/')
                cwj.infocomSimulate.tools.writeToFile('../data/Final_result_lack_cars/'+ eachl + '/Final_result_lack_cars', str(our))
                cwj.infocomSimulate.tools.writeToFile('../data/Final_result_lack_cars/'+ eachl + '/Final_result_lack_cars' + '_query_times', str(query_times))
             # except:
             #    continue


classify_result_by_date()

if __name__ == '__main__':
    pass
