# imports
from bs4 import BeautifulSoup
import requests
import csv

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: greyhound-data.com
def main():

    fobj = open('greyhound-data.csv', 'w')      # open file
    csvw = csv.writer(fobj, delimiter = ';')      # create csv writer, set delimiter to ;

    for year in range(2000,2016,1):

        ghd_ir_url = "http://www.greyhound-data.com/db.php?masterbreeders=3&raceland=IE&year="+str(year)+"&mindist=0&maxdist=unlimited&go=+calculate+new+statistic+"     # ireland / 2000
        ghd_uk_url = "http://www.greyhound-data.com/db.php?masterbreeders=3&raceland=UK&year="+str(year)+"&mindist=0&maxdist=unlimited&go=+calculate+new+statistic+"     # england / 2000
        ghd_us_url = "http://www.greyhound-data.com/db.php?masterbreeders=3&raceland=US&year="+str(year)+"&mindist=0&maxdist=unlimited&go=+calculate+new+statistic+"     # usa / 2000
        ghd_au_url = "http://www.greyhound-data.com/db.php?masterbreeders=3&raceland=AU&year="+str(year)+"&mindist=0&maxdist=unlimited&go=+calculate+new+statistic+"     # australia / 2000


        # IRELAND

        content = getPage(ghd_ir_url).find("table")
        content = content.findAll("tr", { "align" : "right" })

        for c in content:
            c = c.findAll("td")
            txt = ["Ireland;" + str(year)]
            for t in c:
                txt.append(t.text.encode('utf-8'))
            csvw.writerow(txt)
            #print(txt)


        # ENGLAND

        content = getPage(ghd_uk_url).find("table")
        content = content.findAll("tr", { "align" : "right" })

        for c in content:
            c = c.findAll("td")
            txt = ["England;" + str(year)]
            for t in c:
                txt.append(t.text.encode('utf-8'))
            csvw.writerow(txt)
            #print(txt)


        # USA

        content = getPage(ghd_us_url).find("table")
        content = content.findAll("tr", { "align" : "right" })

        for c in content:
            c = c.findAll("td")
            txt = ["USA;" + str(year)]
            for t in c:
                txt.append(t.text.encode('utf-8'))
            csvw.writerow(txt)
            #print(txt)


        # AUSTRALIA

        content = getPage(ghd_au_url).find("table")
        content = content.findAll("tr", { "align" : "right" })

        for c in content:
            c = c.findAll("td")
            txt = ["Australia;" + str(year)]
            for t in c:
                txt.append(t.text.encode('utf-8'))
            csvw.writerow(txt)
        #print(txt)


    fobj.close()                                # close file
    print("\nDONE !\n\n\nGreyhounddata.com was scraped completely.\n")



# main program

if __name__ == '__main__':
    main()