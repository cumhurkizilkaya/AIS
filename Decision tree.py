#!/usr/bin/env python
# coding: utf-8

# In[]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 


# In[]:


AISdata = pd.read_table("11-19Sep_output.txt",sep=";",names=["message","time","sourceId","trackId","aisTrackId","imoNumber","shipName",
                                                      "shipCallsign","shipFlag","destination","eta","latitude","longitude",
                                                      "xVelocity","yVelocity","zVelocity","heightDepth","trackNumber","environment","XX"]
                                                       ,header=0)



# In[]:


AISdata




# In[]:


AISdata.isnull().sum()


# In[]:




# In[]:


AISdata= AISdata.loc[(AISdata['latitude'] >=40.0200 ) & (AISdata['latitude'] <=40.4300 ) & 
            (AISdata['longitude'] >=26.1800 ) & (AISdata['longitude'] <=26.7500 )]


# In[ ]:






AISdata



# In[]:


AISdata= AISdata.loc[(AISdata['destination'] == 'CANAKKALE' ) 
                     | (AISdata['destination'] == 'GELIBOLU' ) 
                     | (AISdata['destination'] == '1915 CANAKKALE PRJ' )
                     | (AISdata['destination'] == 'DARDANELLES' )
                     | (AISdata['destination'] == 'CANAKKALE PS' )
                     | (AISdata['destination'] == 'CANAKKALE P/S' )]


# In[]:


AISdata





# In[]:


AISdata= AISdata.loc[:,['destination','sourceId','trackId','imoNumber','shipFlag','latitude','longitude','xVelocity','yVelocity','zVelocity','trackNumber']]




# In[]:


AISdata



# In[]:


AISdata.isnull().sum()


# In[ ]:







y = AISdata["destination"]   
x = AISdata.drop(["destination"], axis =1 )


# In[ ]:





# In[147]:


x_train,x_valid,y_train,y_valid = train_test_split(x,y, random_state= 101, stratify=y,test_size=0.30)





# In[148]:


y_train.value_counts(normalize=True)




# In[]:


y_valid.value_counts(normalize=True)


# In[ ]:



x_train.shape, y_train.shape


# In[ ]:




x_valid.shape,y_valid.shape




# In[]:


from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree import DecisionTreeRegressor


# In[ ]:






dt_model = DecisionTreeClassifier(random_state=10)


# In[ ]:




dt_model.fit(x_train,y_train)


# In[ ]:





dt_model.score(x_train,y_train)


# In[ ]:






dt_model.score(x_valid,y_valid)


# In[ ]:





dt_model.predict(x_valid)


# In[]:


dt_model.predict_proba(x_valid)


# In[ ]:





y_pred = dt_model.predict_proba(x_valid)[:,1]


# In[]:


new_y =[]
for i in range(len(y_pred)):
    if y_pred[i]<0.6:
        new_y.append(0)
    else:
        new_y.append(1)



from sklearn.metrics import accuracy_score


# In[]:


accuracy_score(y_valid,new_y)






