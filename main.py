import data
import visualisation as viz

year = "2021"
classe = "premiere"
gender = "Girls"

dataResult = data.speCount(classe+".csv",year,gender)

viz.barPlotAll(dataResult,year,classe,gender)