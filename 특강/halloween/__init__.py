import pandas as pd

class Halloween():
    def __init__(self, df, start_year, end_year):
        self.df = df
        self.start_year = start_year
        self.end_year = end_year
        self.acc_rtn = 1
    
    def AccRtn(self):
        self.acc_rtn = 1

        for year in range(self.start_year, self.end_year):
            self.buy_mon = str(year) + "-11"
            self.sell_mon = str(year+1) + "-04"

            self.buy = self.df.loc[self.buy_mon].iloc[0]['Open']
            self.sell = self.df.loc[self.sell_mon].iloc[-1]['Close']

            self.rtn = self.sell / self.buy

            self.acc_rtn *= self.rtn
        return self.acc_rtn
    
    def CAGR(self):
        self.due = self.end_year - self.start_year
        self.cagr = (self.acc_rtn ** (1 / self.due)) - 1
        return self.cagr * 100