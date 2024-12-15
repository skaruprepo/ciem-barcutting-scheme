from barcutclass import BarResult, RebarCache
from stock_cutter_1d import *
import pandas as pd
import numpy as np

def getCuttingScheme(stockLength, demandDf: pd.DataFrame, diameter):
    parentRolls = [[stockLength, ]]
    childRolls = []

    for ___, row in demandDf.iterrows():
        residual = row['Required Length (mm)']
        demand = row['Demand (Nos)']
        childRolls.append([demand, residual])

    cuttingScheme = StockCutter1D(childRolls, parentRolls, output_json=False, large_model=True, cutStyle='minWaste')
    requiredRoll = len(cuttingScheme)

    totalLength = 0
    for roll in cuttingScheme:
        totalLength += sum(roll[1])

    waste = parentRolls[0][0] *  len(cuttingScheme) - np.sum(demandDf.iloc[:, 1].to_numpy() * demandDf.iloc[:, 0].to_numpy())

    barResult = BarResult(requiredRoll, totalLength, waste, cuttingScheme)
    RebarCache.rebarResult[diameter] = barResult
    return