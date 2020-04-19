from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep


def getShpFeatures(name, path):
    mylayerpath=path
    vlayer = QgsVectorLayer(mylayerpath, name, "ogr")
    features = vlayer.getFeatures()
    all_features = []
    for feature in features:
        all_features += [(feature.id(), feature.geometry()),]
     
    return all_features
    
    
app = QgsApplication([], True)
app.setPrefixPath("C:/Program Files/QGIS 3.10/apps/qgis", True)
app.initQgis()

project = QgsProject.instance()

project.read('C:/map/sample.qgz')
    
all_features = getShpFeatures("Poi","C:/map/shps/scenic_spot_C_f/Scenic_spot_C_f.shp")
print(all_features)


app.exitQgis()
