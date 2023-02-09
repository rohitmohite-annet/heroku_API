import pandas as pd
import random
import datetime
import string
def genrate_data():
    leads_number=[i for i in range(10)]
    lead_names = [letter for letter in string.ascii_lowercase[:10]]
    dates = [datetime.datetime.now() + datetime.timedelta(days=random.randint(-1000, 1000)) for i in range(10)]

    df = pd.DataFrame({'leads':leads_number,'name':lead_names,'Date': dates})

    # Print the dataframe
    return df
