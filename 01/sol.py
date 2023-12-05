import re
lines = open("in.txt").read().split("\n")

sum = 0
for line in lines:
    pattern = re.compile('[a-z|A-Z]')
    new_line = pattern.sub('', line)
    sum = sum + int(new_line[0] + new_line[-1])
print(sum)