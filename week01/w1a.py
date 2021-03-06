# %%
import pandas as pd
import altair as alt

# %%
alt.data_transformers.enable("json")

# %%
# Reading in data
url = (
    "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
)
mpg = pd.read_csv(url)
mpg

# %%
displ_vs_hwy = alt.Chart(mpg).encode(x="displ", y="hwy").mark_circle()
displ_vs_hwy

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
mpg.shape

# %% [markdown]

# What does the `drv` variable describe? According to the [data](https://github.com/byuidatascience/data4python4ds/blob/master/data.md#fuel-economy-data-from-1999-to-2008-for-38-popular-models-of-cars) `drv` means "the type of drive train, where f = front-wheel drive, r = rear wheel drive, 4 = 4wd"

# %%
# Make a scatterplot of `hwy` vs `cyl`
hwy_vs_cyl_chart = alt.Chart(mpg).encode(x="cyl", y="hwy").mark_circle()
hwy_vs_cyl_chart


# %%
# What happens if you make a scatterplot of `class` vs `drv`? Why is the plot not useful?
# It has nothing to prove regarding the hypothesis that "cars with big engines use more fuel."
class_vs_drv_chart = alt.Chart(mpg).encode(x="class", y="drv").mark_circle()
class_vs_drv_chart

# %%
# Save the chart required
displ_vs_hwy.save("displ_vs_hwy.png")
# %%
