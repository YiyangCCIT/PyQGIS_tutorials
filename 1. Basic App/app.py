from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep

    
    
app = QgsApplication([], True)
app.setPrefixPath("C:/Program Files/QGIS 3.10/apps/qgis", True)
app.initQgis()

project = QgsProject.instance()

project.read('C:/map/sample.qgz')

# Do something

app.exitQgis()
