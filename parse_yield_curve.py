import datetime
import xml.etree.ElementTree as ET

current_date = datetime.datetime.now().strftime("%m-%d-%y")
download_directory = '/home/eggy/Recession-Predictor/downloads/'
filename = current_date + ".xml"

def parseXML():
    tree = ET.parse(download_directory + filename)
    root = tree.getroot()

    print('DATE         10y-2y      10y-1y      10y-3m')
    for x in range(4, len(root)):
        yield_spread_date = datetime.datetime.strptime(root[x][6][0][1].text, '%Y-%m-%dT%H:%M:%S')

        bond_3_month = float(root[x][6][0][4].text)
        bond_1_year = float(root[x][6][0][6].text)
        bond_2_year = float(root[x][6][0][7].text)
        bond_10_year = float(root[x][6][0][11].text)
        yield_spread_10_2 = bond_10_year - bond_2_year
        yield_spread_10_1 = bond_10_year - bond_1_year
        yield_spread_10_3m = bond_10_year - bond_3_month

        print(yield_spread_date.strftime("%m-%d-%y") + ": " + "     %.2f        %.2f        %.2f" %(yield_spread_10_2, yield_spread_10_1, yield_spread_10_3m))

def main():
    parseXML()

if __name__ == "__main__":
    main()