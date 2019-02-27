import urllib.request
import datetime

def download():
    attempts = 0
    url = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%202019'
    current_date = datetime.datetime.now().strftime("%m-%d-%y")
    download_directory = '/home/eggy/Recession-Predictor/downloads/'
    filename = current_date + ".xml"

    response = urllib.request.urlopen(url)
    content = response.read()

    f = open(download_directory + filename, 'wb')
    f.write(content)
    f.close()

def main():
    download()

if __name__ == "__main__":
    main()