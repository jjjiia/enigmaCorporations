import csv
import json
import collections
import sys

# TODO: Remove these...
newCountries = ["AFGHANISTAN", "ALBANIA", "ALGERIA", "AMERICAN SAMOA", "ANDORRA", "ANGOLA", "ANGUILLA", "ANTIGUA AND BARBUDA", "ARGENTINA", "ARMENIA", "ARUBA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BERMUDA", "BHUTAN", "BOLIVIA", "BOSNIA-HERZEGOVINA", "BOTSWANA", "BOUVET ISLAND", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINA FASO", "BURUNDI", "CAMBODIA", "CAMEROON", "CANADA", "CAPE VERDE", "CAYMAN ISLANDS", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", "CHINA", "CHRISTMAS ISLAND", "COCOS (KEELING) ISLANDS", "COLOMBIA", "COMOROS", "CONGO, DEMOCRATIC REPUBLIC OF THE (ZAIRE)", "CONGO, REPUBLIC OF", "COOK ISLANDS", "COSTA RICA", "CROATIA", "CUBA", "CYPRUS", "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC", "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", "ESTONIA", "ETHIOPIA", "FALKLAND ISLANDS", "FAROE ISLANDS", "FIJI", "FINLAND", "FRANCE", "FRENCH GUIANA", "GABON", "GAMBIA", "GEORGIA", "GERMANY", "GHANA", "GIBRALTAR", "GREECE", "GREENLAND", "GRENADA", "GUADELOUPE (FRENCH)", "GUAM (USA)", "GUATEMALA", "GUINEA", "GUINEA BISSAU", "GUYANA", "HAITI", "HOLY SEE", "HONDURAS", "HONG KONG", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "IVORY COAST (COTE D`IVOIRE)", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACAU", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL ISLANDS", "MARTINIQUE (FRENCH)", "MAURITANIA", "MAURITIUS", "MAYOTTE", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO", "MONTSERRAT", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS", "NETHERLANDS ANTILLES", "NEW CALEDONIA (FRENCH)", "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NIUE", "NORFOLK ISLAND", "NORTH KOREA", "NORTHERN MARIANA ISLANDS", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU", "PHILIPPINES", "PITCAIRN ISLAND", "POLAND", "POLYNESIA (FRENCH)", "PORTUGAL", "PUERTO RICO", "QATAR", "REUNION", "ROMANIA", "RUSSIA", "RWANDA", "SAINT HELENA", "SAINT KITTS AND NEVIS", "SAINT LUCIA", "SAINT PIERRE AND MIQUELON", "SAINT VINCENT AND GRENADINES", "SAMOA", "SAN MARINO", "SAO TOME AND PRINCIPE", "SAUDI ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA LEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", "SOUTH AFRICA", "SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS", "SOUTH KOREA", "SOUTH SUDAN", "SPAIN", "SRI LANKA", "SUDAN", "SURINAME", "SVALBARD AND JAN MAYEN ISLANDS", "SWAZILAND", "SWEDEN", "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TIMOR-LESTE (EAST TIMOR)", "TOGO", "TOKELAU", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "TURKS AND CAICOS ISLANDS", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", "UNITED KINGDOM", "UNITED STATES", "URUGUAY", "UZBEKISTAN", "VANUATU", "VENEZUELA", "VIETNAM", "VIRGIN ISLANDS", "WALLIS AND FUTUNA ISLANDS", "YEMEN", "ZAMBIA", "ZIMBABWE"]
currentzipcodes = ["10001", "10002", "10003", "10004", "10005", "10006", "10007", "10009", "10010", "10011", "10012", "10013", "10014", "10016", "10017", "10018", "10019", "10020", "10021", "10022", "10023", "10024", "10025", "10026", "10027", "10028", "10029", "10030", "10031", "10032", "10033", "10034", "10035", "10036", "10037", "10038", "10039", "10040", "10044", "10065", "10069", "10075", "10103", "10110", "10111", "10112", "10115", "10119", "10128", "10152", "10153", "10154", "10162", "10165", "10167", "10168", "10169", "10170", "10171", "10172", "10173", "10174", "10177", "10199", "10271", "10278", "10279", "10280", "10282", "10301", "10302", "10303", "10304", "10305", "10306", "10307", "10308", "10309", "10310", "10311", "10312", "10314", "10451", "10452", "10453", "10454", "10455", "10456", "10457", "10458", "10459", "10460", "10461", "10462", "10463", "10464", "10465", "10466", "10467", "10468", "10469", "10470", "10471", "10472", "10473", "10474", "10475", "11001", "11003", "11004", "11005", "11040", "11101", "11102", "11103", "11104", "11105", "11106", "11109", "11201", "11203", "11204", "11205", "11206", "11207", "11208", "11209", "11210", "11211", "11212", "11213", "11214", "11215", "11216", "11217", "11218", "11219", "11220", "11221", "11222", "11223", "11224", "11225", "11226", "11228", "11229", "11230", "11231", "11232", "11233", "11234", "11235", "11236", "11237", "11238", "11239", "11351", "11354", "11355", "11356", "11357", "11358", "11359", "11360", "11361", "11362", "11363", "11364", "11365", "11366", "11367", "11368", "11369", "11370", "11371", "11372", "11373", "11374", "11375", "11377", "11378", "11379", "11385", "11411", "11412", "11413", "11414", "11415", "11416", "11417", "11418", "11419", "11420", "11421", "11422", "11423", "11424", "11425", "11426", "11427", "11428", "11429", "11430", "11432", "11433", "11434", "11435", "11436", "11451", "11691", "11692", "11693", "11694", "11697"]

target_countries = ["AFGHANISTAN", "ALBANIA", "ALGERIA", "AMERICAN SAMOA", "ANDORRA", "ANGOLA", "ANGUILLA", "ANTIGUA AND BARBUDA", "ARGENTINA", "ARMENIA", "ARUBA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BERMUDA", "BHUTAN", "BOLIVIA", "BOSNIA-HERZEGOVINA", "BOTSWANA", "BOUVET ISLAND", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINA FASO", "BURUNDI", "CAMBODIA", "CAMEROON", "CANADA", "CAPE VERDE", "CAYMAN ISLANDS", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", "CHINA", "CHRISTMAS ISLAND", "COCOS (KEELING) ISLANDS", "COLOMBIA", "COMOROS", "CONGO, DEMOCRATIC REPUBLIC OF THE (ZAIRE)", "CONGO, REPUBLIC OF", "COOK ISLANDS", "COSTA RICA", "CROATIA", "CUBA", "CYPRUS", "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC", "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", "ESTONIA", "ETHIOPIA", "FALKLAND ISLANDS", "FAROE ISLANDS", "FIJI", "FINLAND", "FRANCE", "FRENCH GUIANA", "GABON", "GAMBIA", "GEORGIA", "GERMANY", "GHANA", "GIBRALTAR", "GREECE", "GREENLAND", "GRENADA", "GUADELOUPE (FRENCH)", "GUAM (USA)", "GUATEMALA", "GUINEA", "GUINEA BISSAU", "GUYANA", "HAITI", "HOLY SEE", "HONDURAS", "HONG KONG", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "IVORY COAST (COTE D`IVOIRE)", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACAU", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL ISLANDS", "MARTINIQUE (FRENCH)", "MAURITANIA", "MAURITIUS", "MAYOTTE", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO", "MONTSERRAT", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS", "NETHERLANDS ANTILLES", "NEW CALEDONIA (FRENCH)", "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NIUE", "NORFOLK ISLAND", "NORTH KOREA", "NORTHERN MARIANA ISLANDS", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU", "PHILIPPINES", "PITCAIRN ISLAND", "POLAND", "POLYNESIA (FRENCH)", "PORTUGAL", "PUERTO RICO", "QATAR", "REUNION", "ROMANIA", "RUSSIA", "RWANDA", "SAINT HELENA", "SAINT KITTS AND NEVIS", "SAINT LUCIA", "SAINT PIERRE AND MIQUELON", "SAINT VINCENT AND GRENADINES", "SAMOA", "SAN MARINO", "SAO TOME AND PRINCIPE", "SAUDI ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA LEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", "SOUTH AFRICA", "SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS", "SOUTH KOREA", "SOUTH SUDAN", "SPAIN", "SRI LANKA", "SUDAN", "SURINAME", "SVALBARD AND JAN MAYEN ISLANDS", "SWAZILAND", "SWEDEN", "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TIMOR-LESTE (EAST TIMOR)", "TOGO", "TOKELAU", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "TURKS AND CAICOS ISLANDS", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", "UNITED KINGDOM", "UNITED STATES", "URUGUAY", "UZBEKISTAN", "VANUATU", "VENEZUELA", "VIETNAM", "VIRGIN ISLANDS", "WALLIS AND FUTUNA ISLANDS", "YEMEN", "ZAMBIA", "ZIMBABWE"]
target_zipcodes = {"10001", "10002", "10003", "10004", "10005", "10006", "10007", "10009", "10010", "10011", "10012", "10013", "10014", "10016", "10017", "10018", "10019", "10020", "10021", "10022", "10023", "10024", "10025", "10026", "10027", "10028", "10029", "10030", "10031", "10032", "10033", "10034", "10035", "10036", "10037", "10038", "10039", "10040", "10044", "10065", "10069", "10075", "10103", "10110", "10111", "10112", "10115", "10119", "10128", "10152", "10153", "10154", "10162", "10165", "10167", "10168", "10169", "10170", "10171", "10172", "10173", "10174", "10177", "10199", "10271", "10278", "10279", "10280", "10282", "10301", "10302", "10303", "10304", "10305", "10306", "10307", "10308", "10309", "10310", "10311", "10312", "10314", "10451", "10452", "10453", "10454", "10455", "10456", "10457", "10458", "10459", "10460", "10461", "10462", "10463", "10464", "10465", "10466", "10467", "10468", "10469", "10470", "10471", "10472", "10473", "10474", "10475", "11001", "11003", "11004", "11005", "11040", "11101", "11102", "11103", "11104", "11105", "11106", "11109", "11201", "11203", "11204", "11205", "11206", "11207", "11208", "11209", "11210", "11211", "11212", "11213", "11214", "11215", "11216", "11217", "11218", "11219", "11220", "11221", "11222", "11223", "11224", "11225", "11226", "11228", "11229", "11230", "11231", "11232", "11233", "11234", "11235", "11236", "11237", "11238", "11239", "11351", "11354", "11355", "11356", "11357", "11358", "11359", "11360", "11361", "11362", "11363", "11364", "11365", "11366", "11367", "11368", "11369", "11370", "11371", "11372", "11373", "11374", "11375", "11377", "11378", "11379", "11385", "11411", "11412", "11413", "11414", "11415", "11416", "11417", "11418", "11419", "11420", "11421", "11422", "11423", "11424", "11425", "11426", "11427", "11428", "11429", "11430", "11432", "11433", "11434", "11435", "11436", "11451", "11691", "11692", "11693", "11694", "11697"}

rows=[]
values = []

with open('/Users/jiazhang/Documents/GitHub/corporations/crawler/CorporationsData_Original.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        rows.append(row)

def is_valid_zipcode(zipcode):
    if len(zipcode) != 5:
        return False
    try:
        int(zipcode)
        return True
    except ValueError:
        return False


print(len(rows))


ny_companies = []
aggregated_zipcode_data = {}

for row in rows:
    address = str(row[9])
    rowlist = address.split(' ')
    zipcode = rowlist[-1].split("-")[0]

    year = str(row[8][1:5])
    name = str(row[0])
    registrationId = str(row[1])
    status = str(row[4])
    entityType = str(row[3])
    address = str(row[9])
    jurisdiction =  row[2]
    rowlist = address.split(' ')

    if zipcode in target_zipcodes:
        if jurisdiction in target_countries:
            company = {}
            company["name"] = str(name)
            company["address"] = str(address)
            company["zipcode"] = str(zipcode)
            company["entityType"] = str(entityType)
            company["status"] = str(status)
            company["year"] = str(year)
            company["jurisdiction"] = str(jurisdiction)

            ny_companies.append(company)

            if not(zipcode in aggregated_zipcode_data):
                aggregated_zipcode_data[zipcode] = {
                    "sum":0,
                    "max":0,
                    "countries":set(),
                    "values":{}
                }
            
            # Add the jurisdiction to the countries
            aggregated_zipcode_data[zipcode]["countries"].add(jurisdiction)

            # Update the count by countries in the values dictionary
            if jurisdiction in aggregated_zipcode_data[zipcode]["values"]:
                aggregated_zipcode_data[zipcode]["values"][jurisdiction] += 1
            else:
                aggregated_zipcode_data[zipcode]["values"][jurisdiction] = 1
            
            # Increment the total number of companies
            aggregated_zipcode_data[zipcode]["sum"] += 1

            # Update the current max
            aggregated_zipcode_data[zipcode]["max"] = max(aggregated_zipcode_data[zipcode]["max"], aggregated_zipcode_data[zipcode]["values"][jurisdiction])
          

for zipcode in aggregated_zipcode_data:
    aggregated_zipcode_data[zipcode]["countries"] = list(aggregated_zipcode_data[zipcode]["countries"])

print(json.dumps(aggregated_zipcode_data))
  
sys.exit()


# Old Crappy Code...

for zipcode in currentzipcodes:
    #print zipcode
    #print country
    json_values = []
    allzipcodes = []
    allzipcodesF = {}
    zip_dict = {}
    findmax = []
    zipcodesOnly = []
    
    for row in rows:
        address = str(row[9])
        rowlist = address.split(' ')
        datazipcode = rowlist[-1]

        year = str(row[8][1:5])
        name = str(row[0])
        registrationId = str(row[1])
        status = str(row[4])
        entityType = str(row[3])
        address = str(row[9])
        jurisdiction =  row[2]
        rowlist = address.split(' ')
        if jurisdiction in newCountries:    
            allzipcodes.append(jurisdiction)

            obj = {}
            obj["name"] = str(name)
            obj["address"] = str(address)
            obj["zipcode"] = str(zipcode)
            obj["entityType"] = str(entityType)
            obj["status"] = str(status)
            obj["year"] = str(year)
            json_values.append(obj)
            
    zip_dict[str(zipcode)] = json_values
    regionSum = 0
    for i in allzipcodes:
         allzipcodesF[i]=allzipcodesF.get(i,0)+1
     
    for j in allzipcodesF:
        #print allzipcodesF.get(j)
        regionSum = regionSum + allzipcodesF.get(j)
        findmax.append(allzipcodesF.get(j))
        zipcodesOnly.append(j)

    print "\""+str(zipcode)+"\":{\"sum\":"+str(regionSum)+", \"max\":" + str(max(findmax))+ ", \"values\":" + str(allzipcodesF) +", \"countries\": "+str(zipcodesOnly)+"},"


#print(s)
#basePath = '/Users/jiazhang/Documents/GitHub/corporations/'
#output_file = open(basePath+'test2.json', 'w')
#json.dump(zip_dict, output_file)
#print allzipcodesF
