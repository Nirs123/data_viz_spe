import pandas as pd
import time

def speCount(file,year,gender):
    df = pd.read_csv(file)

    speGirls = {"HLP":0,"LLCA":0,"LLCER":0,"HGGSP":0,"SES":0,"MTH":0,"PC":0,"SVT":0,"SI":0,"NSI":0,"ART":0}
    speBoys = {"HLP":0,"LLCA":0,"LLCER":0,"HGGSP":0,"SES":0,"MTH":0,"PC":0,"SVT":0,"SI":0,"NSI":0,"ART":0}

    if gender == "All":
        print("ALL")
        for row in df.itertuples():
            if row[1] == int(year):
                speGirls["HLP"] += row[13]
                speBoys["HLP"] += row[14]
                speGirls["LLCA"] += row[15] + row[17]
                speBoys["LLCA"] += row[16] + row[18]
                speGirls["LLCER"] += row[19]
                speBoys["LLCER"] += row[20]
                speGirls["HGGSP"] += row[21]
                speBoys["HGGSP"] += row[22]
                speGirls["SES"] += row[23]
                speBoys["SES"] += row[24]
                speGirls["MTH"] += row[25]
                speBoys["MTH"] += row[26]
                speGirls["PC"] += row[27]
                speBoys["PC"] += row[28]
                speGirls["SVT"] += row[29]
                speBoys["SVT"] += row[30]
                speGirls["SI"] += row[31]
                speBoys["SI"] += row[32]
                speGirls["NSI"] += row[33]
                speBoys["NSI"] += row[34]
                speGirls["ART"] += row[35] + row[37] + row[39] + row[41] + row[43] + row[45] + row[47]
                speBoys["ART"] += row[36] + row[38] + row[40] + row[42] + row[44] + row[46] + row[48]
        return speGirls,speBoys
    elif gender == "Girls":
        for row in df.itertuples():
            if row[1] == int(year):
                speGirls["HLP"] += row[13]
                speGirls["LLCA"] += row[15] + row[17]
                speGirls["LLCER"] += row[19]
                speGirls["HGGSP"] += row[21]
                speGirls["SES"] += row[23]
                speGirls["MTH"] += row[25]
                speGirls["PC"] += row[27]
                speGirls["SVT"] += row[29]
                speGirls["SI"] += row[31]
                speGirls["NSI"] += row[33]
                speGirls["ART"] += row[35] + row[37] + row[39] + row[41] + row[43] + row[45] + row[47]
        return speGirls
    elif gender == "Boys":
        for row in df.itertuples():
            if row[1] == int(year):
                speBoys["HLP"] += row[14]
                speBoys["LLCA"] += row[16] + row[18]
                speBoys["LLCER"] += row[20]
                speBoys["HGGSP"] += row[22]
                speBoys["SES"] += row[24]
                speBoys["MTH"] += row[26]
                speBoys["PC"] += row[28]
                speBoys["SVT"] += row[30]
                speBoys["SI"] += row[32]
                speBoys["NSI"] += row[34]
                speBoys["ART"] += row[36] + row[38] + row[40] + row[42] + row[44] + row[46] + row[48]
        return speBoys

print(speCount("terminale.csv",2020,"All"))