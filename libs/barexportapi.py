import xlwings as xw
import shutil
import os
import numpy as np

from barcutclass import RebarCache

TEMPLATE_PATH = r"C:\Users\saris\AppData\Roaming\pyRevit\Extensions\rebarcutting.extension\Cutting_Template.xlsx"
CUTOFF = 20

def exportToExcel(exportWBPath: str, stockLength):
    try:
        if os.path.isfile(exportWBPath):
            os.remove(exportWBPath)

        shutil.copyfile(TEMPLATE_PATH, exportWBPath)
    except PermissionError:
        return

    exportWB = xw.Book(exportWBPath)

    exportWB.app.screen_updating = False
    exportWB.app.calculation = 'manual'

    for diameter, barDemand in RebarCache.rebarCache.items():

        demandDf = barDemand.demandSchedule()
        rebarResult = RebarCache.rebarResult.get(diameter)
        resultResultSchedule = rebarResult.cuttingSchemeSchedule()
        demandDf['Multiply'] = demandDf['Required Length (mm)'] * demandDf['Demand (Nos)']

        if demandDf.shape[0] >= CUTOFF:
            sheet = exportWB.sheets['Big'].copy(name=f'D_{diameter:.2f}mm')
            sheet.range('D9').value = stockLength
            sheet.range('D10').value = barDemand.diameter
            sheet.range('C93').value = barDemand.fullStock
            
            sheet.range('C95').value = demandDf['Multiply'].sum() / 1000
            sheet.range('C96').value = rebarResult.totalLength / 1000

            sheet.range('H93').value = rebarResult.requiredRoll
            sheet.range('H94').value = rebarResult.requiredRoll * stockLength / 1000
            sheet.range('H95').value = rebarResult.waste / 1000
            sheet.range('H96').value = (rebarResult.waste / (rebarResult.requiredRoll * stockLength)) * 100
            sheet.range('H97').value = rebarResult.requiredRoll + barDemand.fullStock
        else:
            sheet = exportWB.sheets['Small'].copy(name=f'D_{diameter:.2f}mm')
            sheet.range('D9').value = stockLength
            sheet.range('D10').value = barDemand.diameter
            sheet.range('C36').value = barDemand.fullStock

            sheet.range('C38').value = demandDf['Multiply'].sum() / 1000
            sheet.range('C39').value = rebarResult.totalLength / 1000

            sheet.range('H36').value = rebarResult.requiredRoll
            sheet.range('H37').value = rebarResult.requiredRoll * stockLength / 1000
            sheet.range('H38').value = rebarResult.waste / 1000
            sheet.range('H39').value = (rebarResult.waste / (rebarResult.requiredRoll * stockLength)) * 100
            sheet.range('H40').value = rebarResult.requiredRoll + barDemand.fullStock

        paste2DList(sheet, 14, 2, demandDf.iloc[:, [0, 1]].to_numpy())
        paste2DList(sheet, 14, 6, resultResultSchedule.to_numpy())
        
    exportWB.sheets['Big'].api.Visible = False
    exportWB.sheets['Small'].api.Visible = False
    exportWB.app.screen_updating = True
    exportWB.app.calculation = 'automatic'
    exportWB.save()

def paste1DListRight(sheet, row, column, oneDArray):
    sheet.range((row, column), (row, column + len(oneDArray))).value = np.expand_dims(oneDArray, axis=0)

def paste1DListDown(sheet, row, column, oneDArray):
    sheet.range((row, column), (row + len(oneDArray), column)).value = np.expand_dims(oneDArray, axis=1)

def paste2DList(sheet, row, column, twoDArray):
    rowCount, columnCount = twoDArray.shape
    sheet.range((row, column), (row + rowCount, column + columnCount)).value = twoDArray