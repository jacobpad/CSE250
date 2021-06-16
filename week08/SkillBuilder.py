# %%
# import sys
# !{sys.executable} -m pip install scikit-learn
# !{sys.executable} -m pip install seaborn
# %%
# Loading in packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Loading in data
url = "https://byuistats.github.io/CSE250-Course/skill_builders/ml_sklearn/machine_learning.csv"
df = pd.read_csv(url)
# %%
df
# %%
for i in df.columns:
    print(i)
# %%
# Exercise 1

chart = (
    alt.Chart(df)
    .mark_area(opacity=0.3)
    .encode(x="age", y="survived")
    .properties(width=400, title="Age vs Survived")
)
chart

# %%
title = "Does age affect whether a passenger survived?"
chart1 = alt.Chart(df, title=title).transform_density(
    "age",
    as_=["age", "density"],
    groupby=["survived"]
).mark_area(opacity=.5).encode(
    alt.X("age:Q"),
    alt.Y("density:Q"),
    alt.Color("survived:N")
).configure_title(anchor="start")

chart1

# %%

# Exercise 2

# Step 0: Split the data into X and y variables
# The X variable will contain all your features
X = df.drop("survived", axis=1)  
y = df['survived']  

# Step 1: Split data into train and test sets
# Splitting X and y variables into train and test sets using stratified sampling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=24, stratify=y)

# Step 2
# Creating random forest object
rf = RandomForestClassifier(random_state=24)  
# Fit with the training data
rf.fit(X_train, y_train)

# Step 3
# Using the features in the test set to make predictions
y_pred = rf.predict(X_test)

# Step 4
# Comparing predictions to actual values
accuracy_score(y_test, y_pred)  

# %%

# Exercise 3
feat_imports = (pd.DataFrame(
    {"Feature Names": X_train.columns, 
    "Importances": rf.feature_importances_})
    .sort_values("Importances", ascending=False))

print(feat_imports.to_markdown(index=False))
# %%
