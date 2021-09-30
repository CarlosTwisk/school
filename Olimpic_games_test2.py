#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as pg
import plotly
import matplotlib
import requests
import xlrd
import streamlit as st
import openpyxl
import plotly.graph_objects as go


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


st.title('Olympic games 2021')
# st.write('In this dashboard we are going to show data about the 2021 Olympic games and about the Olympic games in the past 120 years.')
# st.write('The data used for this analysis is imported from Kaggle.')
# st.write('First al the packeges and files were imported to python.')
# st.write('During the data analysis we found out that the Coaches dataset contained 150 NA values, these values were not removed because of the removal of the other important data.')
# st.write('Now the visualisations will be shown.')


# In[4]:


st.header('Medals olympic games 2021')


# # Medals

# In[5]:


Athletes=pd.read_excel('Athletes.xlsx') # Joost
Coaches=pd.read_excel('Coaches.xlsx') #Priscilla
Gender=pd.read_excel('EntriesGender.xlsx')
Medals=pd.read_excel('Medals.xlsx') #Carlos


# In[6]:


st.dataframe(Medals)


# In[7]:


Medals.info()
Medals.head()


# In[8]:


st.subheader('Making a visual bar chart about the different countries and there medals')


# In[9]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
color_scheme={'Gold': '#FFD700', 'Silver': '#c0c0c0','Bronze': '#cd7f32'}

# st.write(
# st.code(
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
plot.show()
st.plotly_chart(plot)


# # Coaches

# In[10]:


st.header('Coaches olimpic games')


# In[11]:


st.subheader('Making a histogram with sliders about the coaches')


# In[12]:


# Histogram van olympische coaches
fig = px.histogram(Coaches, x="Discipline", color="NOC",
animation_frame='NOC', title='What type of Olympic coaches there are in each country'
                  , labels= {'NOC':'Country'})
fig.update_layout(height=700, width=800)
fig.show()
st.plotly_chart(fig)


# In[13]:


st.subheader('Barplot of the genders of the 2021 olympics')


# In[14]:


# barplot van olympische spelen genders 
fig3=px.bar(Gender, x='Discipline', y=['Female', 'Male'], hover_data=['Total'], 
      labels={'value':'Total Gender', 'variable':'Gender', 'Total':'Totaal'}, barmode='stack', title= '2021 Tokyo olimpics' 
       )
st.plotly_chart(fig3)

