# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:47:41 2019

@author: marcelo.oliveira
"""

from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.adobjects.adaccount import AdAccount
import facebookConfig 
import FacebookNormalizeData as normalize
import pandas as pd
 
def get_fb_data(AccountId):
    FacebookAdsApi.init(facebookConfig.Configs['App_id'], facebookConfig.Configs['App_secret'], facebookConfig.Configs['Access_token'])

    my_account = AdAccount(facebookConfig.Accounts[AccountId])
         
    # Grab insight info for all ads in the adaccount
    
    #Ever this function will get data from yesterday
    #If somebody wants to change the range of date, is necessary to change the param 'date_preset'
    #You can change the level of your request. example: ad, adset or campaign
    
    '''
    I dont recommend change the param date_preset because the data comes cumulative, not good for me.
    The data from yesterday is better and trustworthy . I suggest to compare with reports from your Business manager facebook
    '''
    data = my_account.get_insights(params={'date_preset':'yesterday','level':'ad'},
                                     fields=[AdsInsights.Field.account_id,
                                             AdsInsights.Field.account_name,
                                             #AdsInsights.Field.campaign_id,
                                             AdsInsights.Field.campaign_name,
                                             AdsInsights.Field.ad_name,
                                             AdsInsights.Field.ad_id,
                                             AdsInsights.Field.adset_id,
                                             AdsInsights.Field.adset_name,
                                             AdsInsights.Field.cost_per_outbound_click,
                                             AdsInsights.Field.outbound_clicks,
                                             AdsInsights.Field.spend,
                                             AdsInsights.Field.clicks,
                                             AdsInsights.Field.inline_link_clicks,
                                             AdsInsights.Field.inline_link_click_ctr,
                                             AdsInsights.Field.cpm,
                                             AdsInsights.Field.ctr,
                                             AdsInsights.Field.reach,
                                             AdsInsights.Field.frequency,
                                             AdsInsights.Field.impressions])
    
    dataNormalize = normalize.dumps_data(data)
    
    df = normalize.change_types(dataNormalize)
    
    return df


