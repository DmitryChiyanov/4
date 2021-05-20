import re


with open('file.txt', 'r') as final:
    for line in final:


        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]

        line = line.split(':', 1)
        print(line[0],sum(nums))









