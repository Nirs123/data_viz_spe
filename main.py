import data
import visualisation as viz
import tkinter as tk
import PyQt5.QtWidgets as qtw

year = "2021"           # 2020 | 2021
classe = "premiere"     # terminale | premiere
gender = "All"          # All | Girls | Boys
location = "fr"         # fr | region | academie
locationName = ""       # see below
speName = "NSI"         # HLP | LLCA | LLCER | HGGSP | SES | MTH | PC | SVT | SI | NSI | ART

# region: AUVERGNE-RHONE-ALPES | BOURGOGNE-FRANCHE-COMTE | BRETAGNE | CENTRE-VAL DE LOIRE | CORSE | GRAND EST | GUADELOUPE | GUYANE
# HAUTS-DE-FRANCE | ILE-DE-FRANCE | LA REUNION | MARTINIQUE | MAYOTTE | NORMANDIE | NOUVELLE-AQUITAINE | OCCITANIE | PAYS DE LA LOIRE
# PROVENCE-ALPES-COTE D'AZUR | OUTRE-MER HORS REGIONS ACADEMIQUES

# academie: CLERMONT-FERRAND | GRENOBLE | LYON | BESANCON | DIJON | RENNES | ORLEANS-TOURS | CORSE | NANCY-METZ | REIMS | STRASBOURG
# GUADELOUPE | GUYANE | AMIENS | LILLE | CRETEIL | PARIS | VERSAILLES | LA REUNION | MARTINIQUE | MAYOTTE | NORMANDIE | BORDEAUX
# LIMOGES | POITIERS | MONTPELLIER | TOULOUSE | NANTES | AIX-MARSEILLE | NICE | NOUVELLE CALEDONIE | POLYNESIE FRANCAISE
# ST PIERRE ET MIQUELON

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Viz spécialités Lycée")
        self.setFixedHeight(600)
        self.setFixedWidth(1000)

        self.menu()

        vbox = qtw.QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def menu(self):
        self.groupBox = qtw.QGroupBox("MEGA TEST")
        grid = qtw.QGridLayout()

        button = qtw.QPushButton("test")
        grid.addWidget(button, 0,0)

        self.groupBox.setLayout(grid)

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

#dataResult = data.speCount(classe+".csv",year,gender,location,locationName)

#viz.piePlot(dataResult,year,classe,location,locationName,speName)
#viz.barPlot(dataResult,year,classe,gender,location,locationName)