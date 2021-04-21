# %%
import sys
!{sys.executable} -m pip install pandas vega
# #%%
# import sys
# !{sys.executable} -m pip install altair
# !{sys.executable} -m pip install altair_saver
# #%%
# import sys
# !{sys.executable} export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib"
# #%%
# import os
# os.system('npm install -g vega-lite vega-cli canvas')
# %%
# "cmd+shift+p - interactive python"

import pandas as pd
import altair as alt
#from altair_saver import save
import altair_viewer

# %%
# alt.data_transformers.enable('json')

# %%
# Reading in data
url = (
    "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
)
mpg = pd.read_csv(url)
mpg
# %%
displ_vs_hwy = alt.Chart(mpg).mark_circle().encode( #re-arranged the .mark_circle() here
    x='displ',
    y='hwy')
displ_vs_hwy
# altair_viewer.show(displ_vs_hwy) # try this when showing the chart

# %%
# I'm not too sure about this part of the reading/assignmemnt

# chart = (alt.Chart(<DATA>)
#    .encode(<ENCODINGS>)
#     <.mark_*()>)

# %%
# Run Chart(mpg).mark_point(). What do you see?
alt.Chart(mpg).mark_point()

# %%
# The shape of mpg is 234 rows, 11 columns
mpg.shape #FYI - this is not producing an output

# %% [markdown]
'''
What does the drv variable describe? According to the [data](https://github.com/byuidatascience/data4python4ds/blob/master/data.md#fuel-economy-data-from-1999-to-2008-for-38-popular-models-of-cars) drv means "the type of drive train, where f = front-wheel drive, r = rear wheel drive, 4 = 4wd"
'''
# %%
# Make a scatterplot of `hwy` vs `cyl`
hwy_vs_cyl_chart = alt.Chart(mpg).encode(x="cyl", y="hwy").mark_circle()
#hwy_vs_cyl_chart #fix per above​
# %%
# What happens if you make a scatterplot of `class` vs `drv`? Why is the plot not useful?
# It has nothing to prove regarding the hypothesis that "cars with big engines use more fuel."
class_vs_drv_chart = alt.Chart(mpg).encode(x="class", y="drv").mark_circle()
#class_vs_drv_chart #fix per above

# %%
# Save the chart required
displ_vs_hwy.save('displ_vs_hwy1.png') #try single quotes not double
# %%
#save(class_vs_drv_chart, 'chart.png')
displ_vs_hwy.save('chartName.png')
# %%