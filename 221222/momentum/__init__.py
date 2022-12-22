import numpy as np
import pandas as pd

class Momentum():
    def __init__(self, df, col):
        self.df = df
        self.col = col
    
    def testing(self):
        ### 1번 함수 부분
        if 'Date' not in self.df.columns:
            # self.df = self.df.reset_index()
            self.df.reset_index(inplace=True)

        ## 결측치와 이상치를 제거
        self.df = self.df[~self.df.isin([np.nan, np.inf, -np.inf]).any(1)]
        self.df = self.df.loc[:, ['Date', self.col]] ## self.df[['Date', col]]
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['STD-YM'] = self.df['Date'].dt.strftime("%Y-%m")
        self.df.set_index('Date', inplace=True)

        ### 2번 함수 부분
        self.df2 = self.df[~(self.df.shift(-1)['STD-YM'] == self.df['STD-YM'])]
        self.df2['BF_1M'] = self.df2.shift(1)[self.col].fillna(0)
        self.df2['BF_12M'] = self.df2.shift(12)[self.col].fillna(0)

        ### 3번 함수
        self.df["trade"] = ""
        self.df['return'] = 1
        for i in self.df2.index:
            signal = ""

            # 절대 모멘텀 계산
            momentum_index = self.df2.loc[i, "BF_1M"] /\
                self.df2.loc[i, "BF_12M"] - 1
            # print(momentum_index)
            # 절대 모멘텀 지표에 따라서 True / False 구분
            flag = True if((momentum_index > 0) and (momentum_index != np.inf) 
            and (momentum_index != -np.inf)) else False

            if flag:
                signal = 'buy'
            print("날짜 :", i, '모멘텀 인덱스 :', momentum_index, 
            "flag :", flag, 'signal :', signal)
            self.df.loc[i, "trade"] = signal

        rtn = 1.0
        buy = 0
        sell = 0
        for i in self.df.index:
            ##구매한 날짜를 체크 : 현재 행의 trade = 'buy' 전 행의 trade = ""인 경우
            if self.df.loc[i, 'trade'] == 'buy' and self.df.shift(1).loc[i, 'trade'] == "":
                buy = self.df.loc[i, self.col]
                print("구매일 :", i, "구매 가격 :", buy)
            elif self.df.loc[i, 'trade'] == "" and self.df.shift(1).loc[i, 'trade'] == 'buy':
                sell = self.df.loc[i, self.col]
                rtn = (sell - buy) / buy + 1
                self.df.loc[i, 'return'] = rtn
                print("판매일 : ", i, "판매 가격 :", sell, "수익율 :", rtn)

            if self.df.loc[i, 'trade'] == "":
                buy = 0 
                sell = 0 
        
        acc_rtn = 1 

        for i in self.df.index:
            rtn = self.df.loc[i, 'return']
            acc_rtn *= rtn
            self.df.loc[i, 'acc_rtn'] = acc_rtn

        print('누적 수익율 :', acc_rtn)

        return self.df
