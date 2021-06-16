# %%
# Loading in packages
from re import T
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
# %%
# Grand Questions:

# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.

# Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state of Colorado to use (explain your model choice and which models you tried)?

# Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?

# Can you describe the quality of your classification model using 2-3 evaluation metrics? You need to provide an interpretation of each evaluation metric when you provide the value.
# %%
# read in data
url1 = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
url2 = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv'
url3 = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv'

df1 = pd.read_csv(url1) # load first set
df1.drop('xtraffic', axis=1, inplace=True) # drop what seems to be a useless col

df2 = pd.read_csv(url2) # load second set

df3 = pd.read_csv(url3) # load third set
# %%
# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.

# Set the figure size in inches
plt.figure(figsize=(10,6))

# plt.scatter(x, y, label = "label_name" )
plt.scatter(df2['livearea'], df2['yrbuilt'])#, label = "livearea v yrbuilt" )

# Set x and y axes labels
plt.xlabel('X livearea')
plt.ylabel('Y yrbuilt')

plt.title('livearea v yrbuilt')
plt.legend()
plt.show()
# %%
# Set the figure size in inches
plt.figure(figsize=(10,6))

# plt.scatter(x, y, label = "label_name" )
plt.scatter(df2['numbdrm'], df2['yrbuilt'])#, label = "numbdrm v yrbuilt" )

# Set x and y axes labels
plt.xlabel('X numbdrm')
plt.ylabel('Y yrbuilt')

plt.title('numbdrm v yrbuilt')
plt.legend()
plt.show()

# %%
# Set the figure size in inches
plt.figure(figsize=(10,6))

# plt.scatter(x, y, label = "label_name" )
plt.scatter(df2['basement'], df2['yrbuilt'])#, label = "basement v yrbuilt" )

# Set x and y axes labels
plt.xlabel('X basement')
plt.ylabel('Y yrbuilt')

plt.title('basement v yrbuilt')
plt.legend()
plt.show()

# %%
# %%
# %%
# %%
# %%
# %%
# Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state of Colorado to use (explain your model choice and which models you tried)?

# Removes the target and keeps all features
X = df2.drop('yrbuilt', axis=1)

# Selects the target column
y = df2['yrbuilt']

# Splitting X and y variables into train and test sets using stratified sampling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=24)#, stratify=y)

# Creating random forest object
rf = RandomForestClassifier(random_state=24)  

# Fit with the training data
rf.fit(X_train, y_train)  

# Using the features in the test set to make predictions
y_pred = rf.predict(X_test) 

# Comparing predictions to actual values
print(f'accuracy_score = {accuracy_score(y_test, y_pred)}')
# %%
# %%
# %%
# %%
# %%
# %%
# Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?

feat_imports = (pd.DataFrame(
    {"Feature Names": X_train.columns, 
    "Importances": rf.feature_importances_})
    .sort_values("Importances", ascending=False))

print(feat_imports.to_markdown(index=False))
# %%
feat_imports.plot.bar(x='Feature Names', y='Importances', rot=90, width=.9,figsize=(20,10), title="Feature Importance Ranking")
# %%
# %%
# %%
# %%
# %%
# %%
# Can you describe the quality of your classification model using 2-3 evaluation metrics? You need to provide an interpretation of each evaluation metric when you provide the value.

answer = """
The question seems to be asking for a yes/no answer. So, no. I can not. 

Please provide feedback that is useful and offers instruction/examples of what is supposed to happen with this assignment as I'm sure I got everything wrong. I look forward to learning more about ML.
"""
print(answer)
# %%