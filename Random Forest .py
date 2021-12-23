#!/usr/bin/env python
# coding: utf-8

# In[72]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 


# In[ ]:





# In[ ]:





# In[85]:


AISdata = pd.read_table("11-19Sep_output.txt",sep=";",names=["message","time","sourceId","trackId","aisTrackId","imoNumber","shipName",
                                                      "shipCallsign","shipFlag","destination","eta","latitude","longitude",
                                                      "xVelocity","yVelocity","zVelocity","heightDepth","trackNumber","environment","XX"]
                                                       ,header=0)


# In[ ]:





# In[86]:


AISdata


# In[ ]:





# In[75]:


AISdata.isnull().sum()


# In[87]:


AISdata= AISdata.loc[(AISdata['latitude'] >=40.0200 ) & (AISdata['latitude'] <=40.4300 ) & 
            (AISdata['longitude'] >=26.1800 ) & (AISdata['longitude'] <=26.7500 )]


# In[88]:


AISdata.shape


# In[ ]:





# In[77]:


AISdata.isnull().sum()


# In[ ]:





# In[89]:


AISdata= AISdata.loc[(AISdata['destination'] == 'CANAKKALE' ) 
                     | (AISdata['destination'] == 'GELIBOLU' ) 
                     | (AISdata['destination'] == '1915 CANAKKALE PRJ' )
                     | (AISdata['destination'] == 'DARDANELLES' )
                     | (AISdata['destination'] == 'CANAKKALE PS' )
                     | (AISdata['destination'] == 'CANAKKALE P/S' )]


# In[90]:


AISdata.shape


# In[ ]:





# In[91]:


AISdata.isnull().sum()


# In[ ]:





# In[92]:


AISdata=AISdata.drop(['XX'], axis=1)


# In[ ]:





# In[ ]:





# In[93]:


AISdata


# In[ ]:





# In[ ]:





# In[94]:


AISdata.dropna(subset=['destination'], inplace=True)


# In[ ]:





# In[96]:


y = AISdata["destination"]   
x = AISdata.drop(["message","time","aisTrackId","shipName","shipCallsign","destination","eta",
                                                     "heightDepth","environment"], axis =1 )
x = pd.DataFrame(x)


# In[106]:


x


# In[ ]:





# In[ ]:





# In[102]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.30, random_state= 42)


# In[ ]:





# In[103]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators =100,  random_state= 42)


# In[ ]:





# In[104]:


rf.fit(x_train, y_train)


# In[ ]:





# In[105]:


y_pred = rf.predict(x_test)
accuracy_score(y_test,y_pred)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




