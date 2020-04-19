from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep

def getShpFields(name, path):
    mylayerpath=path
    vlayer = QgsVectorLayer(mylayerpath, name, "ogr")
    all_fields = []
    for field in vlayer.fields():
        all_fields += [(field.name(), field.typeName()),]
    return all_fields
    

app = QgsApplication([], True)
app.setPrefixPath("C:/Program Files/QGIS 3.10/apps/qgis", True)
app.initQgis()

project = QgsProject.instance()

project.read('C:/map/sample.qgz')
    
all_fields = getShpFields("Poi","C:/map/shps/scenic_spot_C_f/Scenic_spot_C_f.shp")
print(all_fields)

app.exitQgis()
