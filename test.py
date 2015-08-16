f = open('data.txt', 'r')
data = f.read()
data = data.split('\n')
cver = data[0]
dver = data[1]
heroes = eval(data[2])
