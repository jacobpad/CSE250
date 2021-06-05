# %%
import datadotworld as dw
import pandas as pd
import altair as alt

# import sys
# !{sys.executable} -m pip install tabulate
# %%
# Grand Question 1
# 
# Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. 
# The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    p.playerid
    , c.schoolid
    , s.salary
    , s.yearid
    , s.teamid
    FROM people p
    JOIN collegeplaying c ON p.playerid = c.playerid
    JOIN salaries s on c.playerid = s.playerid
    WHERE c.schoolid = 'idbyuid'
    ORDER BY s.salary DESC
    ;
    ''')

gq1 = result.dataframe
print(gq1.head(3).to_markdown())
gq1

# %%
# Grand Question 2
# 
# This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)
# 
# Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.
# 
# Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.
# 
# Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.

# %%
# Part 1
# Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    playerid
    , yearid
    , h/ab AS batting_average
    FROM batting
    WHERE h >= 1
    ORDER BY batting_average DESC
    LIMIT 5
    ;
    ''')

gq2a = result.dataframe
print(gq2a.head(3).to_markdown())
gq2a

# %%
# Part 2
# Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    playerid
    , yearid
    , h/ab AS batting_average
    FROM batting
    WHERE ab >= 1
    ORDER BY batting_average DESC
    LIMIT 5
    ;
    ''')

gq2b = result.dataframe
print(gq2b.head(3).to_markdown())
gq2b

# %%
# Part 3
# Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT p.namefirst, p.namelast, SUM(b.h) as hits, SUM(b.ab) AS at_bat, SUM(b.h)/SUM(b.ab) AS bat_avg
    FROM people p
    JOIN batting b ON p.playerid = b.playerid
    WHERE b.ab > 100
    GROUP BY p.playerid
    ORDER BY bat_avg DESC
    LIMIT 5
    ;    
   ''')

gq2c = result.dataframe
print(gq2c.head(3).to_markdown())
gq2c

# %%
# Grand Question 3
# 
# Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and its description.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    -- At Bat vs Triples with Runs Scored

    SELECT    f.franchname AS Team
            , t.teamid
            , t.ab AS at_bat
            , t.2b AS doubles
            , t.r AS runs_scored
            , t.2b/t.ab AS doubles_by_at_bat
            , t.r/t.2b AS runs_per_double
    FROM teams t
    JOIN teamsfranchises f ON t.franchid = f.franchid
    WHERE f.active = "Y" AND t.teamid = "ARI" OR t.teamid = "SDN"
    GROUP BY f.franchname
    ORDER BY runs_scored DESC
    ;
   ''')

gq3 = result.dataframe
print(gq3.head(3).to_markdown())
gq3

# %%
# 
# Diamondbacks score more runs from doubles than Padres

# Chart
gq3_chart = (
    alt.Chart(gq3)
    .encode(x="Team", y="runs_per_double")
    .mark_bar()
    .properties(width=400, title="Diaondbacks Score More Runs Than Padres From Doubles")
)


gq3_chart.save('gq3_chart.png')
gq3_chart

# %%
