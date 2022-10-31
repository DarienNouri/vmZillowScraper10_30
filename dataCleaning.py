import urllib
import pandas as pd

import sqlalchemy
import numpy as np
import pyodbc
from urllib import parse
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

'''

get sql connection string parameters

'''

driver_name = ''
driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
if driver_names:
    driver_name = driver_names[0]
if driver_name:
    conn_str = 'DRIVER={}; ...'.format(driver_name)
    # then continue with ...
    # pyodbc.connect(conn_str)
    # ... etc.
else:
    print('(No suitable driver found. Cannot connect.)')
#driver = 'ODBC Driver 18 for SQL Server'
driver = driver_name
driver2 = '{SQL Server Native Client 11.0}'
server = 'tcp:zillow-db.database.windows.net'
database = 'zillow'
username = 'darien'
password = 'Amrikor11'


def getDaysOnZillowCol(variableData):
    dozList = []
    for i in variableData:
        dozList.append(i['text'])
    for i in range(len(dozList)):
        if 'days on Zillow' not in dozList[i]:
            dozList[i] = 'Nan'
        else:
            val = dozList[i].split()[0]
            dozList[i] = int(val)
    return dozList


def transformData(data):
    latLong = []
    variableData = []
    hdpData = []
    for i in data:
        latLong.append(i['latLong'])
        variableData.append(i['variableData'])
        hdpData.append(i['hdpData']['homeInfo'])
    df = pd.DataFrame.from_dict(data, orient='columns')
    if 'builderName' not in df:
        df['builderName'] = np.nan



    df1 = df[
        ['unformattedPrice', 'addressStreet', 'addressCity', 'addressState', 'addressZipcode', 'beds', 'baths', 'area',
         'sgapt', 'zestimate', 'brokerName', 'isFeaturedListing', 'builderName', 'utcDateTime', 'zpid', 'detailUrl']]
    df1['zpid'] = pd.to_numeric(df1['zpid'])
    keys = ['zpid', 'taxAssessedValue', 'latitude', 'longitude', 'datePriceChanged', 'rentZestimate', 'priceReduction',
            'priceChange', 'lotAreaValue']
    masterList = []
    for i in hdpData:
        listingDict = {}
        for key in keys:
            if key in i.keys():
                listingDict[key] = i[key]
        masterList.append(listingDict)
    # dozCol = getDaysOnZillowCol(variableData)
    # df1['daysOnZillow'] = dozCol
    df1['daysOnZillow'] = np.nan
    secondaryTable = pd.DataFrame(masterList)
    return pd.merge(df1, secondaryTable, left_on='zpid', right_on='zpid', how='left')


def saveToSQL(df):

    params = urllib.parse.quote_plus(
        'DRIVER={' + driver + '};Server=' + server + ';Database=' + database + ';Port=1433;uid=' + username + ';Pwd=' + password)
    engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={params}', fast_executemany=True)
    with engine.connect() as connection:
        df.to_sql('master', connection, if_exists='append', index=False, chunksize=1000)
