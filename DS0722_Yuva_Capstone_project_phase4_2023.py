#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Read the crime data from a CSV file
crime_data = pd.read_csv('01_District_wise_crimes_committed_IPC_2001_2012.csv')
crime_data.head()


# In[3]:


STATE_IN_INDIA=crime_data['STATE/UT'].unique()
STATE_IN_INDIA=STATE_IN_INDIA[:-4]
STATE_IN_INDIA
# Findinind unique state value from given data


# In[4]:


df=crime_data.drop(['STATE/UT'], axis=1)


# In[5]:


# Calculating total crime rate
df['TOTAL CRIME']=df['MURDER']+df['ATTEMPT TO MURDER']+df['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']+df['RAPE']+df['CUSTODIAL RAPE']+df['OTHER RAPE']+df['KIDNAPPING & ABDUCTION']+df['KIDNAPPING AND ABDUCTION OF OTHERS']+df['DACOITY']+df['ROBBERY']+df['BURGLARY']+df['THEFT']+df['AUTO THEFT']+df['OTHER THEFT']+df['RIOTS']+df['CHEATING']+df['COUNTERFIETING']+df['ARSON']+df['HURT_GREVIOUS HURT']+df['DOWRY DEATHS']+df['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']+df['INSULT TO MODESTY OF WOMEN']+df['CRUELTY BY HUSBAND OR HIS RELATIVES']+df['CAUSING DEATH BY NEGLIGENCE']+df['OTHER IPC CRIMES']


# In[6]:


df


# In[42]:


#Selecting only following features from given data
df1=df[['DISTRICT','YEAR','TOTAL CRIME']]
df1


# In[39]:


#lable encoding for district field
from sklearn.preprocessing import LabelEncoder
lab_enc = LabelEncoder()
lab_enc.fit_transform(df['DISTRICT'])
df1


# In[43]:


from sklearn import preprocessing
lab = preprocessing.LabelEncoder()
lab_enc = LabelEncoder()
df1['DISTRICT'] = lab_enc.fit_transform(df1['DISTRICT'])
df1.head()


# In[44]:



df1


# In[45]:


# Elbow method This metod based on the frelationship between Within Cluster Sum of Squared distances(WCSS or inertia)and number of square
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,4):
    kmeans=KMeans(n_clusters=i,random_state=20)
    kmeans.fit(df1)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,4),wcss)
plt.title ('Elbow method')
plt.xlabel('No of cluster')
plt.ylabel('WCSS')
plt.show()


# In[46]:


#Fitting Kmeans to the data set
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans =kmeans.fit_predict(df1)
print(y_kmeans)


# In[47]:


#Fitting Kmeans to the data set
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit_predict(df1.iloc[:,1:])


# In[17]:


#finding cluster centers
kmeans.cluster_centers_


# In[48]:


#record of number of labels
labels=kmeans.labels_
labels


# In[49]:


#Finding unique value of three different cluster present in given data
import numpy as np
unique,counts=np.unique(kmeans.labels_,return_counts=True)
dict_data=dict(zip(unique,counts))
dict_data

#In sensitive area we have total 8785 records ,moderate sensitive area have 130 records & high sensitive area have 102 records for different years from 2001 to 2012


# In[50]:


df1['cluster']=kmeans.labels_
df1


# In[51]:


kmeans.inertia_


# In[52]:


kmeans.score


# In[53]:


df1['STATE/UT']=crime_data['STATE/UT']
df1


# In[54]:


# Finding cluster for different states in india States Andhra, Kerala,Delhi, MP, Maharashtra ,West bengal, Karanataka & Rajasthan show higher crime rates 
f,ax=plt.subplots(figsize=(24,15))
stats=df1.sort_values(['cluster','STATE/UT'],ascending=True)
sns.set_color_codes('pastel')
sns.barplot(y='STATE/UT',x='TOTAL CRIME',data=stats)
sns.despine(left=True,bottom=True)


# In[56]:


df1['District_name']=crime_data['DISTRICT']


# In[57]:


df2=df[['DISTRICT','YEAR','TOTAL CRIME']]
df2['CLUSTER']=kmeans.labels_
df2


# In[69]:


sensitive_area=df2[df2.CLUSTER==0]
sensitive_area


# In[1]:


#f,ax=plt.subplots(figsize=(24,15))
#stats=df2.sort_values(['CLUSTER','DISTRICT'],ascending=True)
#sns.set_color_codes('pastel')
#sns.barplot(y='DISTRICT',x='TOTAL CRIME',data=stats)
#sns.despine(left=True,bottom=True)


# In[71]:


modrate_sensitive_area=df2[df2.CLUSTER==1]
modrate_sensitive_area


# In[74]:


peacefull_area=df2[df2.CLUSTER==2]
peacefull_area


# In[ ]:


##CRIME ANALYSIS IN INDIA##
    


India is a diverse country with a wide range of crime types occurring across various regions. Some of the most common crimes in India include theft, burglary, robbery, sexual assault, domestic violence, cybercrimes, and drug-related offenses. While crime rates can vary significantly from one state to another, certain factors tend to influence crime in sensitive areas:

1. Socioeconomic Factors: Areas with higher poverty rates and unemployment tend to have higher crime rates. Poverty can lead to desperation, which may push individuals into criminal activities.

2. Education and Awareness: Education plays a crucial role in crime prevention. Areas with higher literacy rates and better access to education often have lower crime rates.

3. Law Enforcement: The effectiveness of law enforcement and the presence of police can impact crime rates. Areas with strong law enforcement tend to have lower crime rates, while areas with weak or corrupt law enforcement may experience higher crime.

4. Social and Cultural Factors: Cultural norms, traditions, and social attitudes can influence crime patterns. In some areas, certain crimes might be more prevalent due to prevailing social norms or attitudes.

5. Drug and Alcohol Abuse: Substance abuse can lead to a higher likelihood of criminal behavior, including violence and property crimes.

6. Urbanization: Rapid urbanization can lead to overcrowding, poverty, and inequality, creating an environment conducive to criminal activities.

Strategies to Reduce Crime:

1. Community Policing: Strengthening community policing initiatives can foster better relationships between law enforcement and the community, leading to improved crime prevention and resolution.

2. Education and Skill Development: Investing in education and skill development programs can help reduce poverty and unemployment, decreasing the motivation for criminal activities.

3. Public Awareness Campaigns: Conducting public awareness campaigns to educate people about the consequences of crime and the importance of reporting crimes can help deter criminal behavior.

4. Rehabilitation Programs: Focusing on rehabilitation and reintegration of offenders into society can reduce the likelihood of re-offending.

5. Enhanced Technology: Utilizing technology to improve surveillance, communication, and crime analysis can help law enforcement agencies respond more effectively to criminal activities.

6. Addressing Social Issues: Addressing issues like drug abuse, domestic violence, and mental health can help reduce crime associated with these problems.

Safe and Unsafe Districts:

Determining the safest and most unsafe districts in India can be challenging due to the dynamic nature of crime patterns. Crime rates can change over time, and various factors influence safety levels. It is essential to refer to the latest data from reliable sources, such as government crime statistics and crime mapping websites, to identify current trends.

In conclusion, reducing crime in India requires a multi-faceted approach involving various stakeholders, including the government, law enforcement agencies, communities, and NGOs. Targeted efforts to address socioeconomic issues, improve education, enhance law enforcement, and promote public awareness can make significant strides in crime prevention and creating safer environments.


# In[ ]:




