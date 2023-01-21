import matplotlib.pyplot as plt

def barPlot(data,year,classe,gender,location,locationName):
    if gender == "All":
        valuesGirls = list(data[0].values())
        valuesBoys = list(data[1].values())
        titles = list(data[0].keys())
        positions = range(len(valuesGirls))
    elif gender == "Girls":
        valuesGirls = list(data.values())
        titles = list(data.keys())
        positions = range(len(valuesGirls))
    elif gender == "Boys":
        valuesBoys = list(data.values())
        titles = list(data.keys())
        positions = range(len(valuesBoys))

    width = 0.7

    fig = plt.figure(figsize=(8,6))

    if gender == "All":
        plt.bar(positions,valuesBoys,width,color='#87CEEB')
        plt.bar(positions,valuesGirls,width,bottom=valuesBoys,color='#EC8993')
        plt.legend(labels=["Garçons","Filles"],fancybox=True,framealpha=0.7,borderpad=0.8,shadow=True)
    elif gender == "Girls":
        plt.bar(positions,valuesGirls,width,color='#EC8993')
    elif gender == "Boys":
        plt.bar(positions,valuesBoys,width,color='#87CEEB')

    if location == "fr":
        plt.title(f"Nombre d'étudiants par spécialité en France \n en classe de {classe} à la rentrée {year}",size=14,pad=20)
    elif location == "region":
        plt.title(f"Nombre d'étudiants par spécialité dans la région de {locationName} \n en classe de {classe} à la rentrée {year}",size=13,pad=20)
    elif location == "academie":
        plt.title(f"Nombre d'étudiants par spécialité dans l'academie de {locationName} \n en classe de {classe} à la rentrée {year}",size=13,pad=20)
    plt.xticks(positions,titles,rotation=45,size=10)
    plt.xlabel("Spécialité",size=13)
    plt.ylabel("Nombre d'étudiants",size=13)
    plt.subplots_adjust(bottom=0.18,left=0.15,right=0.85,top=0.85)

    plt.show()

def piePlot(data,year,classe,location,locationName,speName):
    values = [data[0][speName],data[1][speName]]
    labels = ["Filles","Garçons"]
    total = values[0] + values[1]

    plt.pie(values,colors=['#EC8993','#87CEEB'],autopct='%1.1f%%')
    plt.legend(labels=labels,fancybox=True,framealpha=0.7,borderpad=0.8,shadow=True)
    if location == "fr":
        plt.title(f"Répartition des étudiants en {speName} en France \n en classe de {classe} à la rentrée {year}",size=14,pad=20)
    elif location == "region":
        plt.title(f"Répartition des étudiants en {speName} dans la région de {locationName} \n en classe de {classe} à la rentrée {year}",size=13,pad=20)
    elif location == "academie":
        plt.title(f"Répartition des étudiants en {speName} dans l'academie de {locationName} \n en classe de {classe} à la rentrée {year}",size=13,pad=20)
    plt.subplots_adjust(top=0.8)
    plt.show()