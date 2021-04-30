#%%
import pandas as pd
import altair as alt 

#%%
alt.data_transformers.enable('json')

#%%
url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'

df = pd.read_csv(url)
df
#%%
