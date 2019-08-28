# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:33:58 2019

@author: marcelo.oliveira
"""
import FacebookGetData
import time 
import pandas as pd
from datetime import date, timedelta
import xlsxwriter
#from bson.json_util import dumps

yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime('%d%m%y')

# 'S2G_AccountId'
# 'OQV_AccountId'
start_time = time.time()

s2gPath = ".../FacebookAds - S2G - " + yesterday +".xlsx"
#s2gPath = "../FacebookAds - S2G- " + yesterday +".csv"
oqvPath = ".../FacebookAds - OQV - " + yesterday +".xlsx"
#oqvPath = ".../FacebookAds - OQV- " + yesterday +".csv"

accounts = ['_AccountId','_AccountId']
#import qgrid
import FacebookGetData

def printGetData():
    for acc in accounts:
        if 'S2G' in acc:
            print('Downloading Data')
            print('...')        
            #df = []
            S2G = FacebookGetData.get_fb_data(acc)
            S2G.to_excel(s2gPath,engine="openpyxl",index=False,encoding='utf-8-sig')
            #S2G.to_csv(s2gPath,encoding='utf-8-sig',index=False, sep=';',date_format='%d-%m-%Y')
            print('S2G Downloaded\n')
        elif 'OQV' in acc:
            print('Downloading OQV Data ')
            print('...')
            OQV = FacebookGetData.get_fb_data(acc)
            OQV.to_excel(oqvPath,engine="openpyxl",index=False,encoding='utf-8-sig')
            
            #baseS2g.to_excel(ano,engine='openpyxl',index=False,encoding='utf-8-sig')
            #OQV.to_csv(oqvPath,encoding='utf-8-sig',index=False,sep=';',date_format='%d-%m-%Y')
            print('OQV Downloaded\n')

printGetData()

elapsed = time.time() - start_time
print(round(elapsed,2), 'sec \n')       
print('Finished, Bye')
        
