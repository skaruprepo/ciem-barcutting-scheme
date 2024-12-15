from ast import Raise
import numpy as np
import pandas as pd
import math

from Autodesk.Revit import DB
from barcutclass import BarDemand, DemandID, RebarCache

def feetToMM(v):
    return v * 304.8

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def getBarData(stockLength: float, debug = False):

    doc = __revit__.ActiveUIDocument.Document
    collector = DB.FilteredElementCollector(doc).OfClass(DB.Structure.Rebar)

    for element in collector:
        if isinstance(element, DB.Structure.Rebar):

            diameter = feetToMM(element.get_Parameter(DB.BuiltInParameter.REBAR_BAR_DIAMETER).AsDouble())
            diameter = round(diameter, 0)
            barLength = feetToMM(element.get_Parameter(DB.BuiltInParameter.REBAR_ELEM_LENGTH).AsDouble())
            elementID = element.Id.IntegerValue
            quantity = element.Quantity
           
            fullStock = 0
           
            if barLength > stockLength:
                fullStock = np.floor(barLength / stockLength)
                residual = barLength - fullStock * stockLength
            else:
                residual = barLength

            # Rounding to near 10 for resolution
            residual = roundup(residual)

            if debug:
                print(f"Element ID: {elementID} have {quantity} Nos.")
                print(f"Diameter: diameter {diameter} mm")
                print(f"Total Stock: {fullStock}, Residual: {residual} mm")

            barDemand = RebarCache.rebarCache.get(diameter)

            if barDemand is None:
                demand = DemandID(residual, [elementID] * quantity)
                demandDict = {residual: demand}
                barDemand = BarDemand(diameter, fullStock, demandDict)

                RebarCache.rebarCache[diameter] = barDemand
            else:
                if barDemand.diameter != diameter:
                    raise Exception("Bar diameter is not matched, Internal Error !")
                
                barDemand.fullStock = barDemand.fullStock + fullStock

                demandDict = barDemand.demandDict
                if residual not in demandDict.keys():
                    demand = DemandID(residual, [elementID] * quantity)
                    demandDict[residual] = demand
                
                else:
                    demand = demandDict.get(residual)
                    if demand.requiredLength != residual:
                        raise Exception("Initialize bar demand is not matched, Internal Error !")
                    demand.elementIDList = demand.elementIDList + [elementID] * quantity

            
            if debug:
                for diameter, barDemand in RebarCache.rebarCache.items():
                    print("# ==== REBAR CACHE =====")
                    print(f"Diameter: {diameter:.2f} mm")
                    print(f"Requried Full Stock: {barDemand.fullStock:.0f} EA")
                    print(barDemand.demandSchedule())
        
    return
            
