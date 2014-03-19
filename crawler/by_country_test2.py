import csv
import json
import collections
## this gets the coordinates and kind of rounds them down so they can be put into bins
Manhattan = ["10002", "10003", "10009", "10004", "10005", "10006", "10007", "10038", "10280", "10048", "10012", "10013", "10014", "10010", "10016", "10017", "10022", "10001", "10011", "10018", "10019", "10020", "10036", "10034", "10040", "10033","10032","10026", "10027", "10030", "10037", "10039", "10031", "10029", "10035" ,"10021", "10028", "10044", "10128", "10023", "10024", "10025"]
NewYorkCity = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040, 10041, 10043, 10044, 10045, 10046, 10047, 10048, 10055, 10060, 10069, 10072, 10079, 10080, 10081, 10082, 10087, 10090, 10094, 10095, 10096, 10098, 10099, 10101, 10102, 10103, 10104, 10105, 10106, 10107, 10108, 10109, 10110, 10111, 10112, 10113, 10114, 10115, 10116, 10117, 10118, 10119, 10120, 10121, 10122, 10123, 10124, 10125, 10126, 10128, 10129, 10130, 10131, 10132, 10133, 10138, 10149, 10150, 10151, 10152, 10153, 10154, 10155, 10156, 10157, 10158, 10159, 10160, 10161, 10162, 10163, 10164, 10165, 10166, 10167, 10168, 10169, 10170, 10171, 10172, 10173, 10174, 10175, 10176, 10177, 10178, 10179, 10184, 10185, 10196, 10197, 10199, 10203, 10211, 10212, 10213, 10242, 10249, 10256, 10257, 10258, 10259, 10260, 10261, 10265, 10268, 10269, 10270, 10271, 10272, 10273, 10274, 10275, 10276, 10277, 10278, 10279, 10280, 10281, 10282, 10285, 10286, 10292, 11237]
#print("Starting...")
values = []
rows=[]
with open('CorporationsData_Original.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        rows.append(row)
        #print row
alljurisdictions = []
alljurisdictionsF = {}
zip_dict = {}
for zipcode in NewYorkCity:
    json_values = []
    for row in rows:
        if(str(zipcode) in row[9]):
            if("FOREIGN" in row[3]):
                print row
                year = str(row[8][0:4]) 
                name = str(row[0])
                status = str(row[4])
                entityType = str(row[3])
                address = str(row[9])
                jurisdiction = str(row[2])
                alljurisdictions.append(jurisdiction)
                #print(year, name, address, jurisdiction, entityType, status)
                #value = {"key":zipcode, "year":year, "name":name, "address":address, "jurisdiction":jurisdiction, "entityType":entityType, "status":status}
                obj = {}
                obj["name"] = str(name)
                obj["address"] = str(address)
                obj["entityType"] = str(entityType)
                obj["status"] = str(status)
                obj["year"] = str(year)
                obj["zipcode"] = str(zipcode)
                json_values.append(obj)
                #values.append(value)
    
    zip_dict[str(jurisdiction)] = json_values
    
#print(s)
basePath = '/Users/jiazhang/Documents/GitHub/enigmaCorporations/'
output_file = open(basePath+'NewYorkCity_bycountry.json', 'w')
json.dump(zip_dict, output_file)
#print alljurisdictionsF
