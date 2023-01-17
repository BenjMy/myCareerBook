#!/usr/bin/env python
# coding: utf-8

# ### Network graph 
# https://plotly.com/python/network-graphs/
# 
# ### Sankey diagrams
# https://borealperspectives.org/2013/11/10/sankey-diagrams-bad-charts-and-science-careers/
# http://bl.ocks.org/drarnakarick/967acc51cc5e7842fd7c4dc67f21f859
# 
# ### Other metrics
# - Altmetrics
# - ???
# 
# ### scholarly API
# - pip install scholarly

# In[9]:


# read csv file
import pandas as pd
pd.options.plotting.backend = "plotly"

articles_zenodo = pd.read_excel('RyC_articles.xlsx',sheet_name=1)
articles_zenodo.head()


# In[10]:


#from rpy2.robjects.packages import importr
from scholarly import scholarly

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Benjamin Mary')
#search_query = scholarly.search_author('Benjamin Mary, Padova')


# In[ ]:


# Retrieve the first result from the iterator
first_author_result = next(search_query)
scholarly.pprint(first_author_result)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result)
#scholarly.pprint(author)


first_author_result

citedby


# In[ ]:





# In[2]:


import matplotlib as mpl
pd.options.plotting.backend = "matplotlib"
mpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2
mpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2


# In[3]:


pd_citations = pd.DataFrame(author['cites_per_year'], index=[0])
pd_cit_t = pd_citations.transpose()




fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes([0, 0, 1, 1])
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', right='on')
ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', right='on')
pd_cit_t[:-1].plot(ax=ax,linewidth=2, color='k',legend=None)
ax.set_xlabel('year')
ax.set_ylabel('cites per year')
plt.annotate('total:' + str(author['citedby']), xy=(0.65, 0.85), xycoords='axes fraction')



ax.set_ylabel('cites per year per article')

pd_cit_t


# In[4]:


publications = author['publications']

pub_year = []
for key in publications:   
    try:
        print(key['bib']['pub_year'])
        pub_year.append(int(key['bib']['pub_year']))
    except:
        pass

pub_year


# In[4]:


# Take a closer look at the first publication
first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
#scholarly.pprint(first_publication_filled)


# In[5]:


# Print the titles of the author's publications
#publication_titles = [pub['bib']['title'] for pub in author['publications']]
#print(publication_titles)


# In[6]:


# Which papers cited that publication?
#citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
#print(citations)


# In[7]:


field_activity.sort_values(by='Publication Year', ascending=True, inplace=True)
field_activity

nb_publi_year = field_activity['Publication Year'].value_counts()

field_activity.groupby('Item Type')

mean_impact_factor = []
nb_of_citations = []
nb_of_citations_year = []

# period of 2020/2021
# ------------------
Soil_IF = 3.3
PS_IF = 3.299 
VZJ_IF = 3.289
SciRep_IF = 4.379


# In[ ]:



field_activity['Nb_year'] = nb_publi_year

field_activity



fig = nb_publi_year.sort_index().plot(x="Year", y="Nb",legend=[], color="species",
                title="Automatic Labels Based on Data Frame Column Names")
fig.show()


nb_publi_year


# In[ ]:


from rpy2.robjects.packages import importr
utils = importr('scholar')

