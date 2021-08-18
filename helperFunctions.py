def ungroupListElements(outerList):
    ungrouped = []
    for subList in outerList:
        for item in subList:
            ungrouped.append(item)
    return ungrouped


def groupListElements(givenList, groupSize):
    if len(givenList) % groupSize != 0:
        sys.exit("func groupListElements: list not evenly divisible by group size")

    groupedList = []
    for groupN in range(len(givenList) // groupSize):
        innerList = []
        for itemN in range(groupSize):
            innerList.append(givenList[groupN * groupSize + itemN])

        groupedList.append(innerList)

    return groupedList


def countSharedElements(listA=(), listB=(), orderMatters=True):
    sharedElements = 0
    if orderMatters:
        for index in range(len(listA)):
            if listA[index] == listB[index]:
                sharedElements += 1

    if not orderMatters:
        for item in listA:
            if item in listB:
                sharedElements += 1

    return sharedElements


def combineSchematics(addedSchematics=(), subtractedSchematics=()):
    finalSchematic = {}
    for schematic in addedSchematics:
        for itemType in schematic:
            for item in schematic[itemType]:
                if itemType in finalSchematic:
                    finalSchematic[itemType].append(item)
                if itemType not in finalSchematic:
                    finalSchematic[itemType] = []

    for schematic in subtractedSchematics:
        for itemType in schematic:
            for sItem in schematic[itemType]:
                for item in finalSchematic[itemType]:
                    if countSharedElements(item, sItem, orderMatters=False) == len(item):
                        if sItem in finalSchematic[itemType]:
                            finalSchematic[itemType].remove(sItem)

    return finalSchematic


