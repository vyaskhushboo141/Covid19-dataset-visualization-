#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import plotly
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


# In[26]:


data=pd.read_csv('covidw19.csv',parse_dates=['ObservationDate'])


# In[27]:


data.head()


# In[28]:


data.columns


# In[6]:


data.tail()


# In[39]:


data.rename(columns={'ObservationDate':'date','Province/State':'state', 'Country/Region':'country',
       'Last Update':'lastupdate', 'Confirmed':'confirmed', 'Deaths':'deaths', 'Recovered':'recovered'},inplace=True)


# In[40]:


data['active']=data['confirmed']-data['deaths']-data['recovered']


# In[9]:


top=data[data['date']==data['date'].max()]
world=top.groupby('country')['confirmed','active','deaths'].sum().reset_index()
world.head()


# In[29]:


figure=px.choropleth(world, locations="country",
                locationmode='country names',color="active",
                hover_name="country",range_color=[1,1000],
                title='Countries with active cases')
figure.show()


# In[21]:


top_actives=top.groupby(by='country')['active'].sum().sort_values(ascending=False).head(20).reset_index()


# In[ ]:





# In[33]:


plt.figure(figsize=(15,10))
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel("Dates",fontsize=30)
plt.ylabel('country',fontsize=30)
plt.title("top 20 contries having most active cases", fontsize=30)
ax=sns.barplot(x=top_actives.active, y=top_actives.country)
for i,(value,name) in enumerate(zip(top_actives.active, top_actives.country)):
    ax.text(value, i-.05,f'{value:,.0f}',size=10,ha='left',va='center')
    
ax.set(xlabel='total cases',ylabel='country')


# In[34]:


top_deaths=top.groupby(by='country')['deaths'].sum().sort_values(ascending=False).head(20).reset_index()


# In[35]:


plt.figure(figsize=(15,10))
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel("Dates",fontsize=30)
plt.ylabel('country',fontsize=30)
plt.title("top 20 contries having most death cases", fontsize=30)
ax=sns.barplot(x=top_deaths.deaths, y=top_deaths.country)
for i,(value,name) in enumerate(zip(top_deaths.deaths, top_deaths.country)):
    ax.text(value, i-.05,f'{value:,.0f}',size=10,ha='left',va='center')
    
ax.set(xlabel='total cases',ylabel='country')


# In[36]:


top_recovered=top.groupby(by='country')['recovered'].sum().sort_values(ascending=False).head(20).reset_index()


# In[37]:


plt.figure(figsize=(15,10))
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel("Dates",fontsize=30)
plt.ylabel('country',fontsize=30)
plt.title("top 20 contries having most recovered cases", fontsize=30)
ax=sns.barplot(x=top_recovered.recovered, y=top_recovered.country)
for i,(value,name) in enumerate(zip(top_recovered.recovered, top_recovered.country)):
    ax.text(value, i-.05,f'{value:,.0f}',size=10,ha='left',va='center')
    
ax.set(xlabel='total cases',ylabel='country')


# In[42]:


us=data[data.country=='US']
us=us.groupby(by='date')['recovered','deaths','confirmed','active'].sum().reset_index()


# In[43]:


uk=data[data.country=='UK']
uk=uk.groupby(by='date')['recovered','deaths','confirmed','active'].sum().reset_index()
uk=uk.iloc[33:].reset_index().drop('index',axis=1)


# In[44]:


India=data[data.country=='India']
India=India.groupby(by='date')['recovered','deaths','confirmed','active'].sum().reset_index()
India=India.iloc[9:].reset_index().drop('index',axis=1)


# In[45]:


Brazil=data[data.country=='Brazil']
Brazil=Brazil.groupby(by='date')['recovered','deaths','confirmed','active'].sum().reset_index()
Brazil=Brazil.iloc[8:].reset_index().drop('index',axis=1)


# In[47]:


plt.figure(figsize=(15,10))

sns.pointplot(us.index,us.confirmed,color="Red")
sns.pointplot(uk.index,uk.confirmed,color="Blue")
sns.pointplot(India.index,India.confirmed,color="Green")
sns.pointplot(Brazil.index,Brazil.confirmed,color="Black")

plt.title('confirmed cases over time',fontsize=25)
plt.ylabel('confirmed cases',fontsize=15)
plt.xlabel('No. of Days',fontsize=15)
plt.show()


# In[48]:


plt.figure(figsize=(15,10))

sns.pointplot(us.index,us.deaths,color="Red")
sns.pointplot(uk.index,uk.deaths,color="Blue")
sns.pointplot(India.index,India.deaths,color="Green")
sns.pointplot(Brazil.index,Brazil.deaths,color="Black")

plt.title('deaths cases over time',fontsize=25)
plt.ylabel('deaths cases',fontsize=15)
plt.xlabel('No. of Days',fontsize=15)
plt.show()


# In[49]:


plt.figure(figsize=(15,10))

sns.pointplot(us.index,us.recovered,color="Red")
sns.pointplot(uk.index,uk.recovered,color="Blue")
sns.pointplot(India.index,India.recovered,color="Green")
sns.pointplot(Brazil.index,Brazil.recovered,color="Black")

plt.title('recovered cases over time',fontsize=25)
plt.ylabel('recoveredcases',fontsize=15)
plt.xlabel('No. of Days',fontsize=15)
plt.show()


# In[ ]:




