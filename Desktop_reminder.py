import numpy as np
import pandas as pd
from random import sample
import time
from plyer import notification 

df = pd.read_csv("C:\\Users\\Shambhavi\\Desktop\\Projects\\Daily Word\\dictionary.csv")

while(True):
        rindex =  np.array(sample(range(len(df)), 1))
        msg = df.loc[rindex].to_string(index = False, header = False)
        notification.notify(
            title = "Word of the day!",
            message = '''{}'''.format(msg),
            app_icon = "icon.ico",
            timeout  = 30
        )

        time.sleep(60*60*4)
