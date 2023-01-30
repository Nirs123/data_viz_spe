import pandas as pd
import numpy as np

def speCount(file,year,gender,location,locationName):
    #Open csv file
    df = pd.read_csv("data/"+file)

    #Initiate dictionaries
    speGirls = {"HLP":0,"LLCA":0,"LLCER":0,"HGGSP":0,"SES":0,"MTH":0,"PC":0,"SVT":0,"SI":0,"NSI":0,"ART":0}
    speBoys = {"HLP":0,"LLCA":0,"LLCER":0,"HGGSP":0,"SES":0,"MTH":0,"PC":0,"SVT":0,"SI":0,"NSI":0,"ART":0}

    #Gap particularity on terminale.csv file
    gap = 0
    if file == "terminale.csv":
        gap = 2

    #Function to check location
    def verifyLocation(row,location,locationName):
        if location == "fr":
            return True
        elif location == "region":
            if row[2] == locationName:
                return True
        elif location == "academie":
            if row[3] == locationName:
                return True
        return False

    #For each row in csv file
    for row in df.itertuples():
        #Apply request settings (year and location)
        if row[1] == int(year) and verifyLocation(row,location,locationName):
            #If row is valid, add each numbers to dictinaries
            speGirls["HLP"] += np.int32(np.int32(np.nan_to_num(row[13])))
            speBoys["HLP"] += np.int32(np.nan_to_num(row[14]))
            speGirls["LLCA"] += np.int32(np.nan_to_num(row[15])) + np.int32(np.nan_to_num(row[17]))
            speBoys["LLCA"] += np.int32(np.nan_to_num(row[16])) + np.int32(np.nan_to_num(row[18]))
            speGirls["LLCER"] += np.int32(np.nan_to_num(row[19]))
            speBoys["LLCER"] += np.int32(np.nan_to_num(row[20]))
            speGirls["HGGSP"] += np.int32(np.nan_to_num(row[21]))
            speBoys["HGGSP"] += np.int32(np.nan_to_num(row[22]))
            speGirls["SES"] += np.int32(np.nan_to_num(row[23]))
            speBoys["SES"] += np.int32(np.nan_to_num(row[24]))
            speGirls["MTH"] += np.int32(np.nan_to_num(row[25]))
            speBoys["MTH"] += np.int32(np.nan_to_num(row[26]))
            speGirls["PC"] += np.int32(np.nan_to_num(row[27]))
            speBoys["PC"] += np.int32(np.nan_to_num(row[28]))
            speGirls["SVT"] += np.int32(np.nan_to_num(row[29]))
            speBoys["SVT"] += np.int32(np.nan_to_num(row[30]))
            if file == "premiere.csv":
                speGirls["SI"] += np.int32(np.nan_to_num(row[31]))
                speBoys["SI"] += np.int32(np.nan_to_num(row[32]))
            speGirls["NSI"] += np.int32(np.nan_to_num(row[33-gap]))
            speBoys["NSI"] += np.int32(np.nan_to_num(row[34-gap]))
            speGirls["ART"] += np.int32(np.nan_to_num(row[35-gap])) + np.int32(np.nan_to_num(row[37-gap])) + np.int32(np.nan_to_num(row[39-gap])) + np.int32(np.nan_to_num(row[41-gap])) + np.int32(np.nan_to_num(row[43-gap])) + np.int32(np.nan_to_num(row[45-gap])) + np.int32(np.nan_to_num(row[47-gap]))
            speBoys["ART"] += np.int32(np.nan_to_num(row[36-gap])) + np.int32(np.nan_to_num(row[38-gap])) + np.int32(np.nan_to_num(row[40-gap])) + np.int32(np.nan_to_num(row[42-gap])) + np.int32(np.nan_to_num(row[44-gap])) + np.int32(np.nan_to_num(row[46-gap])) + np.int32(np.nan_to_num(row[48-gap]))
    
    #Depending on the request gender, return dictionnaries
    if gender == "All":
        return speGirls,speBoys
    elif gender == "Girls":
        return speGirls
    elif gender == "Boys":
        return speBoys


def speCountRegion(file,year,speName):
    gap = 0
    if file == "terminale.csv":
        gap = 2
        
    dicoIndex = {"HLP":[13,14],"LLCA":[15,16,17,18],"LLCER":[19,20],"HGGSP":[21,22],
        "SES":[23,24],"MTH": [25,26],"PC":[27,28],"SVT":[29,30],"SI":[31,32],
        "NSI":[33-gap,34-gap],"ART":[i-gap for i in range(35,49)]}

    dicoRegion = {"AUVERGNE-RHONE-ALPES":84,"BOURGOGNE-FRANCHE-COMTE":27,"BRETAGNE":53,"CENTRE-VAL DE LOIRE":24,
    "CORSE":94,"GRAND EST":44,"HAUTS-DE-FRANCE":32,"ILE-DE-FRANCE":11,"NORMANDIE":28,
    "NOUVELLE-AQUITAINE":75,"OCCITANIE":76,"PAYS DE LA LOIRE":52,"PROVENCE-ALPES-COTE D'AZUR":93}
    excludedRegion = ['GUADELOUPE',"MARTINIQUE","GUYANE","MAYOTTE","LA REUNION","OUTRE-MER HORS REGIONS ACADEMIQUES"]

    df = pd.read_csv("data/"+file)
    
    tmpDict = {11:0,24:0,27:0,28:0,32:0,44:0,52:0,53:0,75:0,76:0,84:0,93:0,94:0}
    
    for row in df.itertuples():
        if row[1] == year and row[2] not in excludedRegion:
            for item in dicoIndex[speName]:
                tmpDict[dicoRegion[row[2]]] += row[item]
    
    dicoRes = {"index":[],"value":[]}
    for key,value in tmpDict.items():
        dicoRes["index"].append(str(key))
        dicoRes["value"].append(value)

    return dicoRes