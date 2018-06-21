import math


filePATH = 'cifFiles/CLR.cif.txt'

arrLines = []

with open(filePATH) as fP:

    for line in fP:

        #print(line)
        arrLines.append(line)

indexStart = 0
i = 0
indexEnd = 0

coordSubSet = []

for item in arrLines:
    i = i + 1
    if '_chem_comp_atom.pdbx_ordinal' in item:
        indexStart = arrLines. index(item)
    if '_chem_comp_bond.comp_id' in item:
        indexEnd = arrLines.index(item)

#print("START ", indexStart, "AND END ", indexEnd)

coordSubSet = arrLines[indexStart:indexEnd]

#print(len(arrLines), " AND TRUNCATED ", len(coordSubSet))

dictAtomCoord = {}

lenArr = []
#80 len line
for csSet in coordSubSet:
    #print("MY ITEM", csSet)
    if len(csSet) >= 80:
        #print("THAT IS A COORDINATE STRING", csSet)
        strBefore = csSet
        strAfter =  " ".join(csSet.split())
        #print(strBefore, "\n \n", strAfter)
        tmpSplitStr = strAfter.split(' ')
        #print("COORDS", tmpSplitStr[9:12])
        coord = tmpSplitStr[12:15]
        key = tmpSplitStr[1].strip()

        if key not in dictAtomCoord:
            dictAtomCoord[key] = coord

'''for key in dictAtomCoord:
    print(key, dictAtomCoord[key])'''

dictSetManualMadeByMe = {1 : {'set':['O1', 'C2', 'C3', 'C4'], 'coord' : {}, 'middle' : []},
                         2 : {'set':['C1', 'C2', 'C3', 'C4', 'C5', 'C10'], 'coord' : {}, 'middle' : []},
                         3: {'set':['C5', 'C5', 'C7', 'C8', 'C9', 'C10', 'C19'], 'coord' : {}, 'middle' : []},
                         4: {'set':['C8', 'C9', 'C11', 'C12', 'C13', 'C14'], 'coord' : {}, 'middle' : []},
                         5: {'set':['C18'], 'coord' : {}, 'middle' : []},
                         6: {'set' : ['C13', 'C14', 'C15', 'C16', 'C17'], 'coord' : {}, 'middle' : []},
                         7: {'set':['C20', 'C21', 'C22', 'C23'], 'coord' : {}, 'middle' : []},
                         8: {'set' : ['C24', 'C25', 'C26', 'C27'], 'coord' : {}, 'middle' : []}}

#centroid = average(x), average(y), average(z)


for key in dictSetManualMadeByMe:
    for item in dictSetManualMadeByMe[key]['set']:
        #print('ITEM NO', item)
        if item not in dictSetManualMadeByMe[key]['coord']:
            #print(item)
            #print("TEST ITEM INSIDE", dictAtomCoord[item])
            arrayValue = dictAtomCoord[item]
            dictSetManualMadeByMe[key]['coord'][item] = arrayValue

'''for key in dictSetManualMadeByMe:
    for item in dictSetManualMadeByMe[key]['coord']:
        print(key)
        print("TEST COORD SET UP IN BIG DICT", item, " THE KEY AND THE DATA ", dictSetManualMadeByMe[key]['coord'][item])'''
for key in dictSetManualMadeByMe:
    i = len(dictSetManualMadeByMe[key]['set'])
    sumX = 0.0
    sumY = 0.0
    sumZ = 0.0
    for item in dictSetManualMadeByMe[key]['coord']:
        #print(item)
        sumX = float(sumX) + float(dictSetManualMadeByMe[key]['coord'][item][0])
        sumY = float(sumY) + float(dictSetManualMadeByMe[key]['coord'][item][1])
        sumZ = float(sumZ) + float(dictSetManualMadeByMe[key]['coord'][item][2])

    #print('The values of the X, Y, Z', sumX, sumY, sumZ)

    middlePoint = [sumX/i, sumY/i, sumZ/i]

    dictSetManualMadeByMe[key]['middle'] = middlePoint

###############TEST

'''for key in dictSetManualMadeByMe:
    print("SUPERTEST", dictSetManualMadeByMe[key]['coord'], "\n", dictSetManualMadeByMe[key]['middle'])'''

#########################

#Connections dictionary, as given in itp file

dictConnect = {1: {'seedConnected':[2], 'dist':{}},
               2: {'seedConnected':[3, 4], 'dist':{}},
               4: {'seedConnected':[6,7], 'dist':{}},
               5: {'seedConnected':[6], 'dist':{}},
               6: {'seedConnected':[7], 'dist':{}},
               7: {'seedConnected':[8], 'dist':{}}
               }#'''

#FINDING THE DISTANCE BETWEEN THE POINTS IN 3D

for key in dictConnect:
    point1 = dictSetManualMadeByMe[key]['middle']
    for item in dictConnect[key]['seedConnected']:
        point2 = dictSetManualMadeByMe[item]['middle']
        distanceBetweenThePoints = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)
        keyDist = str(key) + ' ' + str(item)
        if keyDist not in dictConnect[key]['dist']:
            dictConnect[key]['dist'][keyDist] = distanceBetweenThePoints

############ Test of the distance


for i in dictConnect:
    for k in dictConnect[i]['dist']:
        print('THE CONNECTION: ', k, "AND THE DISTANCE: ", dictConnect[i]['dist'][k]/10)