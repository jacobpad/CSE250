# %%
import datadotworld as dw
import pandas as pd
import altair as alt

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
gq2b

# %%
# Part 3
# Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.

result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    playerid
    , SUM(h) as hits
    , SUM(ab) as at_bats
    , h/ab AS batting_average
    FROM batting
    WHERE ab > 100
    GROUP BY playerid
    ORDER BY batting_average DESC
    LIMIT 5
    ; 
    
    # SELECT  playerid, 
    #     h AS hits, 
    #     ab AS at_bat, 
    #     h/ab AS batting_average
    # FROM batting
    # WHERE ab > 300
    # GROUP BY playerid
    # ORDER BY batting_average DESC
    # -- ORDER BY at_bat DESC
    # LIMIT 5;


    
       ''')

gq2b = result.dataframe
gq2b

