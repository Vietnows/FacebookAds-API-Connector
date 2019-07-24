# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:10:49 2019

@author: marcelo.oliveira
"""
from pandas.io.json import json_normalize
from bson.json_util import dumps
import json
import pandas as pd


''' 
Pay attention!!!

I suppose that data is stored in mongodb database, then the data cames like cursor mongodb.

Below I do this code to dump the data and convert to string and after convert to json. 
After this I normalize the data with json_normalize that returns a pandas Dataframe.
'''
def dumps_data(data):
    dataDumps = dumps(data)
    dataDumpJson = json.loads(dataDumps)
    dataNormalize = json_normalize(dataDumpJson)
    
    return dataNormalize

'''
Below I change the types of the columns.
'''
def change_types(dataNormalize):
    dataNormalize['spend'] = dataNormalize['spend'].apply(float)
    dataNormalize['cpm'] = dataNormalize['cpm'].apply(float)
    dataNormalize['inline_link_click_ctr'] = dataNormalize['inline_link_click_ctr'].apply(float)
    dataNormalize['impressions'] = dataNormalize['impressions'].apply(int)
    dataNormalize['inline_link_clicks'] = dataNormalize['inline_link_clicks'].apply(int)
    dataNormalize['reach'] = dataNormalize['reach'].apply(int)
    dataNormalize = dataNormalize.fillna(0)
    
    return dataNormalize