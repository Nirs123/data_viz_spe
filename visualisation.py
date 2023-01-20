import matplotlib.pyplot as plt

def barPlotAll(data,year,classe,gender):
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
        plt.bar(positions,valuesBoys,width,color='r')
        plt.bar(positions,valuesGirls,width,bottom=valuesBoys,color='b')
        plt.legend(labels=["Garçons","Filles"],fancybox=True,framealpha=0.7,borderpad=0.8,shadow=True)
        plt.suptitle("Garçons et Filles",size=12)
    elif gender == "Girls":
        plt.bar(positions,valuesGirls,width,color='b')
        plt.suptitle("Filles uniquement",size=12)
    elif gender == "Boys":
        plt.bar(positions,valuesBoys,width,color='b')
        plt.suptitle("Garçons uniquement",size=12)

    plt.title(f"Nombre d'étudiants par spécialité en {classe} à la rentrée {year}",size=16,pad=20)
    plt.xticks(positions,titles,rotation=45,size=10)
    plt.xlabel("Spécialité",size=13)
    plt.ylabel("Nombre d'étudiants",size=13)
    plt.subplots_adjust(bottom=0.18,left=0.15,right=0.85,top=0.85)

    plt.show()