#!/usr/bin/env python
# coding: utf-8

# # Pivoting Data in SQL
# 
# ## Setup
# 
# 1. Start by installing MySQL from here: https://dev.mysql.com/downloads/
# 2. Follow the instructions from [here](https://ladvien.com/data-analytics-mysql-localhost-setup/) to setup MySQL on your local machine.
# 3. Install MySQL Workbench from here: https://dev.mysql.com/downloads/workbench/
# 4. Download dataset used in this lecture from here: https://github.com/ardhiraka/PFDS_sources/blob/master/players.csv and https://github.com/ardhiraka/PFDS_sources/blob/master/teams.csv
# 

# Let's start by aggregating the data to show the number of players of each year in each conference, similar to the first example in the inner join lesson:
# 
# ```sql
# SELECT teams.conference AS conference,
#        players.year,
#        COUNT(1) AS players
#   FROM hacktiv8.players players
#   JOIN hacktiv8.teams teams
#     ON teams.school_name = players.school_name
#  GROUP BY 1,2
#  ORDER BY 1,2
# ```
# 
# In order to transform the data, we'll need to put the above query into a subquery. It can be helpful to create the subquery and select all columns from it before starting to make transformations. Re-running the query at incremental steps like this makes it easier to debug if your query doesn't run. Note that you can eliminate the ORDER BY clause from the subquery since we'll reorder the results in the outer query.
# 
# ```sql
# SELECT *
#   FROM (
#         SELECT teams.conference AS conference,
#                players.year,
#                COUNT(1) AS players
#             FROM hacktiv8.players players
# 			JOIN hacktiv8.teams teams
#             ON teams.school_name = players.school_name
#          GROUP BY 1,2
#        ) sub
# ```
# 
# Assuming that works as planned (results should look exactly the same as the first query), it's time to break the results out into different columns for various years. Each item in the SELECT statement creates a column, so you'll have to create a separate column for each year:
# 
# ```sql
# SELECT conference,
#        SUM(CASE WHEN year = 'FR' THEN players ELSE NULL END) AS fr,
#        SUM(CASE WHEN year = 'SO' THEN players ELSE NULL END) AS so,
#        SUM(CASE WHEN year = 'JR' THEN players ELSE NULL END) AS jr,
#        SUM(CASE WHEN year = 'SR' THEN players ELSE NULL END) AS sr
#   FROM (
#         SELECT teams.conference AS conference,
#                players.year,
#                COUNT(1) AS players
#           FROM hacktiv8.players players
#           JOIN hacktiv8.teams teams
#             ON teams.school_name = players.school_name
#          GROUP BY 1,2
#        ) sub
#  GROUP BY 1
#  ORDER BY 1
#  ```
# 
# But this could still be made a little better. You'll notice that the above query produces a list that is ordered alphabetically by Conference. It might make more sense to add a "total players" column and order by that (largest to smallest):
# 
# ```sql
# SELECT conference,
#        SUM(players) AS total_players,
#        SUM(CASE WHEN year = 'FR' THEN players ELSE NULL END) AS fr,
#        SUM(CASE WHEN year = 'SO' THEN players ELSE NULL END) AS so,
#        SUM(CASE WHEN year = 'JR' THEN players ELSE NULL END) AS jr,
#        SUM(CASE WHEN year = 'SR' THEN players ELSE NULL END) AS sr
#   FROM (
#         SELECT teams.conference AS conference,
#                players.year,
#                COUNT(1) AS players
#           FROM hacktiv8.players players
#           JOIN hacktiv8.teams teams
#             ON teams.school_name = players.school_name
#          GROUP BY 1,2
#        ) sub
#  GROUP BY 1
#  ORDER BY 2 DESC
# ```
# 
# 
