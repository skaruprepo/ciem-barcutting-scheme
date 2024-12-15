
import time
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon

from barcutting import getCuttingScheme
from bardata import getBarData
from barexportapi import exportToExcel
from maingui_uic import Ui_MainGUI
from barcutclass import RebarCache

class MainGUI(QMainWindow):
    
    def __init__(self):
        super(MainGUI, self).__init__()
        self.ui = Ui_MainGUI()
        self.ui.setupUi(self)

        self.ui.btnSearchPath.clicked.connect(self.searchExportPath)
        self.ui.btnRun.clicked.connect(self.runScript)
        self.ui.actionClear.triggered.connect(self.clearGUI)

        self.setWindowIcon(QIcon('icon.png'))

    def clearGUI(self):
        self.ui.stockLength.clear()
        self.ui.outputPath.clear()

    def searchExportPath(self):
        filepath, _ = QFileDialog.getSaveFileName(self,"Choose File", "","Excel (*.xlsx)|*.xlsx||", )
        if filepath:
            self.ui.outputPath.setText(filepath)

    def runScript(self):
         
        startTime = time.time()
        stockLength = float(self.ui.stockLength.text())
        exportPath = self.ui.outputPath.text()

        getBarData(stockLength, debug=False)

        for diameter, barDemand in RebarCache.rebarCache.items():

            demanDf = barDemand.demandSchedule()
            getCuttingScheme(stockLength, demanDf, diameter)
            
            rebarResult = RebarCache.rebarResult.get(diameter)
            requiredRoll, totalLength, waste = rebarResult.requiredRoll, rebarResult.totalLength, rebarResult.waste
            cuttingScheme = rebarResult.cuttingScheme
        
        exportToExcel(exportPath, stockLength)

        endTime = time.time()
        QMessageBox.information(self, "Success", f"Elapsed Time: {endTime - startTime:.2f} s")