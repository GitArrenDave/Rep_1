import numpy as np
np.set_printoptions(threshold=np.inf)
file = open('firsttask.txt','r')
teacharray = np.loadtxt('firsttask.txt')
a = 450/2.64
b = 150-a*0.41

taskarray = a*teacharray+b
taskarray = np.round(taskarray)
taskarray = taskarray.astype(int)
print(taskarray)
content = file.read()
linenumb = content.split("\n")
file.close()
smoothlinenumb = len(linenumb)
for i in range(len(linenumb)-2):
    diff0 = abs(taskarray[i][0] - taskarray[i+1][0])
    diff1 = abs(taskarray[i][1] - taskarray[i+1][1])
    diff2 = abs(taskarray[i][2] - taskarray[i+1][2])
    diff3 = abs(taskarray[i][3] - taskarray[i+1][3])
    diff4 = abs(taskarray[i][4] - taskarray[i+1][4])
    diff5 = abs(taskarray[i][5] - taskarray[i+1][5])
    maxdiff = max([diff0, diff1, diff2, diff3, diff4, diff5])
    smoothlinenumb += maxdiff
print(smoothlinenumb)
def diff(zeile, spalte):
    differenz = abs(taskarray[zeile][spalte] - taskarray[zeile+1][spalte])
    return differenz

smotharray = [[],[],[],[],[],[]]


file2 = open('smoothtask.txt', 'w+')
#smotharray = np.around(smotharray,decimals=1)
smotharray[0].append(taskarray[1][0])
smotharray[1].append(taskarray[1][1])
smotharray[2].append(taskarray[1][2])
smotharray[3].append(taskarray[1][3])
smotharray[4].append(taskarray[1][4])
smotharray[5].append(taskarray[1][5])
print(len(smotharray), len(smotharray[0]), len(smotharray[1]), len(smotharray[2]), len(smotharray[3]))
for i in range(len(linenumb)-2):
    diff0 = round(abs(taskarray[i][0] - taskarray[i+1][0]))
    diff1 = round(abs(taskarray[i][1] - taskarray[i+1][1]))
    diff2 = round(abs(taskarray[i][2] - taskarray[i+1][2]))
    diff3 = round(abs(taskarray[i][3] - taskarray[i+1][3]))
    diff4 = round(abs(taskarray[i][4] - taskarray[i+1][4]))
    diff5 = round(abs(taskarray[i][5] - taskarray[i+1][5]))
    maxdiff = max([diff0, diff1, diff2, diff3, diff4, diff5])

    if maxdiff == 0:
        smotharray[0].append(taskarray[i+1][0])
        smotharray[1].append(taskarray[i+1][1])
        smotharray[2].append(taskarray[i+1][2])
        smotharray[3].append(taskarray[i+1][3])
        smotharray[4].append(taskarray[i+1][4])
        smotharray[5].append(taskarray[i+1][5])
        #print(len(smotharray), len(smotharray[0]), len(smotharray[1]), len(smotharray[2]), len(smotharray[3]))
    else:
        for j in range(6):
            if diff(i,j) == maxdiff:
                if (taskarray[i][j] - taskarray[i+1][j]) < 0:
                    smotharray[j].extend(list(range(taskarray[i][j], taskarray[i+1][j])))
                elif (taskarray[i][j] - taskarray[i+1][j]) > 0:
                    smotharray[j].extend(list(range(taskarray[i][j], taskarray[i+1][j], -1)))

            elif diff(i,j) < maxdiff: 
                if (taskarray[i][j] - taskarray[i+1][j]) < 0:
                    smotharray[j].extend(list(range(taskarray[i][j], taskarray[i+1][j])))
                    smotharray[j].extend([ taskarray[i+1][j] for _ in range(diff(i,j), maxdiff)])
                elif (taskarray[i][j] - taskarray[i+1][j]) > 0:
                    smotharray[j].extend(list(range(taskarray[i][j], taskarray[i+1][j], -1)))
                    smotharray[j].extend([ taskarray[i+1][j] for _ in range(diff(i,j), maxdiff)])
                elif (taskarray[i][j] - taskarray[i+1][j]) == 0:
                    smotharray[j].extend([ taskarray[i+1][j] for _ in range(maxdiff)])
#print(len(smotharray), len(smotharray[0]), len(smotharray[1]), len(smotharray[2]), len(smotharray[3]))

                
        

smotharray = np.array(smotharray)
smotharray = smotharray.transpose()
print(taskarray)
#print(smotharray, smotharray.shape)
content = str(smotharray)

file2.write(content)
file2.close()

