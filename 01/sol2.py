import re
lines = open("in.txt").read().split("\n")

re_array = [re.compile('one'),  re.compile('two'),  re.compile('three'),
            re.compile('four'), re.compile('five'), re.compile('six'),
            re.compile('seven'),re.compile('eight'),re.compile('nine')]

sum = 0
for line in lines:

    pos_array = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    pos_array[0] = line.find('one')
    pos_array[1] = line.find('two')
    pos_array[2] = line.find('three')
    pos_array[3] = line.find('four')
    pos_array[4] = line.find('five')
    pos_array[5] = line.find('six')
    pos_array[6] = line.find('seven')
    pos_array[7] = line.find('eight')
    pos_array[8] = line.find('nine')

    if(len([pos for pos in pos_array if pos > -1]) > 0):
        min_pos = min([pos for pos in pos_array if pos > -1])
        for i in range(len(pos_array)):
            if pos_array[i] == min_pos:
                line = re_array[i].sub(str(i+1),line,count=1)

    pos_array = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    pos_array[0] = line.rfind('one')
    pos_array[1] = line.rfind('two')
    pos_array[2] = line.rfind('three')
    pos_array[3] = line.rfind('four')
    pos_array[4] = line.rfind('five')
    pos_array[5] = line.rfind('six')
    pos_array[6] = line.rfind('seven')
    pos_array[7] = line.rfind('eight')
    pos_array[8] = line.rfind('nine')

    if(len([pos for pos in pos_array if pos > -1]) > 0):
        max_pos = max([pos for pos in pos_array if pos > -1])
        for i in range(len(pos_array)):
            if pos_array[i] == max_pos:
                line = re_array[i].sub(str(i+1),line,count=1)

    pattern = re.compile('[a-z]')
    new_line = pattern.sub('', line)
    sum = sum + int(new_line[0] + new_line[-1])
print(sum)