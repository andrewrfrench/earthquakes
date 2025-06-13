import numpy as np
import pandas as pd
import requests
from datetime import datetime



def get_quakes(form, orderby, limit):
    """
    Simple function to get a DataFrame of EarthQuake data from USGS API
    Must choose params from USGS API in dictionary key:value pairs
    https://earthquake.usgs.gov/fdsnws/event/1/query%22
    """
    
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    
    params = {
        "format": form,
        "orderby": orderby,
        "limit": limit,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200: 
        data = response.json()
        data = data['features']
        count = params['limit']
        rows = []
        for i in data:
            p_dict = {"code":  data[3-count]['properties']['code'],
                    "place": data[3-count]['properties']['place'],
                    "magnitude" : data[3-count]['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(data[3-count]['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": data[3-count]["geometry"]["coordinates"][0],
                    "latitude": data[3-count]["geometry"]["coordinates"][1]
                    }
            count -= 1
            q_dict = pd.DataFrame.from_dict(p_dict,orient='index').T
            rows.append(q_dict)
        df = pd.concat(rows).reset_index(drop=True)
        return df
