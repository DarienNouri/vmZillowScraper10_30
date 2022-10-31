from devFile import DecodeUrl
from bs4 import BeautifulSoup
import requests
import json
import html
import time
from devFile import DecodeUrl

import nest_asyncio
import traceback
import pandas as pd
nest_asyncio.apply()
from datetime import datetime

import os


import csv


##'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'



req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'zguid=23|%24ca6368b9-7b92-4d51-ab67-c2be89065efd; _ga=GA1.2.1460486079.1621047110; _pxvid=7fa13d96-b528-11eb-9860-0242ac120012; _gcl_au=1.1.2025797213.1621047113; __gads=ID=66253ab863481044:T=1621047113:S=ALNI_MZr3mehwm2Wjo7NOrmalVtEcJSXag; __pdst=50987f626deb4767a53b5d8ca2ea406a; _fbp=fb.1.1621047115574.1019382068; _pin_unauth=dWlkPU5EVm1PRGRpTVRBdE5UTTFaUzAwWlRBNExUZzJZall0TWpZMU1HWTBNV0ppWlRkbA; G_ENABLED_IDPS=google; userid=X|3|231a9d744e104379%7C3%7CiEt8bkUx9hWaFeyCeAwN9tHl_T0d0Cq-kynGuEvNYr4%3D; loginmemento=1|c2274ba4a4ad76bbe89263d30695c182e9177b9c40a2691f3054987d66a944be; zjs_user_id=%22X1-ZU158jhpb2klds9_4wzn7%22; zgcus_lbut=; zgcus_aeut=189997416; zgcus_ludi=b44a961b-c7ef-11eb-a48f-96824e7eff50-18999; optimizelyEndUserId=oeu1623111792776r0.8778663892923859; _cs_c=1; WRUIDAWS=3326630244368428; visitor_id701843=248614376; visitor_id701843-hash=4be116fbd77089f953bfb6eaf5996ef92662a6ef7d237d3c49f154ffaf4eaa9295c64fb254b106bdff234e183c94498c01af2aab; __stripe_mid=80125db1-17d1-4fc5-ae37-86b12a68709cf3da6d; g_state={"i_p":1627697570928,"i_l":4}; zjs_anonymous_id=%22ca6368b9-7b92-4d51-ab67-c2be89065efd%22; _gac_UA-21174015-56=1.1626042638.Cj0KCQjwraqHBhDsARIsAKuGZeH8gi095UkXfohW-WWvyLosdmTdL8cfJwgAabYF9hS2XU6JlXqpWLcaAq5SEALw_wcB; _gcl_aw=GCL.1626042640.Cj0KCQjwraqHBhDsARIsAKuGZeH8gi095UkXfohW-WWvyLosdmTdL8cfJwgAabYF9hS2XU6JlXqpWLcaAq5SEALw_wcB; zgsession=1|1edd82e6-372a-4546-bc8b-c2bbadfd29b4; DoubleClickSession=true; fbc=fb.1.1626412984774.IwAR2QM6bzrTskAWN5Sk8UnmPlAxb1HRy1h1GRch888QqXfczHZZWb2vDZfIw; _fbc=fb.1.1626413249162.IwAR2QM6bzrTskAWN5Sk8UnmPlAxb1HRy1h1GRch888QqXfczHZZWb2vDZfIw; _csrf=lV2BBFim7Vy2gFTn--PUt0VA; _gaexp=GAX1.2.w27igyYtRQaAa8XQM3MjDw.18837.2!VDVoDKTnRcyv8f4FAcJ8PA.18915.2!Khnq27RoQmSe5DEusmh5xA.18913.3; _gid=GA1.2.705011419.1630004829; FSsampler=707279376; __CT_Data=gpv=26&ckp=tld&dm=zillow.com&apv_82_www33=26&cpv_82_www33=26&rpv_82_www33=13; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+27+2021+12%3A39%3A52+GMT-0600+(Mountain+Daylight+Time)&version=5.11.0&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false; _cs_id=41cbdc9c-bb0b-aad9-9521-b1328a65ff77.1623111795.22.1630089665.1630089591.1.1657275795752; utag_main=v_id:01796deff9e3001a59964343177e03079002907100838$_sn:41$_se:2$_ss:0$_st:1630255637884$dc_visit:38$ses_id:1630253822479%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:2%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:7b8796ca-44dd-45c9-97d9-bcb642d04cd1%3Bexp-session; JSESSIONID=6CB8C410E0FE216644E8C3A0D0851618; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEklf443J474nftKzJe5PKLD80sujgHvySB7tGcqZunX3BDDH9VwceMqGMTPC54%2F0q4CH%2BfmwsC6P; KruxPixel=true; _derived_epik=dj0yJnU9ai1PSUp1eHZ2Y3J3d0c2NVU1N3BBOFlHbnRBOGFzT0smbj1vLWRISDFwdUNoblN5MjQ4cTVyN213Jm09MSZ0PUFBQUFBR0VzRjRVJnJtPTEmcnQ9QUFBQUFHRXNGNFU; KruxAddition=true; search=6|1632872450375%7Crect%3D40.241821806991595%252C-103.77545313688668%252C39.18758562803622%252C-106.02765040251168%26disp%3Dmap%26mdm%3Dauto%26type%3Dhouse%252Cmultifamily%252Ctownhouse%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%0911093%09%09%09%09%09%09; _uetsid=d5e0465006a011ecbe3bd1a0f1c47d01; _uetvid=987e1c70c40a11ebaed8859af36f82fb; _px3=ba45c3df5d5d63d4d9780a102253cd60b21ab52b04778344e332e05474011c21:oCvapPXE6jD0rCXhSf4UjtEC2U956148EDyiWwRFOF8z5vwK63/hC8OWsk09O61g1spnZw64iXApZu1wOmKpyA==:1000:68UzJ5+ar5XwNm61bm41bhSHp8Zp1PfQQlL/5tcqdUIJ3RmA106//vvYGewCCwmln6acqbDAVKgqfB8Th05yX0Cw0TBW7dhfNdeNRjp9bxeLvKqZ56yuW+aVoYYp/zj6MNKv9c16vKlP771xSdCgUTvZ0CDmh7Ng55sHugOHt/jj+2Zmp2WLnuYR4rf7SEndqWBbAyQhhG4BKeyrZyEMpA==; AWSALB=3BIj2fUDeYgoAcLKaZdMkcyTzWSof62v91DQuCssJMyknlpZWcRcVnUU5Me29AcnFcjg1k9H2ehS6N0rSwxo4w8lmEvFCy6hgQfKm1HH8oVoWtpICS36NoLMMxmZ; AWSALBCORS=3BIj2fUDeYgoAcLKaZdMkcyTzWSof62v91DQuCssJMyknlpZWcRcVnUU5Me29AcnFcjg1k9H2ehS6N0rSwxo4w8lmEvFCy6hgQfKm1HH8oVoWtpICS36NoLMMxmZ',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'


}
req_headers1 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951 Safari/537.36'
}


def run(url=None, presetFilters=None, startprice=None, testing = False, testingLarge = False):
    global decoder, raw_dict


    if presetFilters is None:
        decoder = DecodeUrl(url)  # get_link())

        raw_dict = decoder.decode_url()
        if startprice is not None:
            filters = decoder.get_url_filters(raw_dict, startprice)
        else:
            filters = decoder.get_url_filters(raw_dict)

        integrate_filters = decoder.set_url_filters(filters)
    else:
        decoder = DecodeUrl()
        integrate_filters = decoder.set_url_filters(presetFilters)

    count = 0

    start_time = time.time()  ##testing
    localStorage = []
    end = False
    listing_count = 0
    print("Crawl Initiated")

    while end is False:
        count += 1
        if testing is True:
            numPages = 2
        else:
            numPages = 24


        for i in range(1, numPages):  # times out after 25th page, so loop with new price
            if end is True:
                break
            try:
                time.sleep(12)
                url = decoder.generate_url(integrate_filters, i)
                r = requests.get(url=url, headers=req_headers1)
                #try:
                data = json.loads(r.text)
                #print(r.text[:2000])
                #except:
                    #break
                listings = data['cat1']['searchResults']['listResults']
                for card in listings:
                    current_price = card['unformattedPrice']

                    card['utcDateTime'] = str(datetime.utcnow())
                    if len(localStorage) > 5:
                        if current_price < localStorage[-4]['unformattedPrice'] - 10:
                            localStorage.pop(-1)
                            print('Reached Last Page')
                            end = True
                            break
                    localStorage.append(card)

            except:
                print()
                print(traceback.format_exc())
                end = True
                print(len(localStorage))
                break
        time.sleep(1)
        try:
            new_price = localStorage[-1]['unformattedPrice']
            print("Listing Count:", len(localStorage))
            print(new_price)
        except:
            #print(str(soup)[:4000])
            break
        if presetFilters is None:
            update_link = decoder.get_url_filters(raw_dict, new_price)
        else:
            presetFilters[1]['price_min']['min'] = new_price
            update_link = presetFilters



        integrate_filters = decoder.set_url_filters(update_link)
        if testing is True:
            break
        if testingLarge is True and count == 4:
            break
    print("Number of Listings Scraped: ", len(localStorage))
    print(time.time() - start_time)
    return localStorage


def createSaveName(filters):
    d = datetime.now()
    date = d.date()
    h_m = str(d.time()).split(':')[:2]
    hour_min = h_m[0] + "_" + h_m[1]
    s = str(date).split('-')
    date = s[0] + "_" + s[1] + "_" + s[2]
    saveDateTime = date + "_" + hour_min
    savelocation = filters[0][0]
    saveName = savelocation + "_" + saveDateTime
    return saveName

def saveJSON(payload, saveName):
    savePath = os.getcwd()+'\dataJson'
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    with open(os.path.join(savePath, saveName + '.json'), "w") as f:
        json.dump(payload, f, indent=4)

def saveCSV(payload, saveName):
    savePath = os.getcwd()+'\dataCSV'

    if not os.path.exists(savePath):
        os.makedirs(savePath)
    with open(os.path.join(savePath, saveName + '.csv'), "w") as csv_file:
        df = pd.DataFrame(payload)
        df.to_csv(csv_file)





# link = 'https://www.zillow.com/new-york-ny/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.49741171289062%2C%22east%22%3A-73.46195028710937%2C%22south%22%3A40.32354617219259%2C%22north%22%3A41.07006558882081%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A10000000%7D%2C%22mp%22%3A%7B%22min%22%3A51479%7D%7D%2C%22isListVisible%22%3Atrue%7D'

# run(link)
