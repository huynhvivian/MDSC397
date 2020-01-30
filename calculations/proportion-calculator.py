import sys
import re

#argument handling
bestTree = sys.argv[1]
if "BRCA1" in bestTree:
    filename = "BRCA1"
elif "APC" in bestTree:
    filename = "APC"
elif "EGFR" in bestTree:
    filename = "EGFR"
elif "OCA2" in bestTree:
    filename = "OCA2"
elif "PHEX" in bestTree:
    filename = "PHEX"
elif "TARS1" in bestTree:
    filename = "TARS1"

#create list for file line
with open(bestTree, 'r') as file:
    line = file.readline()
    final_list = re.split(':|,', line)
file.close()

#finding homo sapien newick number, assigning to variable
homo_sapien_distance = 0
while homo_sapien_distance == 0:
    for index in range(len(final_list)):
        if 'Homo' in final_list[index]:
            homo_sapien_distance = final_list[index + 1]
            if ')' in homo_sapien_distance:
                homo_sapien_distance = homo_sapien_distance.replace(")", "")
            if '(' in homo_sapien_distance:
                homo_sapien_distance = homo_sapien_distance.replace("(", "")
                
#adding total distance, exception will occur if index is not a number
count = 1
total_distance = 0
for number in final_list:
    if ')' in number:
        number = number.replace(")", "")
    if "(" in number:
        number = number.replace("(", "")
    try:
        float_num = float(number)
        total_distance += float_num
    except:
        count = 1

#calculate proportion value
proportion_value = (float(homo_sapien_distance))/(float(total_distance))

#print proportion value into another file
proportion_file = open(filename + 'proportion.txt', 'a')
proportion_file.write(str(proportion_value))
proportion_file.close()