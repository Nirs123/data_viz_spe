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
    year = int(year)

    dicoIndex = {"HLP":[13,14],"LLCA":[15,16,17,18],"LLCER":[19,20],"HGGSP":[21,22],
        "SES":[23,24],"MTH": [25,26],"PC":[27,28],"SVT":[29,30],"SI":[31,32],
        "NSI":[33-gap,34-gap],"ART":[i-gap for i in range(35,49)]}

    dicoRegion = {"AUVERGNE-RHONE-ALPES":84,"BOURGOGNE-FRANCHE-COMTE":27,"BRETAGNE":53,"CENTRE-VAL DE LOIRE":24,
    "CORSE":94,"GRAND EST":44,"HAUTS-DE-FRANCE":32,"ILE-DE-FRANCE":11,"NORMANDIE":28,
    "NOUVELLE-AQUITAINE":75,"OCCITANIE":76,"PAYS DE LA LOIRE":52,"PROVENCE-ALPES-COTE D'AZUR":93}
    excludedRegion = ['GUADELOUPE',"MARTINIQUE","GUYANE","MAYOTTE","LA REUNION","OUTRE-MER HORS REGIONS ACADEMIQUES"]

    df = pd.read_csv("data/"+file)
    
    dictNbEtudiantSpe = {11:0,24:0,27:0,28:0,32:0,44:0,52:0,53:0,75:0,76:0,84:0,93:0,94:0}
    dictNbEtudiantTot = {11:0,24:0,27:0,28:0,32:0,44:0,52:0,53:0,75:0,76:0,84:0,93:0,94:0}

    for row in df.itertuples():
        if row[1] == year and row[2] not in excludedRegion:
            dictNbEtudiantTot[dicoRegion[row[2]]] += np.int32(np.int32(np.nan_to_num(row[10])))
            for item in dicoIndex[speName]:
                dictNbEtudiantSpe[dicoRegion[row[2]]] += row[item]

    dicoRes = {"index":[],"value":[]}
    for key,value in dictNbEtudiantSpe.items():
        dicoRes["index"].append(str(key))
        dicoRes["value"].append(((value)*100)/dictNbEtudiantTot[key])

    return dicoRes


def speCountDep(file,year,speName):
    gap = 0
    if file == "terminale.csv":
        gap = 2
    year = int(year)
        
    dicoIndex = {"HLP":[13,14],"LLCA":[15,16,17,18],"LLCER":[19,20],"HGGSP":[21,22],
        "SES":[23,24],"MTH": [25,26],"PC":[27,28],"SVT":[29,30],"SI":[31,32],
        "NSI":[33-gap,34-gap],"ART":[i-gap for i in range(35,49)]}

    dicoDep =   {'AIN': '01', 'AISNE': '02', 'ALLIER': '03', 'ALPES-DE-HTE-PROVENCE': '04', 'HAUTES-ALPES': '05', 'ALPES-MARITIMES': '06', 
    'CORSE-DU-SUD': '2A', 'HAUTE-CORSE': '2B', 'ARDECHE': '07', 'ARDENNES': '08', 'ARIEGE': '09', 'AUBE': '10', 'AUDE': '11', 'AVEYRON': '12', 
    'BOUCHES-DU-RHONE': '13', 'CALVADOS': '14', 'CANTAL': '15', 'CHARENTE': '16', 'CHARENTE-MARITIME': '17', 'CHER': '18', 'CORREZE': '19', 
    "COTE D'OR": '21', "COTES D'ARMOR": '22', 'CREUSE': '23', 'DORDOGNE': '24', 'DOUBS': '25', 'DROME': '26', 'EURE': '27', 'EURE-ET-LOIR': '28', 
    'FINISTERE': '29', 'GARD': '30', 'HAUTE-GARONNE': '31', 'GERS': '32', 'GIRONDE': '33', 'HERAULT': '34', 'ILLE-ET-VILAINE': '35', 'INDRE': '36', 
    'INDRE-ET-LOIRE': '37', 'ISERE': '38', 'JURA': '39', 'LANDES': '40', 'LOIR-ET-CHER': '41', 'LOIRE': '42', 'HAUTE-LOIRE': '43', 
    'LOIRE-ATLANTIQUE': '44', 'LOIRET': '45', 'LOT': '46', 'LOT-ET-GARONNE': '47', 'LOZERE': '48', 'MAINE-ET-LOIRE': '49', 'MANCHE': '50', 
    'MARNE': '51', 'HAUTE-MARNE': '52', 'MAYENNE': '53', 'MEURTHE-ET-MOSELLE': '54', 'MEUSE': '55', 'MORBIHAN': '56', 'MOSELLE': '57', 
    'NIEVRE': '58', 'NORD': '59', 'OISE': '60', 'ORNE': '61', 'PAS-DE-CALAIS': '62', 'PUY-DE-DOME': '63', 'PYRENEES-ATLANTIQUES': '64', 
    'HAUTES-PYRENEES': '65', 'PYRENEES-ORIENTALES': '66', 'BAS-RHIN': '67', 'HAUT-RHIN': '68', 'RHONE': '69', 'HAUTE-SAONE': '70', 
    'SAONE-ET-LOIRE': '71', 'SARTHE': '72', 'SAVOIE': '73', 'HAUTE SAVOIE': '74', 'PARIS': '75', 'SEINE MARITIME': '76', 'SEINE-ET-MARNE': '77', 
    'YVELINES': '78', 'DEUX-SEVRES': '79', 'SOMME': '80', 'TARN': '81', 'TARN-ET-GARONNE': '82', 'VAR': '83', 'VAUCLUSE': '84', 'VENDEE': '85', 
    'VIENNE': '86', 'HAUTE-VIENNE': '87', 'VOSGES': '88', 'YONNE': '89', 'TERRITOIRE DE BELFORT': '90', 'ESSONNE': '91', 'HAUTS-DE-SEINE': '92', 
    'SEINE-SAINT-DENIS': '93', 'VAL-DE-MARNE': '94', "VAL-D'OISE": '95'}
    excludedDep = ['GUADELOUPE','GUYANE','LA REUNION','MARTINIQUE','NOUVELLE CALEDONIE','POLYNESIE FRANCAISE','MAYOTTE',
                    'ST-PIERRE-ET-MIQUELON','WALLIS ET FUTUNA']

    df = pd.read_csv("data/"+file)
    
    dictNbEtudiantSpe = {}
    dictNbEtudiantTot = {}
    for value in dicoDep.values():
        dictNbEtudiantSpe[value] = 0
        dictNbEtudiantTot[value] = 0

    for row in df.itertuples():
        if row[1] == year and row[4] not in excludedDep:
            dictNbEtudiantTot[dicoDep[row[4]]] += np.int32(np.int32(np.nan_to_num(row[10])))
            for item in dicoIndex[speName]:
                dictNbEtudiantSpe[dicoDep[row[4]]] += row[item]

    dicoRes = {"index":[],"value":[]}
    for key,value in dictNbEtudiantSpe.items():
        dicoRes["index"].append(str(key))
        dicoRes["value"].append(((value)*100)/dictNbEtudiantTot[key])

    return dicoRes