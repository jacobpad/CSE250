#%%
# import sys
# !{sys.executable} -m pip install datadotworld
#%%
import datadotworld as dw

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM allstarfull LIMIT 5')

print(results.dataframe)
# %%
# Exercise 1

# a. What is the name of the table that records data about pitchers in the regular seasons?

# pitching from Pitching.csv

# b. What do the HR and HBP columns mean in that table respectively?

# HR             Homeruns
# HBP            Batters Hit By Pitch

# %%
# Exercise 2 SELECT and FROM

# Create a query that shows all columns from the table you found in Exercise 1, save the dataframe in a variable “pitch”
# result = dw.query('byuidss/cse-250-baseball-database', 
#     'SELECT _______ FROM _______')

result = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM pitching;')

ex2_select_from = result.dataframe
ex2_select_from

# %%
# Excercise 2 WHERE

# a. Using a SQL query, select all rows in the same table where HR is lesser than 10 and gs is greater than 25.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT playerID, hr, gs FROM pitching
    WHERE hr < 10 AND gs > 25;
    ''')

ex2_where = result.dataframe
ex2_where

# b. Find out what the columns mean and explain your query in words

# HR             Homeruns - homeruns given up
# GS             Games Started - Num of games pitcher started
# %%
# Excercise 3 ORDER BY

# Using the same query in exercise 2, edit it so that the table is ordered by the year of the season(nearest to furthermost) and the player ID(alphabetically).

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT playerID, yearID, hr, gs FROM pitching
    WHERE hr < 10 AND gs > 25
    ORDER BY yearID DESC, playerID
    ;
    ''')

ex3_order = result.dataframe
ex3_order
# %%
# Excercise 4 Joins

# Identify the shared columns (keys) and join the table in exercise 2 with the salaries table, then filter the data so that it shows only pitchers in the year 1986.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT p.playerID, p.yearID, p.hr, p.gs, s.salary 
    FROM pitching AS p
    JOIN salaries s ON p.playerid = s.playerid
    WHERE hr < 10 AND gs > 25 AND p.yearID = 1986
    ;
    ''')

ex4_joins = result.dataframe
ex4_joins

# %%
# Exercise 5 Group By

# Create a query that captures the number of pitchers the Washington Nationals used in each year, then sort the table by year

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT yearid, COUNT(DISTINCT playerid)
    FROM pitching
    WHERE teamid = 'WAS'
    GROUP BY yearid
    ORDER BY yearid;
    ''')

ex5_group_by = result.dataframe
ex5_group_by

# %%
# Exercise 6 For The Overachievers

## Research the order of operations for SQL and put the following keywords in that order.

# The order is FROM JOIN WHERE GROUP BY HAVING SELECT ORDER BY LIMIT