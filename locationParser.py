import collections
import json
from tabulate import tabulate
from devFile import DecodeUrl


def addLocations(link):
    with open('locationPresets.json', 'r') as f:
        presets = json.load(f)
    decoder = DecodeUrl(link)
    u = decoder.decode_url()
    filters = decoder.get_url_filters(u)
    location_dict = {u['searchQueryState']['usersSearchTerm']: filters}
    presets.append(location_dict)
    print(presets)
    with open('locationPresets.json', 'w') as f:
        json.dump(presets, f)
        f.close()


def makeSelection():
    with open('locationPresets.json', 'r') as f:
        presets = json.load(f)
    dataDict = {}

    table = []
    count = 0
    for i in presets:
        dataDict[count] = list(i.items())
        count += 1

    for key, value in dataDict.items():
        selections = (str(key) + ': ' + str(value[0][0]))
        table.append([str(key), str(value[0][0])])
    print(tabulate(table, headers=["Index", "City/State"]))
    print("Enter an index")
    selectedIndex = int(input())
    row = dataDict[selectedIndex]
    cityState = row[0]
    metrics = row[0][1]
    # decoder = DecodeUrl()
    # setFilters = decoder.set_url_filters(metrics)
    return row


def pullAll():
    with open('locationPresets.json', 'r') as f:
        presets = json.load(f)
    dataDict = {}

    table = []
    count = 0
    for i in presets:
        dataDict[count] = list(i.items())
        count += 1
    return dataDict


def selectByState():
    with open('locationPresets.json', 'r') as f:
        presets = json.load(f)
    dataDict = {}
    selectionDict =  {}
    table = []
    count = 0
    count1 = 0
    for i in presets:

        key, value = next(iter(i.items()))

        dataDict[key] = value
        count += 1
    presets = collections.OrderedDict(sorted(dataDict.items()))
    for key, value in presets.items():
        selectionDict[count1] = [key,value]
        count1 +=1

    for key, value in selectionDict.items():
        selections = (str(key) + ': ' + str(value[0]))
        table.append([str(key), str(value[0])])
    print(tabulate(table, headers=["Index", "City/State"]))
    print("Select States")
    selectedIndex = (input())
    selectedIndex = selectedIndex.split(" ")
    returnList = []
    for i in selectedIndex:
        returnList.append(selectionDict[int(i)])
    return returnList

