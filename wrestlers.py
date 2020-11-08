#Andrew Eppinger
#CS 325 Fall 2020
#Homework #5: Wrestling rivalries

import fnmatch          #fnmatch and os need to be imported to accomodate different names being used for the
import os               #input files
file_pattern = 'wrestler*'
files = os.listdir('./')
filename = ''
for file in files:
    if fnmatch.fnmatch(file,file_pattern):
        filename = file

content_list = []                   #Var to store the each line of the act.text file
cases = []           #Var to store the numbers from each line after they're converted to ints

text_file = open(filename, 'r')
input = []

for line in text_file:              #Iterates through each line of the text file, storing each line in a list

    line = line.split(' ')
    content_list.append(line)

wrestlers = []
matchups = []
#This portion of code organizes the data from the input file and makes it usable for the algorithm.
while len(content_list) > 0:
    w_length = int(content_list[0][0])
    content_list = content_list[1:]
    while w_length > 0:
        wrestlers.append(content_list[0][0].rstrip('\n'))
        content_list = content_list[1:]
        w_length -= 1
    m_length = int(content_list[0][0])
    content_list = content_list[1:]
    while m_length > 0:
        empty_list = []
        empty_list.append(content_list[0][0])
        empty_list.append((content_list[0][1].rstrip('\n')))
        matchups.append(empty_list)
        content_list = content_list[1:]
        m_length -= 1

results = ''
babyfaces = []
heels = []

for wrestler in matchups:
    if wrestler[0] not in babyfaces and wrestler[0] not in heels: #Checks if the first wrestler has been assigned a role
        if wrestler[1] in babyfaces:    #Checks if the potential rival has been assigned a role
            heels.append(wrestler[0])
        else:
            babyfaces.append(wrestler[0])
    if wrestler[1] not in babyfaces and wrestler[1] not in heels: #Checks if the second wrestler has been assigned a role
        if wrestler[0] in babyfaces:    #Checks if the first wrestler has been assigned a role
            heels.append(wrestler[1])
        elif wrestler[0] in heels:
            babyfaces.append(wrestler[1])
        else:
            babyfaces.append(wrestler[1])

babyfaces.sort()    #Sorts the lists to better match sample outputs. Has no bearing on results.
heels.sort()


#This portion of code checks if the rivals are in opposite roles. If they are, it checks the next matchup. If not,
#results are updated to impossible and the program stops checking becsause the rest of the rivalries are moot.
for wrestler in matchups:
    if wrestler[0] in babyfaces and wrestler[1] in heels or wrestler[0] in heels and wrestler[1] in babyfaces:
        pass
    else:
        results = 'Impossible'
        break

#If all rivalries are possible, the list of babyfaces and heels is printed to the console as required.
if results != 'Impossible':
    results = results + 'Yes Possible' + '\n' + 'Babyfaces: '
    for item in babyfaces:
        results = results + item + ' '
    results = results + '\n' + 'Heels: '
    for item in heels:
        results = results + item + ' '
print(results)