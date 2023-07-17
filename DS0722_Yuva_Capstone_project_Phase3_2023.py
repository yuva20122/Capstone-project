#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Phase 3 SQL operation
import sqlite3
db = sqlite3.connect("indian_crime.db")


# In[2]:


cursor = db.cursor()


# In[15]:


# creating a table
cursor.execute("CREATE TABLE dist_crime_women(state_ut TEXT, district TEXT, year INT, rape INT, kidnapping INT, dowery_death INT, assult_women_modesty INT,inssult_women_modesty INT, crul_husb_rela INT, Impo_girl INT)")


# In[16]:


# 3.1 Insertind values into table
with open("42_District_wise_crimes_committed_against_women_2001_2012.csv",'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO dist_crime_women VALUES(?,?,?,?,?,?,?,?,?,?)",row.split(","))
        db.commit()
        no_records +=1
        
        print(no_records,"Records inserted")


# In[22]:


result=cursor.execute("SELECT state_ut,district,year, MAX(rape) AS max_rape, max(kidnapping)AS max_kid  FROM dist_crime_women GROUP BY district ")
for row in result:
    print(row)
#3.2 We can able to find highest number of rapes & Kidnappings that happened in which state, District, and year by running above query


# In[32]:


result=cursor.execute("SELECT state_ut,district,year, MIN(rape) AS min_rape, MIN(kidnapping)AS min_kid  FROM dist_crime_women GROUP BY district ")
for row in result:
    print(row)
#3.3 We can able to find lowest number of rapes & Kidnappings that happened in which state, District, and year by running above query


# In[3]:


# New table created  to store data from file 02_District_wise_crimes_committed_against_ST_2001_2012


# In[36]:


cursor.execute("CREATE TABLE dist_crime_SC(state_ut TEXT, district TEXT, year INT,murder INT, rape INT, kidnapping INT,dacoity INT, robbery INT,arson INT, hurt INT,poa INT, pcr INT, cri_sc INT)")


# In[37]:


#3.4 Inserting values into table
with open("02_01_District_wise_crimes_committed_against_SC_2001_2012.csv",'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO dist_crime_SC VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
        db.commit()
        no_records +=1
        
        


# In[60]:


result=cursor.execute("SELECT district, MAX(dacoity) as max_dacoit, MAX(robbery) as max_robbbry FROM dist_crime_SC GROUP BY district ORDER BY robbery DESC ")
for row in result:
    print(row)


# In[4]:


result=cursor.execute("SELECT district, MIN(murder) as min_murder FROM dist_crime_SC GROUP BY district ORDER BY murder  ")
for row in result:
    print(row)


# In[63]:


#3.7	Write SQL query to find the number of murders in ascending order in district and yearwise.


result=cursor.execute("SELECT year,district, murder  FROM dist_crime_SC GROUP BY district ORDER BY year  ")
for row in result:
    print(row)


# In[3]:


# New table created  to Insert records of STATE/UT, DISTRICT, YEAR, MURDER, ATTEMPT TO MURDER, and RAPE columns only from 01_District_wise_crimes_committed_IPC_2001_2012.csv into a new table


# In[ ]:


# Now we will create a data frame to store the result of our 3.2 sql query


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_sql_query("SELECT state_ut,district,year, MAX(rape) AS max_rape, max(kidnapping)AS max_kid  FROM dist_crime_women GROUP BY district ",db)
df=pd.DataFrame(data,columns=['state_ut','district','year', 'max_rape', 'max_kid'])
print(df)

    


# In[12]:


print(type(data))


# In[8]:


df.shape


# In[10]:


df.isnull().sum()


# In[ ]:





# In[5]:


df_year_count=pd.crosstab(df['district'],df['year'],margins=True)
df_year_count


# In[3]:


result=cursor.execute("SELECT *  FROM district_ipc_crime  ")
for row in result:
    print(row)


# In[5]:


cursor.execute("CREATE TABLE district_ipc_crime (state_ut VARCHAR(255),district VARCHAR(255),year INT,murder INT,attempt_to_murder INT,COLUMN_7 INT,rape INT,COLUMN_8 INT,COLUMN_9 INT,COLUMN_10 INT,COLUMN_11 INT,COLUMN_12 INT,COLUMN_13 INT,COLUMN_14 INT,COLUMN_15 INT,COLUMN_16 INT,COLUMN_17 INT,COLUMN_18 INT,COLUMN_19 INT,COLUMN_20 INT,COLUMN_21 INT,COLUMN_22 INT,COLUMN_23 INT,COLUMN_24 INT,COLUMN_25 INT,COLUMN_26 INT,COLUMN_27 INT,COLUMN_28 INT,COLUMN_29 INT,COLUMN_30 INT,COLUMN_31 INT,COLUMN_32 INT,COLUMN_33 INT)")


# In[10]:


with open("01_District_wise_crimes_committed_IPC_2001_2012.csv",'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO district_ipc_crime VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
        db.commit()
        


# In[4]:


result=cursor.execute("SELECT state_ut,district,year, MAX(murder) AS max_murder  FROM district_ipc_crime GROUP BY district ")
for row in result:
    print(row)


# In[7]:


data1=pd.read_sql_query("SELECT  state_ut,district,year, MAX(murder) AS max_murder  FROM district_ipc_crime GROUP BY district ",db)
df1=pd.DataFrame(data1,columns=['state_ut','district','year', 'max_murder'])
print(df1)


# In[21]:


data2=pd.read_sql_query("SELECT  state_ut,district,year, murder   FROM district_ipc_crime ",db)
df2=pd.DataFrame(data2,columns=['state_ut','district','year', 'murder'])
print(df2)


# In[8]:


import pandas as pd

# We have a dataframe named 'df1' with columns 'State/UT', 'District', 'Murders', and 'Year'

# Group the data by 'State/UT' and 'District' and count the number of unique years
district_counts = df1.groupby(['state_ut', 'district']).year.nunique()
district_counts


# In[9]:


# Group the data by 'State/UT' and 'District' and count the number of unique years
district_counts = df1.groupby(['state_ut', 'district']).year.nunique()
district_counts


# In[11]:



# Filter the districts that appear three or more years

filtered_districts = district_counts[district_counts >= 1]
filtered_districts


# In[ ]:




