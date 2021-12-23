#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np 
import pandas as pd 
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt 
from pylab import rcParams 
rcParams['figure.figsize'] = 14,6

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[46]:


AISdata = pd.read_table("11-15Sep_output.txt",sep=";",names=["message","time","sourceId","trackId","aisTrackId","imoNumber","shipName",
                                                      "shipCallsign","shipFlag","destination","eta","latitude","longitude",
                                                      "xVelocity","yVelocity","zVelocity","heightDepth","trackNumber","environment","XX"]
                                                       ,header=0)


# In[ ]:





# In[47]:


AISdata


# In[ ]:





# In[48]:


AISdata.info()


# In[ ]:





# In[50]:


#plot the geographical points 
_ = plt.plot(AISdata['longitude'], AISdata['latitude'],marker='.', linewidth=0, color='#128128')
_ = plt.grid(which='major', color='#cccccc', alpha=0.45)
_ = plt.title('Geoprahical distribution of AIS tracker', family='Arial', fontsize=12)
_ = plt.xlabel('longitude')
_ = plt.ylabel('latitude')
_ = plt.show()


# In[ ]:





# In[51]:


#Prepare data for model 
dbscan_data = AISdata [['longitude','latitude']]
dbscan_data = dbscan_data.values.astype('float32', copy=False)
dbscan_data


# In[ ]:





# In[52]:


#Normalize data 
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
dbscan_data = dbscan_data_scaler.transform(dbscan_data)
dbscan_data


# In[ ]:





# In[53]:


model = DBSCAN(eps = 0.25, min_samples = 20, metric='euclidean').    fit(dbscan_data)
model


# In[ ]:





# In[42]:


model.labels_


# In[ ]:





# In[43]:


#Seperate outliers from clustered data 
outliers_df = AISdata[model.labels_ == -1]
clusters_df = AISdata[model.labels_ != -1]

colors =model.labels_
colors_clusters = colors[colors != -1]
color_outliers = 'black'

#Get info about the cluster 
clusters = Counter(model.labels_)
print(clusters)
print(AISdata[model.labels_ == -1])
print('number of clusters = {}'.format(len(clusters)-1))


# In[ ]:





# In[ ]:





# In[44]:


#Plot cluster and outliers
fig = plt.figure()

ax= fig.add_axes([.1,.1,1,1])

ax.scatter(clusters_df['longitude'], clusters_df['latitude'],
          c = colors_clusters, edgecolors= 'black', s=50)
ax.scatter(outliers_df['longitude'], outliers_df['latitude'],
          c = color_outliers, edgecolors= 'black', s=50)

ax.set_xlabel('longitude', family = 'Arial', fontsize = 9 ) 
ax.set_ylabel('latitude', family = 'Arial', fontsize = 9 ) 

plt.title('Clustering AIS signals by DBSCAN algorithm', family='Arial', fontsize=12)

plt.grid(which = 'major', color = '#cccccc', alpha = 0.45)
plt.show()


# In[ ]:







