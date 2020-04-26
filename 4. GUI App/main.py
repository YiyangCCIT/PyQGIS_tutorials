# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.PyQt.QtGui import (
    QColor,
)

from qgis.PyQt.QtCore import Qt, QRectF

from qgis.core import (
    QgsVectorLayer,
    QgsPoint,
    QgsPointXY,
    QgsProject,
    QgsGeometry,
    QgsMapRendererJob,
)

from qgis.gui import (
    QgsMapCanvas,
    QgsVertexMarker,
    QgsMapCanvasItem,
    QgsRubberBand,
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadShp = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadShp.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.btnLoadShp.setObjectName("btnLoadShp")
        self.myMap = QgsMapCanvas(self.centralwidget)
        self.myMap.setGeometry(QtCore.QRect(0, 30, 501, 481))
        self.myMap.setObjectName("myMap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnLoadShp.clicked.connect(self.loadShp)

    def loadShp(self):
        canvas = self.myMap
        canvas.setCanvasColor(Qt.white)
        canvas.enableAntiAliasing(True)
        vlayer = QgsVectorLayer("C:/map/shps/scenic_spot_C_f/Scenic_spot_C_f.shp", "POI layer", "ogr")
        if not vlayer.isValid():
            print("Layer failed to load!")

        # add layer to the registry
        QgsProject.instance().addMapLayer(vlayer)

        # set extent to the extent of our layer
        canvas.setExtent(vlayer.extent())

        # set the map canvas layer set
        canvas.setLayers([vlayer])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoadShp.setText(_translate("MainWindow", "Load shape file"))

from qgis.gui import QgsMapCanvas

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

