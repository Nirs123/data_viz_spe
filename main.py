import data
import visualisation as viz
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os
from tkinter.filedialog import asksaveasfile

import geopandas as gpd

#Creating list of regions and academies
regionList = ["AUVERGNE-RHONE-ALPES" , "BOURGOGNE-FRANCHE-COMTE" , "BRETAGNE" , "CENTRE-VAL DE LOIRE" , "CORSE" , "GRAND EST" , "GUADELOUPE" , "GUYANE",
"HAUTS-DE-FRANCE" , "ILE-DE-FRANCE" , "LA REUNION" , "MARTINIQUE" , "MAYOTTE" , "NORMANDIE" , "NOUVELLE-AQUITAINE" , "OCCITANIE" , "PAYS DE LA LOIRE",
"PROVENCE-ALPES-COTE D'AZUR"]
academieList = ["CLERMONT-FERRAND","GRENOBLE","LYON","BESANCON", "DIJON","RENNES","ORLEANS-TOURS","CORSE","NANCY-METZ","REIMS","STRASBOURG",
"GUADELOUPE","GUYANE","AMIENS","LILLE","CRETEIL","PARIS","VERSAILLES","LA REUNION","MARTINIQUE","MAYOTTE","NORMANDIE","BORDEAUX",
"LIMOGES","POITIERS","MONTPELLIER","TOULOUSE","NANTES","AIX-MARSEILLE","NICE","NOUVELLE CALEDONIE","POLYNESIE FRANCAISE","ST PIERRE ET MIQUELON"]

#Class to create tkinter elemnt (label, button, entry or check) and grid it
class Text_Button_Entry:
    def __init__(self,type,text,frame,row,rowspan,column,columnspan,padx,pady,size,command,variable,image,checkSize,width,height):
        self.text = text
        self.frame = frame
        self.row = row
        self.rowspan = rowspan
        self.column = column
        self.columnspan = columnspan
        self.pady = pady
        self.padx = padx
        self.size = size
        self.type = type
        self.command = command
        self.var = variable
        #Create element
        if self.type == "Label":
            self.temp = tk.Label(self.frame, text = self.text, font=('Bahnschrift',str(self.size)),bg="#FFFFFF", fg="#000000")
        elif self.type == "Button":
            self.temp = tk.Button(self.frame, text = self.text, font=('Bahnschrift',str(self.size)),bg="#FFFFFF", fg="#000000", bd=7,command = self.command, image=image,height=height, width=width)
        elif self.type == "Entry":
            self.temp = tk.Entry(self.frame,font=('Bahnschrift',str(self.size)),bg="#FFFFFF", fg="#000000",textvariable=self.var)
        elif self.type == "Check":
            self.temp = tk.Checkbutton(self.frame,text = self.text, font =('Bahnschrift',str(self.size)),bg="#FFFFFF", fg="grey",variable=self.var,width=checkSize)
        #Display element
        self.temp.grid(row = self.row,column = self.column,padx = self.padx,pady = self.pady,columnspan = self.columnspan, rowspan = self.rowspan)

    def grid_forget(self):
        self.temp.grid_forget()

#Main window class
class Window:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Data viz spécialtiés Lycée")
        self.win.geometry('1000x600')
        self.win.minsize(1000,600)
        self.win.maxsize(1000,600)
        self.win.configure(bg="#FFFFFF")

        self.winMainMenu()

        self.win.mainloop()

    #Main menu window
    def winMainMenu(self):
        self.menuFrame = tk.Frame(self.win,bg="#FFFFFF")

        self.barImage = Image.open("img/bar.png")
        self.barImage = self.barImage.resize((280,210), Image.ANTIALIAS)
        self.barImage = ImageTk.PhotoImage(self.barImage)
        self.pieImage = Image.open('img/pie.png')
        self.pieImage = self.pieImage.resize((280,210), Image.ANTIALIAS)
        self.pieImage = ImageTk.PhotoImage(self.pieImage)
        self.mapImage = Image.open("img/map.png")
        self.mapImage = self.mapImage.resize((280,210), Image.ANTIALIAS)
        self.mapImage = ImageTk.PhotoImage(self.mapImage)

        self.title = Text_Button_Entry("Label","Choisissez un graphique",self.menuFrame,0,1,0,2,0,20,35,None,None,None,None,None,None)
        self.barButton = Text_Button_Entry("Button",None,self.menuFrame,1,1,0,1,10,15,0,self.winBarMenu,None,self.barImage,None,None,None)
        self.pieButton = Text_Button_Entry("Button",None,self.menuFrame,1,1,1,1,10,15,0,self.winPieMenu,None,self.pieImage,None,None,None)
        self.mapButton = Text_Button_Entry("Button",None,self.menuFrame,1,1,2,1,10,15,0,None,None,self.mapImage,None,None,None)
        self.barSubtitle = Text_Button_Entry("Label","Graphique à barres avec \nle nombre d'étudiants par spécialité",self.menuFrame,3,1,0,1,0,10,15,None,None,None,None,None,None)
        self.pieSubtitle = Text_Button_Entry("Label","Graphique circulaire représentant\n la répartition du sexe dans une spécialité",self.menuFrame,3,1,1,1,0,0,15,None,None,None,None,None,None)

        self.menuFrame.pack()

    #Pie chart menu
    def winPieMenu(self):
        self.menuFrame.destroy()
        self.pieMenuFrame = tk.Frame(self.win,bg="#FFFFFF")

        self.year2020, self.year2021 = tk.IntVar(),tk.IntVar()
        self.dictYear = {"2020":self.year2020,"2021":self.year2021}

        self.classeP, self.classeT = tk.IntVar(),tk.IntVar()
        self.dictClasse = {"premiere":self.classeP,"terminale":self.classeT}

        self.genderA, self.genderG, self.genderB = tk.IntVar(),tk.IntVar(),tk.IntVar()
        self.dictGender = {"All":self.genderA,"Girls":self.genderG,"Boys":self.genderB}

        self.locationFR, self.locationRegion, self.locationAcademie = tk.IntVar(),tk.IntVar(),tk.IntVar()

        self.speHLP,self.speLLCA,self.speLLCER,self.speHGGSP,self.speSES,self.speMTH,self.spePC,self.speSVT,self.speSI,self.speNSI,self.speART = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
        self.dictSpe = {"HLP":self.speHLP,"LLCA":self.speLLCA,"LLCER":self.speLLCER,"HGGSP":self.speHGGSP,"SES":self.speSES,"MTH":self.speMTH,
                        "PC":self.spePC,"SVT":self.speSVT,"SI":self.speSI,"NSI":self.speNSI,"ART":self.speART}

        self.title = Text_Button_Entry("Label","Choisissez les options du graphique",self.pieMenuFrame,0,1,0,4,0,5,30,None,None,None,None,None,None)

        self.yearTitle = Text_Button_Entry("Label","Année:",self.pieMenuFrame,1,1,0,1,0,10,20,None,None,None,None,None,None)
        self.year2020Check = Text_Button_Entry("Check","2020",self.pieMenuFrame,2,1,0,1,0,3,12,None,self.year2020,None,20,None,None)
        self.year2021Check = Text_Button_Entry("Check","2021",self.pieMenuFrame,2,1,1,2,0,3,12,None,self.year2021,None,20,None,None)

        self.classeTitle = Text_Button_Entry("Label","Classe:",self.pieMenuFrame,3,1,0,1,0,10,20,None,None,None,None,None,None)
        self.classePTitle = Text_Button_Entry("Check","Première",self.pieMenuFrame,4,1,0,1,0,3,12,None,self.classeP,None,20,None,None)
        self.classeTTitle = Text_Button_Entry("Check","Terminale",self.pieMenuFrame,4,1,1,2,0,3,12,None,self.classeT,None,20,None,None)

        self.locationTitle = Text_Button_Entry("Label","Lieu:",self.pieMenuFrame,7,1,0,1,0,10,20,None,None,None,None,None,None)
        self.locationFRTitle = Text_Button_Entry("Check","Toute la France",self.pieMenuFrame,8,1,0,1,0,3,12,None,self.locationFR,None,20,None,None)
        self.locationRegionTitle = Text_Button_Entry("Check","Région (choix ultérieur)",self.pieMenuFrame,8,1,1,2,0,3,12,None,self.locationRegion,None,20,None,None)
        self.locationAcademieTitle = Text_Button_Entry("Check","Académie (choix ultérieur)",self.pieMenuFrame,8,1,3,1,0,3,12,None,self.locationAcademie,None,20,None,None)

        self.speTitle = Text_Button_Entry("Label","Spécialité:",self.pieMenuFrame,9,1,0,1,0,10,20,None,None,None,None,None,None)
        self.speHLPTitle = Text_Button_Entry("Check","HLP",self.pieMenuFrame,10,1,0,1,0,3,12,None,self.speHLP,None,20,None,None)
        self.speLLCATitle = Text_Button_Entry("Check","LLCA",self.pieMenuFrame,10,1,1,1,0,3,12,None,self.speLLCA,None,20,None,None)
        self.speLLCERTitle = Text_Button_Entry("Check","LLCER",self.pieMenuFrame,10,1,2,1,0,3,12,None,self.speLLCER,None,20,None,None)
        self.speHGGSPTitle = Text_Button_Entry("Check","HGGSP",self.pieMenuFrame,10,1,3,1,0,3,12,None,self.speHGGSP,None,20,None,None)
        self.speSESTitle = Text_Button_Entry("Check","SES",self.pieMenuFrame,11,1,0,1,0,3,12,None,self.speSES,None,20,None,None)
        self.speMTHTitle = Text_Button_Entry("Check","MTH",self.pieMenuFrame,11,1,1,1,0,3,12,None,self.speMTH,None,20,None,None)
        self.spePCTitle = Text_Button_Entry("Check","PC",self.pieMenuFrame,11,1,2,1,0,3,12,None,self.spePC,None,20,None,None)
        self.speSVTTitle = Text_Button_Entry("Check","SVT",self.pieMenuFrame,11,1,3,1,0,3,12,None,self.speSVT,None,20,None,None)
        self.speSITitle = Text_Button_Entry("Check","SI",self.pieMenuFrame,12,1,0,1,0,3,12,None,self.speSI,None,20,None,None)
        self.speNSITitle = Text_Button_Entry("Check","NSI",self.pieMenuFrame,12,1,1,1,0,3,12,None,self.speNSI,None,20,None,None)
        self.speARTTitle = Text_Button_Entry("Check","ART",self.pieMenuFrame,12,1,2,1,0,3,12,None,self.speART,None,20,None,None)

        self.validButtonPie = Text_Button_Entry("Button","Valider",self.pieMenuFrame,13,1,0,4,0,10,15,lambda : self.process("pie"),None,None,None,None,None)

        self.pieMenuFrame.pack()

    #Bar chart menu
    def winBarMenu(self):
        self.menuFrame.destroy()
        self.barMenuFrame = tk.Frame(self.win,bg="#FFFFFF")

        self.year2020, self.year2021 = tk.IntVar(),tk.IntVar()
        self.dictYear = {"2020":self.year2020,"2021":self.year2021}

        self.classeP, self.classeT = tk.IntVar(),tk.IntVar()
        self.dictClasse = {"premiere":self.classeP,"terminale":self.classeT}

        self.genderA, self.genderG, self.genderB = tk.IntVar(),tk.IntVar(),tk.IntVar()
        self.dictGender = {"All":self.genderA,"Girls":self.genderG,"Boys":self.genderB}

        self.locationFR, self.locationRegion, self.locationAcademie = tk.IntVar(),tk.IntVar(),tk.IntVar()

        self.title = Text_Button_Entry("Label","Choisissez les options du graphique",self.barMenuFrame,0,1,0,4,0,20,30,None,None,None,None,None,None)
        
        self.yearTitle = Text_Button_Entry("Label","Année:",self.barMenuFrame,1,1,0,1,0,10,20,None,None,None,None,None,None)
        self.year2020Check = Text_Button_Entry("Check","2020",self.barMenuFrame,2,1,0,1,0,5,12,None,self.year2020,None,20,None,None)
        self.year2021Check = Text_Button_Entry("Check","2021",self.barMenuFrame,2,1,1,1,0,5,12,None,self.year2021,None,20,None,None)

        self.classeTitle = Text_Button_Entry("Label","Classe:",self.barMenuFrame,3,1,0,1,0,10,20,None,None,None,None,None,None)
        self.classePTitle = Text_Button_Entry("Check","Première",self.barMenuFrame,4,1,0,1,0,5,12,None,self.classeP,None,20,None,None)
        self.classeTTitle = Text_Button_Entry("Check","Terminale",self.barMenuFrame,4,1,1,2,0,5,12,None,self.classeT,None,20,None,None)

        self.genderTitle = Text_Button_Entry("Label","Genre:",self.barMenuFrame,5,1,0,1,0,7,20,None,None,None,None,None,None)
        self.genderATitle = Text_Button_Entry("Check","Garçons et Filles",self.barMenuFrame,6,1,0,1,0,5,12,None,self.genderA,None,20,None,None)
        self.genderGTitle = Text_Button_Entry("Check","Garçons uniquement",self.barMenuFrame,6,1,1,2,0,5,12,None,self.genderG,None,20,None,None)
        self.genderBTitle = Text_Button_Entry("Check","Filles uniquement",self.barMenuFrame,6,1,3,1,0,5,12,None,self.genderB,None,20,None,None)

        self.locationTitle = Text_Button_Entry("Label","Lieu:",self.barMenuFrame,7,1,0,1,0,10,20,None,None,None,None,None,None)
        self.locationFRTitle = Text_Button_Entry("Check","Toute la France",self.barMenuFrame,8,1,0,1,0,5,12,None,self.locationFR,None,20,None,None)
        self.locationRegionTitle = Text_Button_Entry("Check","Région (choix ultérieur)",self.barMenuFrame,8,1,1,2,0,5,12,None,self.locationRegion,None,20,None,None)
        self.locationAcademieTitle = Text_Button_Entry("Check","Académie (choix ultérieur)",self.barMenuFrame,8,1,3,1,0,5,12,None,self.locationAcademie,None,20,None,None)
        
        self.validButtonPie = Text_Button_Entry("Button","Valider",self.barMenuFrame,13,1,0,4,0,25,15,lambda : self.process("bar"),None,None,None,None,None)

        self.barMenuFrame.pack()

    #Map menu
    def winMapMenu(self):
        pass

    #Process information from map menu
    def processMap(self):
        pass

    #Process information from bar and pie chart menu
    def process(self,type):
        if (self.year2020.get() + self.year2021.get()) != 1:
            errorBox("Veuillez choisir une seule année.")
        elif (self.classeP.get() + self.classeT.get()) != 1:
            errorBox("Veuillez choisir une seule classe.")
        elif type == "bar" and (self.genderA.get() + self.genderG.get() + self.genderB.get()) != 1:
            errorBox("Veuillez choisir un seul genre")
        elif (self.locationFR.get() + self.locationRegion.get() + self.locationAcademie.get()) != 1:
            errorBox("Veuillez choisir un seul lieu.")
        elif type == "pie" and (self.speHLP.get() + self.speLLCA.get() + self.speLLCER.get() + self.speHGGSP.get() + self.speSES.get() + self.speMTH.get()
            + self.spePC.get() + self.speSVT.get() + self.speSI.get() + self.speNSI.get() + self.speART.get()) != 1:
            errorBox("Veuillez choisir un seul enseignement de spécialité")
        else:
            if type == "bar":
                self.barMenuFrame.destroy()
            elif type == "pie":
                self.pieMenuFrame.destroy()
            if self.locationFR.get() != 1:
                self.chooseLocationFrame = tk.Frame(self.win,bg="#FFFFFF")
                if self.locationRegion.get() == 1:
                    self.chooseLocationTitle = Text_Button_Entry("Label","Veuillez choisir la région:",self.chooseLocationFrame,0,1,0,3,0,13,30,None,None,None,None,None,None)
                    self.indexRow,self.indexCol = 1,0
                    self.dictRegion = {}
                    for i in range(len(regionList)):
                        self.regionValue =tk.IntVar()
                        if self.indexCol>2:
                            self.indexCol = 0
                            self.indexRow += 1
                        self.regionName = Text_Button_Entry("Check",regionList[i],self.chooseLocationFrame,self.indexRow,1,self.indexCol,1,0,13,12,None,self.regionValue,None,33,None,None)
                        self.dictRegion[regionList[i]] = self.regionValue
                        self.indexCol += 1
                    self.validButtonLocation = Text_Button_Entry("Button","Valider",self.chooseLocationFrame,self.indexRow+1,1,0,3,0,10,15,lambda : self.verify(type),None,None,None,None,None)
                else:
                    self.chooseLocationTitle = Text_Button_Entry("Label","Veuillez choisir l'académie:",self.chooseLocationFrame,0,1,0,4,0,10,30,None,None,None,None,None,None)
                    self.indexRow,self.indexCol = 1,0
                    self.dictAcademie = {}
                    for i in range(len(academieList)):
                        self.academieValue =tk.IntVar()
                        if self.indexCol>3:
                            self.indexCol = 0
                            self.indexRow += 1
                        self.academieName = Text_Button_Entry("Check",academieList[i],self.chooseLocationFrame,self.indexRow,1,self.indexCol,1,0,10,12,None,self.academieValue,None,20,None,None)
                        self.dictAcademie[academieList[i]] = self.academieValue
                        self.indexCol += 1
                    self.validButtonLocation = Text_Button_Entry("Button","Valider",self.chooseLocationFrame,self.indexRow+1,1,0,4,0,10,15,lambda : self.verify(type),None,None,None,None,None)

                self.chooseLocationFrame.pack()
            else:
                self.generateChart(type)

    #If location not equal to entire France, verify region or academie choose
    def verify(self,type):
        sum = 0
        if self.locationRegion.get() == 1:
            for values in self.dictRegion.values():
                sum += values.get()
        else:
            for values in self.dictAcademie.values():
                sum += values.get()
        if sum != 1:
            errorBox("Veuillez choisir un seul lieu.")
        else:
            self.chooseLocationFrame.destroy()
            self.generateChart(type)

    #Create plot using visualisation.py 
    def generateChart(self,type):
        #Year
        for keys,values in self.dictYear.items():
            if values.get() == 1:
                year = keys
        #Classe
        for keys,values in self.dictClasse.items():
            if values.get() == 1:
                classe = keys
        #Gender
        if type == "pie":
            gender="All"
        elif type == "bar":
            for keys,values in self.dictGender.items():
                if values.get() == 1:
                    gender = keys
        #Spe
        if type == "pie":
            for keys,values in self.dictSpe.items():
                if values.get() == 1:
                    spe = keys
        #Location and LocationName
        locationName = ""
        if self.locationFR.get() == 1:
            location = "fr"
        elif self.locationRegion.get() == 1:
            location = "region"
            for keys,values in self.dictRegion.items():
                if values.get() == 1:
                    locationName = keys
        else:
            location = "academie"
            for keys,values in self.dictAcademie.items():
                if values.get() == 1:
                    locationName = keys

        self.dataResult = data.speCount(classe+".csv",year,gender,location,locationName)

        self.showPlotFrame = tk.Frame(self.win,bg="#FFFFFF")
        if type == "pie":
            self.plot = viz.piePlot(self.dataResult,year,classe,location,locationName,spe)
        elif type == "bar":
            self.plot = viz.barPlot(self.dataResult,year,classe,gender,location,locationName)
        
        self.showPlot()

    #Show plot
    def showPlot(self):
        self.plot.savefig("tmp.png")
        self.plot.clf()
        self.tmpImage = (Image.open("tmp.png"))
        self.resizedImage = ((self.tmpImage).copy()).resize((600,450), Image.ANTIALIAS)
        self.imagePlot = ImageTk.PhotoImage((self.resizedImage))
        self.imagePlotTk = tk.Label(self.showPlotFrame,image=self.imagePlot)

        self.showPlotTitle = Text_Button_Entry("Label","Resultat du graphique",self.showPlotFrame,0,1,0,2,0,10,30,None,None,None,None,None,None)
        self.imagePlotTk.grid(row = 1, rowspan = 3, column=0, columnspan=1,pady=15)
        self.newPlotButton = Text_Button_Entry("Button","Nouveau\ngraphique",self.showPlotFrame,1,1,1,1,25,15,25,self.restart,None,None,None,13,2)
        self.savePlotButton = Text_Button_Entry("Button","Sauvegarder",self.showPlotFrame,2,1,1,1,25,15,25,self.savePlot,None,None,None,13,2)
        self.quitButton = Text_Button_Entry("Button","Quitter",self.showPlotFrame,3,1,1,1,25,15,25,exit,None,None,None,13,2)

        self.showPlotFrame.pack()
        os.remove("tmp.png")

    #Restart the window
    def restart(self):
        self.showPlotFrame.destroy()
        self.winMainMenu()

    #Saveplot
    def savePlot(self):
        self.file = asksaveasfile(initialfile = 'figure.png',defaultextension=".png")
        self.tmpImage.save(self.file.name)

#Classe to display an errorBox with customized message
class errorBox:
    def __init__(self,errorMessage):
        self.errorMessage = errorMessage
        self.popUp = tk.Toplevel()
        self.popUp.title("Erreur")
        self.popUp.config(bg="#FFFFFF")
        self.errorText = Text_Button_Entry("Label",self.errorMessage,self.popUp,0,1,0,1,10,10,20,None,None,None,None,None,None)
        self.exitButton = Text_Button_Entry("Button","Ok",self.popUp,1,1,0,1,0,0,14,self.popUp.destroy,None,None,None,None,None)

if __name__ == "__main__":
    win = Window()
    # data = data.speCountRegion("premiere.csv")
    # classe = "premiere"
    # location = "dep"
    # speName = "SES"
    # year = "2020"
    # tmpData = data.speCountDep(classe+".csv",2020,speName)
    # viz.mapPlot(tmpData,year,classe,location,speName)