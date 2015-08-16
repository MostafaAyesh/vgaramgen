dataf = open('data.txt', 'r')
data = dataf.read()
data = data.split('\n')
cver, dver, heroes = data[0], data[1], eval(data[2])
dataf.close()
##
verf = open('ver.txt', 'r')
ver = verf.read()
ver = ver.split('\n')
cver_, dver_ = ver[0], ver[1]
verf.close()
##
