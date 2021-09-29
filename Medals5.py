#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as pg
import plotly
import matplotlib
import requests
import xlrd
import streamlit as st
import openpyxl


# In[2]:


print('pandas == ' + str(pd.__version__))
print('numpy == ' + str(np.__version__))
print('seaborn == ' + str(sns.__version__))
print('plotly == ' + str(plotly.__version__))
print('matplotlib == ' + str(matplotlib.__version__))
print('requests == ' + str(requests.__version__))
print('xlrd == ' + str(xlrd.__version__))
print('openpyxl == ' + str(openpyxl.__version__))


# In[3]:


# df=requests.get()
Medals=pd.read_excel('Medals.xlsx') #Carlos


# In[4]:


print(Medals.info())
Medals.head()


# In[5]:


import plotly.graph_objects as go


# In[24]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
color_scheme={'Gold': '#FFD700', 'Silver': '#c0c0c0','Bronze': '#cd7f32'}

plot= pg.Figure(data=[go.Bar(
    name='Gold', x=Medals['Team'], y=Medals['Gold'], marker_color='#FFD700'
),
    go.Bar(
    name='Silver', x=Medals['Team'], y=Medals['Silver'], marker_color='#c0c0c0'
),
    go.Bar(
    name='Bronze', x=Medals['Team'], y=Medals['Bronze'], marker_color= '#cd7f32'
    ),
])
plot.update_layout(
    updatemenus=[
        dict(
            direction="down", x=-0.1,
            buttons=list([
                dict(label="Total medals",
                     method="restyle",
                     args=[{"visible": [True, True, True]},
                           {"title": "Both"}]),
                dict(label="Gold",
                     method="restyle",
                     args=[{"visible": [True, False, False]},
                           {"title": "Gold",
                            }]),
                dict(label="Silver",
                     method="restyle",
                     args=[{"visible": [False, True, False]},
                           {"title": "Silver",
                            }]),
                dict(label="Bronze",
                     method="restyle",
                     args=[{"visible": [False, False, True]},
                           {"title": "Bronze",
                            }]),]))])
plot.update_layout(
    title='Medals per Country', title_x=0.5,
    xaxis=dict(
        title='Country',
        titlefont_size=16,
        tickfont_size=10),
    yaxis=dict(
        title='Amount of medals',
        titlefont_size=16,
        tickfont_size=10),
    legend=dict(
        x=0.82,
        y=0.95,
        bgcolor='rgba(0, 0, 0, 0)',
        bordercolor='rgba(0, 0, 0, 0)'
    ),
    barmode='stack',
    bargap=0.15,
    bargroupgap=0.07
)
plot.show
st.plotly_chart(plot.show())


# In[20]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
color_scheme={'Gold': '#FFD700', 'Silver': '#c0c0c0','Bronze': '#cd7f32'}
plot2=px.bar(Medals, x='Team', y=['Gold', 'Silver', 'Bronze'], hover_data=['Total'],
            labels={'value':'Amount of medals', 'variable':'Medal', 'Total':'Total medals'}, barmode='stack', 
       color_discrete_map=color_scheme)
st.bar_chart(plot2.show())


# In[8]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
fig= go.Figure()
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Gold'], name='Golden Medals', marker_color='#FFD700'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Silver'], name='Silver Medals', marker_color='#c0c0c0'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Bronze'], name='Bronze Medals', marker_color= '#cd7f32'))

fig.update_layout(
    title='Medals per Country', title_x=0.5,
    xaxis=dict(
        title='Country',
        titlefont_size=16,
        tickfont_size=10),
    yaxis=dict(
        title='Amount of medals',
        titlefont_size=16,
        tickfont_size=10),
    legend=dict(
        x=0.82,
        y=0.95,
        bgcolor='rgba(0, 0, 0, 0)',
        bordercolor='rgba(0, 0, 0, 0)'
    ),
    barmode='stack',
    bargap=0.15,
    bargroupgap=0.07
)
fig.show()


# In[9]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Gold']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Gold Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Gold Medals across Nations", size=20)
plt.show()


# In[10]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Silver']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='black',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Silver Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Silver Medals across Nations", size=20)
plt.show()


# In[11]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Bronze']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Bronze Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Bronze Medals across Nations", size=20)
plt.show()


# In[12]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Total']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Total Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Total Medals across Nations", size=20)
plt.show()

