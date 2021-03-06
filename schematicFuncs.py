
# nuances of dynamic schematics

# keep track of time
# keep track of what the current schematic frame is
# keep track of how many frames the schematic goes through [per second] or [per single increment]

from listModification import ungroupListElements
from varStorage import *
import sys


class BaseSchematic:
	def __init__(self):
		self.createSchematic()


	def __iter__(self):
		return iter(self.schematic)

	
	def createSchematic(self):
		sys.exit("Please override createSchematic() method for the BaseSchematic class")


	def removeElements(self, *featureTypes):
		schematic = self.schematic
		for featureType in featureTypes:
			for schemSetN in range(len(schematic)):
				schematic[schemSetN]['features'][featureType] = []


class DynamicSchematic:
	def updateSchematic(self):
		sys.exit("Please override updateSchematic() method for the DynamicSchematic class")


def fillBlankSet(schemSet):
	default = {'features': {'points': [], 'lines': [], 'triangles': []},
	 'colors': {'point fill': '#F0F0F0', 'point outline': '#F0F0F0', 'line color': '#F0F0F0', 'triangle fill': '#F0F0F0', 'triangle outline': '#F0F0F0'},
	 'set specs': {'point size': 2, 'line width': 2, 'outline triangles': False}}
	for detailType in default:
		if detailType not in schemSet:
			schemSet[detailType] = default[detailType]
		else:
			for itemType in default[detailType]:
				if itemType not in schemSet[detailType]:
					schemSet[detailType][itemType] = default[detailType][itemType]
	return schemSet


def hasParent(classInstance, parentClassName):
	return parentClassName in [baseClass.__name__ for baseClass in classInstance.__class__.__bases__]


def createRunningLine(points, closeShape=False):
	if closeShape:
		points.append(points[0])
	
	lines = []
	for pointN in range(len(points)):
		point = points[pointN]
		if pointN > 0:
			lines.append([points[pointN][0], points[pointN-1][0]])

	return lines


def combineSchematics(addedSchematics=(), subtractedSchematics=()):
	for negSchem in subtractedSchematics:
		for posSchemN in range(len(addedSchematics)):
			posSchem = addedSchematics[posSchemN]
			
			addedSchematics[posSchemN] = combineSchemSets(addedSchemSets=posSchem, subtractedSchemSets=negSchem)
	
	finalSchematic = ungroupListElements(addedSchematics)
	return finalSchematic


def combineSchemSets(addedSchemSets=(), subtractedSchemSets=()):

    for negSchem in subtractedSchemSets:
	    for posSchemN in range(len(addedSchemSets)):
		    posSchem = addedSchemSets[posSchemN]
		    posSchem = subtractSchemSet(posSchem, negSchem)
		    addedSchemSets[posSchemN] = posSchem
    
    return addedSchemSets


# def subtractSchemSet(posSchemSet, negSchemSet):
#     for itemType in negSchemSet:
#         for item in negSchemSet[itemType]:
#             if item in posSchemSet[itemType]:
#                 posSchemSet[itemType].remove(item)


def subtractSchemSet(posSchemSet, negSchemSet):
	for detailType in negSchemSet:
		for itemType in negSchemSet[detailType]:
			for item in negSchemSet[detailType][itemType]:
				if item in posSchemSet[detailType][itemType]:
					posSchemSet[detailType][itemType].remove(item)


def updateRotation(ratesOfChange):
	timePassed = time.time() - renderVars.timeCreated
	thetas = [rateOfChange*timePassed for rateOfChange in ratesOfChange]
	return thetas



