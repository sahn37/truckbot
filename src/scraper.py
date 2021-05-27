from craigslist import CraigslistForSale
import pandas as pd
import time
from discord_bot import notify


int_sleep = 60
df_trucks_old_scrape = None

while True:
    # print('starting scraping')
    
    # if df_trucks_old_scrape is not None:
    #     print('one time hack')
    #     df_trucks_old_scrape = df_trucks_old_scrape.tail(df_trucks_old_scrape.shape[0]-1)
    
    # print('about to scrape')
    cl_s = CraigslistForSale(site='washingtondc', area=None, category='cto',
                             filters={'auto_bodytype': u'truck', 'auto_transmission': u'manual'})
    
    # print('parsing result')
    df_trucks_new_scrape = pd.DataFrame(cl_s.get_results(sort_by='newest', geotagged=True))
    
    try:
        # print('trying')
        df_trucks_diff = df_trucks_new_scrape[~df_trucks_new_scrape['id'].isin(df_trucks_old_scrape['id'])]
    
        if df_trucks_diff.shape[0] > 0:
            # print('new truck found')
            for url in df_trucks_diff['url'].tolist():
                notify('NEW TRUCK FOUND: {0}'.format(url))
        else:
            # print('nothing new found')
            time.sleep(int_sleep)
        
    except TypeError:
        # print('typeerror')
        pass
    
    finally:
        # print('finally')
        df_trucks_old_scrape = df_trucks_new_scrape.copy()