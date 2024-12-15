from dataclasses import dataclass
from typing import Any, Dict, List
import pandas as pd
import numpy as np

class DemandID():
    def __init__(self, requiredLength: float, elementIDList: List[int]):
        self.requiredLength = requiredLength
        self.elementIDList = elementIDList
        

class BarDemand():
    def __init__(self, diameter: float, fullStock: int, demand: Dict[float, DemandID]):
        self.diameter = diameter
        self.fullStock = fullStock
        self.demandDict = demand

    def demandSchedule(self):
        demandDf = pd.DataFrame(columns=['Required Length (mm)', 'Demand (Nos)'])
        i = 0
        for requiredLength, DemandID in self.demandDict.items():
            demandDf.loc[i] = np.array([DemandID.requiredLength, len(DemandID.elementIDList)])
            i += 1

        return demandDf

@dataclass
class BarResult():
    requiredRoll: int
    totalLength: float
    waste: float
    cuttingScheme: Any

    def cuttingSchemeSchedule(self):
        
        cuttingSchemeDf = pd.DataFrame(columns=['Nos', 'Pattern', 'Residual'])
        nRow = 0

        for _, roll in enumerate(self.cuttingScheme):
            residual, pattern = roll[0], roll[1]
            if cuttingSchemeDf[cuttingSchemeDf['Pattern'] == str(pattern)].shape[0] == 0:
                cuttingSchemeDf.loc[nRow] = [1, str(pattern), residual]
                nRow += 1
            else:
                value = cuttingSchemeDf.loc[cuttingSchemeDf['Pattern'] == str(pattern),'Nos']
                cuttingSchemeDf.loc[cuttingSchemeDf['Pattern'] == str(pattern),'Nos'] = value + 1

        return cuttingSchemeDf

class RebarCache():

    rebarCache: Dict[int, BarDemand] = {}
    rebarResult: Dict[int, BarResult] = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RebarCache, cls).__new__(cls)
        return cls.instance

    @classmethod
    def clearCache(cls):
        cls.rebarCache = {}
        cls.rebarResult = {}
