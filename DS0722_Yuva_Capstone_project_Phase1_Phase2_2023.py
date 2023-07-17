#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Phase1 DATA collection
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Read the State geographical data from a CSV file.Data source google wkipedia data on 2011 census.
Population = pd.read_csv('population.csv')
Population.shape


# In[3]:


Population.drop(index=35,inplace=True)
Population


# In[6]:


#Phase 2 State/UT wise data analysis


import pandas as pd

# Read the crime data from a CSV file
crime_data = pd.read_csv('01_District_wise_crimes_committed_IPC_2001_2012.csv')


# In[25]:


# crime_data.isnull().sum() there is no any null value found in given data. We have selected following column from for our data analysis


# In[7]:


new_crime_data=crime_data[['STATE/UT','DISTRICT','YEAR','MURDER','RAPE','KIDNAPPING & ABDUCTION','ROBBERY','DOWRY DEATHS','RIOTS']]


# In[8]:


new_crime_data


# In[ ]:



# Group the data by state and sum the crime counts
#statewise_crime_murder = new_crime_data.groupby('STATE/UT')['MURDER'].sum()

# Calculate the crime rate per state
#population_data = {
#    'State': ['State1', 'State2', 'State3'],  # Replace with actual state names
#    'Population': [1000000, 2000000, 3000000]  # Replace with actual population data
#}
#population_df = pd.DataFrame(population_data)
#statewise_crime_rate = statewise_crime / population_df['Population'] * 1000  # Calculate crime rate per 1000 population

# Print the statewise crime rate
#print(statewise_crime_rate)


# In[8]:


# Group the data by state and sum the crime counts
statewise_crime_murder = new_crime_data.groupby('STATE/UT')['MURDER'].sum()


# In[9]:


# Group the data by state and sum the crime counts
statewise_crime_robbery = new_crime_data.groupby('STATE/UT')['ROBBERY'].sum()


# In[10]:


# Group the data by state and sum the crime counts
statewise_crime_rape = new_crime_data.groupby('STATE/UT')['RAPE'].sum()


# In[11]:


# Group the data by state and sum the crime counts
statewise_crime_kidnap = new_crime_data.groupby('STATE/UT')['KIDNAPPING & ABDUCTION'].sum()


# In[12]:


# Group the data by state and sum the crime counts
statewise_crime_dowery = new_crime_data.groupby('STATE/UT')['DOWRY DEATHS'].sum()


# In[13]:


# Group the data by state and sum the crime counts
statewise_crime_riots = new_crime_data.groupby('STATE/UT')['RIOTS'].sum()


# In[14]:


Horz_concat=pd.concat([statewise_crime_murder,statewise_crime_rape,statewise_crime_kidnap,statewise_crime_dowery,statewise_crime_robbery,statewise_crime_riots],axis=1)
Horz_concat


# In[15]:


total_crime=Horz_concat.sum(axis=1)
df=pd.DataFrame(total_crime)

Population['crime']=total_crime
df.shape
df


# In[17]:


df2=pd.DataFrame(Horz_concat)


# In[18]:


list=['A &  N ISLANDS', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR', 'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI UT', 'GOA', 'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA',  'LAKSHADWEEP', 'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU',  'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND', 'WEST BENGAL']
df2['STATE/UT']=list
df2


# In[19]:


Population['STATE/UT']=list


# In[81]:





# In[20]:


#Calculation of total crime statewise
df2['total_crime']=df2['MURDER']+df2['RAPE']+df2['KIDNAPPING & ABDUCTION']+df2['ROBBERY']+df2['DOWRY DEATHS']+df2['RIOTS']
df2


# In[21]:





# Reset the index of the DataFrame
df2.reset_index(inplace=True, drop=True)
Population.reset_index(inplace=True, drop=True)

# Print the updated DataFrame

print(Population)


# In[22]:


# creation of common data by cobining two dataframes 

common_data= df2.merge(Population,on='STATE/UT',how='outer')


# In[23]:


common_data


# In[26]:


#2.1Analysis of Literacy Rate vs Total Crimes.
import matplotlib.pyplot as plt



# Create a scatter plot
plt.scatter(x=common_data['Literacy rate'], y=common_data['total_crime']);

# Set the labels and title
plt.xlabel('Literacy Rate')
plt.ylabel('Total Crimes')
plt.title('Literacy Rate vs Total Crimes')

# Show the plot
plt.show()



# In[27]:


sns.regplot(x='Literacy rate',y='total_crime',data=common_data);


# In[ ]:


# From above gapph It is seen that yhere is negative correlation between  Literacy vs total_crime as literacy is increases total crime is going on decreasing


# In[25]:


# Group the data by state and sum the crime counts yearwise
year_crime_murder = new_crime_data.groupby('YEAR')['MURDER'].sum()
year_crime_rape = new_crime_data.groupby('YEAR')['RAPE'].sum()
year_crime_kidnap = new_crime_data.groupby('YEAR')['KIDNAPPING & ABDUCTION'].sum()
year_crime_robery = new_crime_data.groupby('YEAR')['ROBBERY'].sum()
year_crime_dowery = new_crime_data.groupby('YEAR')['DOWRY DEATHS'].sum()
year_crime_riots = new_crime_data.groupby('YEAR')['RIOTS'].sum()


# In[26]:


year_concat=pd.concat([year_crime_murder,year_crime_rape,year_crime_kidnap,year_crime_robery,year_crime_dowery,year_crime_riots],axis=1)
df3=pd.DataFrame(year_concat)
df3['YEAR']=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
df3.reset_index(inplace=True, drop=True)
df3


# In[146]:


df3.to_csv('year_data.csv', index=False)


# In[33]:


y=df3['YEAR']
x=df3.drop(columns = ['YEAR'])


# In[35]:


#2.3	Analysis of year-on-year total crime rate.

plt.figure(figsize = (15,10),facecolor ='yellow')
plotnumber =1
for column in x:
    if plotnumber <=6:
        ax = plt.subplot(2,3,plotnumber)
        plt.scatter(x[column],y)
        plt.xlabel(column,fontsize = 10)
        plt.ylabel('YEAR',fontsize = 10)
        sns.regplot(x[column],y,data=df3);
    plotnumber +=1
plt.tight_layout()


# In[ ]:


#From year on data It is seen among all other features only muder vs year show negative correlation.All other features rape, kidnapping , robbery , dowery & riots show positive correlation with respect to time.


# In[29]:



2.4	 Analysis of area vs overall crime



# In[32]:


Y=common_data['total_crime']
X=common_data ['Area _km2']
state=common_data['STATE/UT']


# In[49]:


plt.figure(figsize = (30,20),facecolor ='yellow')
plotnumber =1
for row in state:
    if plotnumber <=36:
        ax = plt.subplot(6,6,plotnumber)
        plt.scatter(X,Y)
        plt.xlabel(row ,fontsize = 12)
        plt.ylabel('Total crime',fontsize = 12)
        plt.title('Area vs Total Crimes')
        
    plotnumber +=1
plt.tight_layout()


# In[52]:


#2.5	 Analysis of Population vs overall Crime
X=common_data['total_crime']
Y=common_data ['Rural_population']
state=common_data['STATE/UT']


# In[53]:


plt.figure(figsize = (30,20),facecolor ='yellow')
plotnumber =1
for row in state:
    if plotnumber <=36:
        ax = plt.subplot(6,6,plotnumber)
        plt.scatter(X,Y)
        plt.xlabel(row ,fontsize = 12)
        plt.ylabel('Total crime',fontsize = 12)
        plt.title('Rural population vs Total Crimes')
        
    plotnumber +=1
plt.tight_layout()


# In[ ]:




