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
    with open('locationPresets', 'r') as f:
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


'''
urls = [
    'https://www.zillow.com/in/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22IN%22%2C%22mapBounds%22%3A%7B%22west%22%3A-91.4016041484375%2C%22east%22%3A-81.4809498515625%2C%22south%22%3A36.7736736493365%2C%22north%22%3A42.690126823103746%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A22%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/il/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22IL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-94.2268341484375%2C%22east%22%3A-84.3061798515625%2C%22south%22%3A36.77320388582392%2C%22north%22%3A42.68969575159318%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A21%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/ga/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-88.1386241484375%2C%22east%22%3A-78.2179698515625%2C%22south%22%3A29.410489061347363%2C%22north%22%3A35.888676851129794%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/tn/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22TN%22%2C%22mapBounds%22%3A%7B%22west%22%3A-90.9389261484375%2C%22east%22%3A-81.0182718515625%2C%22south%22%3A32.65264838481152%2C%22north%22%3A38.89475131181936%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A53%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/ky/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22KY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-90.7285671484375%2C%22east%22%3A-80.8079128515625%2C%22south%22%3A34.73089322948658%2C%22north%22%3A40.812251959763714%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/id/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22ID%22%2C%22mapBounds%22%3A%7B%22west%22%3A-124.063915296875%2C%22east%22%3A-104.222606703125%2C%22south%22%3A39.95773004841326%2C%22north%22%3A50.73434934903154%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D',
    'https://www.zillow.com/in/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22IN%22%2C%22mapBounds%22%3A%7B%22west%22%3A-91.4016041484375%2C%22east%22%3A-81.4809498515625%2C%22south%22%3A36.7736736493365%2C%22north%22%3A42.690126823103746%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A22%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/mi/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22MI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-96.191207796875%2C%22east%22%3A-76.349899203125%2C%22south%22%3A39.40206315968311%2C%22north%22%3A50.27514875875683%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A30%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D',
    'https://www.zillow.com/nm/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NM%22%2C%22mapBounds%22%3A%7B%22west%22%3A-110.98639564843751%2C%22east%22%3A-101.06574135156251%2C%22south%22%3A30.97033160664985%2C%22north%22%3A37.33721088053735%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/az/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22AZ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-116.89123414843749%2C%22east%22%3A-106.97057985156249%2C%22south%22%3A30.972463688445323%2C%22north%22%3A37.339187909587%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/wa/?searchQueryState=%7B%22usersSearchTerm%22%3A%22AZ%22%2C%22mapBounds%22%3A%7B%22north%22%3A49.84833516606865%2C%22east%22%3A-115.92194985156252%2C%22south%22%3A44.6253606986997%2C%22west%22%3A-125.8426041484375%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A59%2C%22regionType%22%3A2%7D%5D%2C%22pagination%22%3A%7B%7D%7D',
    'https://www.zillow.com/nc/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.8213211484375%2C%22east%22%3A-74.9006668515625%2C%22south%22%3A31.9755588439819%2C%22north%22%3A38.26846388286548%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A36%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/sc/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22SC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.40677807421875%2C%22east%22%3A-78.44645092578125%2C%22south%22%3A32.02145613346853%2C%22north%22%3A35.22710108724415%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D',
    'https://www.zillow.com/ms/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22MS%22%2C%22mapBounds%22%3A%7B%22west%22%3A-94.83677564843751%2C%22east%22%3A-84.91612135156251%2C%22south%22%3A29.302380089810924%2C%22north%22%3A35.78812362106955%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A34%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/mt/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22MT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-119.965437296875%2C%22east%22%3A-100.124128703125%2C%22south%22%3A41.19233819284999%2C%22north%22%3A51.751894103860955%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A35%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D',
    'https://www.zillow.com/ut/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22UT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-116.50735514843751%2C%22east%22%3A-106.58670085156251%2C%22south%22%3A36.51241068433742%2C%22north%22%3A42.45032859617213%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A55%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/wi/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22WI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-94.5298176484375%2C%22east%22%3A-84.6091633515625%2C%22south%22%3A42.16148017025017%2C%22north%22%3A47.611820615093635%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A60%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/wv/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22WV%22%2C%22mapBounds%22%3A%7B%22west%22%3A-85.1420176484375%2C%22east%22%3A-75.2213633515625%2C%22south%22%3A35.88321819882303%2C%22north%22%3A41.87238163976872%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A61%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D',
    'https://www.zillow.com/washington-dc/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Washington%2C%20DC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-77.32459644677735%2C%22east%22%3A-76.70455555322266%2C%22south%22%3A38.70610688776046%2C%22north%22%3A39.08073843844797%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41568%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A1036%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
]



for link in urls:
    locationPresets.addLocations(link)





with open('locationPresets.json', 'r') as f:
    presets = json.load(f)
for i in presets:
    print(i.keys())




'''
