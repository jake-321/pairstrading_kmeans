from AlgorithmImports import *
from statsmodels.tsa.stattools import coint
import numpy as np
from scipy.stats import norm

class FatFluorescentOrangeDinosaur(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2023, 1, 1)
        self.SetEndDate(2024, 12, 1)
        self.SetCash(100000)
        self.SetBenchmark("SPY")

        self.symbol1 = self.AddEquity("NVDA", Resolution.Daily).Symbol
        self.symbol2 = self.AddEquity("WMT", Resolution.Daily).Symbol

        self.lookback = 20

        self.price_window1 = RollingWindow[float](self.lookback)
        self.price_window2 = RollingWindow[float](self.lookback)

    def OnData(self, data: Slice):
        if self.symbol1 not in data.Keys or self.symbol2 not in data.Keys:
            return

        self.price_window1.Add(data[self.symbol1].Close)
        self.price_window2.Add(data[self.symbol2].Close)

        if self.price_window1.Count < self.lookback:
            return

        z_score = self.calculate_z_score(self.price_window1, self.price_window2)

        if z_score > 1:
            self.SetHoldings(self.symbol1, -0.5)
            self.SetHoldings(self.symbol2, 0.5)
        elif z_score < -1:
            self.SetHoldings(self.symbol1, 0.5)
            self.SetHoldings(self.symbol2, -0.5)
        else:
            self.Liquidate()

    def calculate_z_score(self, window1, window2):
        # Calculate spread between the two assets
        prices1 = np.array([i for i in window1])
        prices2 = np.array([i for i in window2])
        spread = np.log(prices1 / prices2)

        spread_mean = np.mean(spread)
        spread_std = np.std(spread)

        z_score = (spread[-1] - spread_mean) / spread_std

        return z_score