import math


filePATH = 'cifFiles/PRED.pdb'

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
    if 'start' in item:
        indexStart = arrLines. index(item)
    if 'CONECT' in item:
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
        coord = tmpSplitStr[-6:-3]
        key = tmpSplitStr[2].strip()

        if key not in dictAtomCoord:
            dictAtomCoord[key] = coord

'''for key in dictAtomCoord:
    print(key, dictAtomCoord[key])'''

dictSetManualMadeByMe = {1 : {'set':['O14', 'C13', 'C12', 'C11'], 'coord' : {}, 'middle' : []},
                         2 : {'set':['C10', 'C12'], 'coord' : {}, 'middle' : []},
                         3: {'set':['C02', 'C11'], 'coord' : {}, 'middle' : []},
                         4: {'set':['C', 'C01', 'C02', 'C04', 'C03', 'C05', 'C19'], 'coord' : {}, 'middle' : []},
                         5: {'set':['O09', 'C08', 'C20', 'C'], 'coord' : {}, 'middle' : []},
                         6: {'set' : ['C20', 'C08', 'C', 'C05', 'C16', 'C18'], 'coord' : {}, 'middle' : []},
                         7: {'set':['C26', 'C16', 'C18', 'C07', 'C06'], 'coord' : {}, 'middle' : []},
                         8: {'set' : ['C17'], 'coord' : {}, 'middle' : []},
                         9: {'set':['O', 'C26', 'C06', 'C16'], 'coord' : {}, 'middle' : []},
                         10: {'set': ['O23', 'C25', 'C22', 'C26'], 'coord': {}, 'middle': []},
                         11: {'set': ['O24', 'C22', 'C25', 'C26'], 'coord': {}, 'middle': []},
                         }

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

    keySpecial = [1, 5, 9, 10, 11]

    if key in keySpecial:
        keyOxygen = ''
        for item in dictSetManualMadeByMe[key]['set']:
            if 'O' in item:
                keyOxygen = item
        dictSetManualMadeByMe[key]['middle'] = [float (x) for x in dictAtomCoord[keyOxygen]]
    else:
        dictSetManualMadeByMe[key]['middle'] = middlePoint

###############TEST'''

#for key in dictSetManualMadeByMe:
    #print("SUPERTEST OF ", key,  " ", dictSetManualMadeByMe[key]['coord'], "\n", dictSetManualMadeByMe[key]['middle'])#'''

#########################

#Connections dictionary, as given in itp file

dictConnect = {1: {'seedConnected':[2, 3], 'dist':{}},
               2: {'seedConnected':[3, 4], 'dist':{}},
               3: {'seedConnected':[4], 'dist':{}},
               4: {'seedConnected':[6], 'dist':{}},
               5: {'seedConnected':[6], 'dist':{}},
               6: {'seedConnected':[7], 'dist':{}},
               7: {'seedConnected':[8, 9], 'dist':{}},
               9: {'seedConnected': [10, 11], 'dist': {}},
               10: {'seedConnected': [11], 'dist': {}}
               }#'''

#FINDING THE DISTANCE BETWEEN THE POINTS IN 3D'''

for key in dictConnect:
    point1 = dictSetManualMadeByMe[key]['middle']
    print(point1)
    for item in dictConnect[key]['seedConnected']:
        point2 = dictSetManualMadeByMe[item]['middle']
        distanceBetweenThePoints = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)
        keyDist = str(key) + ' ' + str(item)
        if keyDist not in dictConnect[key]['dist']:
            dictConnect[key]['dist'][keyDist] = distanceBetweenThePoints

############ Test of the distance


for i in dictConnect:
    for k in dictConnect[i]['dist']:
        print('THE CONNECTION: ', k, "AND THE DISTANCE: ", dictConnect[i]['dist'][k]/10)#'''