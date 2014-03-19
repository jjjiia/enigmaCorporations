import csv
import json
import collections

#see nyc311_headers.csv for column headers

cleanedColumns = []
cleanedColumnsF = {}
#open file
manhattan = 0
brooklyn = 0
queens = 0
statenIsland = 0
bronx = 0
#total, man,brook,q,s,bronx
#humanTotals=[167773, 70195, 48000, 25511, 4008, 20059]
#machineTotals = [61200, 38814,  12482, 6438, 1146, 2320]
with open('original_data/enigma-us-states-az-azcc-corps-listing-3164e1a23aedfa7aecb433bde80f4918.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    coordinates = []
    #print "opened"
    
    for row in spamreader:
        #identify columns
        agency = row[4]
        descriptor = row[6]
        locationType = row[7]
        zipcode = row[9]
        borough = row[23]
        lat = row[49][0:6]
        lng = row[50][0:6]       #print borough
        #make array of needed columns
        newrow = ['human',agency,descriptor,locationType,zipcode,borough,lat,lng]
        newrowStr = str(newrow)
        if "MANHATTAN" in borough:
            manhattan = manhattan+1
        if "BROOKLYN" in borough:
            brooklyn = brooklyn+1
        if "QUEENS" in borough:
            queens = queens+1
        if "STATEN ISLAND" in borough:
            statenIsland = statenIsland+1
        if "BRONX" in borough:
            bronx = bronx+1
        
        #print newrow
        #make array of arrays
        cleanedColumns.append(newrowStr)
        #print cleanedColumns
#print len(cleanedColumns)
#print manhattan, brooklyn, queens, statenIsland, bronx
#print manhattan+brooklyn+queens+statenIsland+bronx
for row in cleanedColumns:
    cleanedColumnsF[row]=cleanedColumnsF.get(row,0)+1

print cleanedColumnsF