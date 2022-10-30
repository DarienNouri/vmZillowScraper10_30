import locationParser
from run_scrape import run, createSaveName
import run_scrape
import dataCleaning


def main(url=None, startprice=None,all=None, test1 = False, test40 = False, testing960 = False):
    if url is not None:
        run(url)
    elif all is True:
        allLoc = locationParser.pullAll()
        count = 0
        for loc in allLoc:
            count += 1
            if count < 5:
               continue
            print('Current Location:', allLoc[loc][0][0])
            payload = run(presetFilters=allLoc[loc][0][1], testing=test40, testingLarge= testing960)
            print('len payload = ', len(payload))


            sqlReady = dataCleaning.transformData(payload)
            dataCleaning.saveToSQL(sqlReady)

            print("Finished Scraping:", print(allLoc[loc][0][0]))
            if test1 is True:
                break

    else:
        filters = locationParser.makeSelection()

        #print(filters[1]['price_min']['min'] = new_price)
        payload = run(presetFilters=filters[0][1], testing=test40)


        sqpReady = dataCleaning.transformData(payload)
        dataCleaning.saveToSQL(sqpReady)
        #saveName = createSaveName(filters)
        #run_scrape.saveJSON(payload, saveName)
        ##run_scrape.saveCSV(payload, saveName)
        print("letsgooobaby")




if __name__ == "__main__":
    main(all=True, test40=False, testing960=False)