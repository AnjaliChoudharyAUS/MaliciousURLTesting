#!/usr/bin/env python
# coding: utf-8

# In[26]:



import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
data = pd.read_csv('Dataset1.csv')

# View first and last 5 observations
print(data.head())
print(data.tail())


# In[27]:


print(data.describe())


# In[18]:


print(data.info()) 


# In[29]:


data ['Result'].value_counts()


# In[ ]:





# In[ ]:





# In[30]:


plt.figure(figsize =(8,8))
plt.hist(data.Type)           


# In[13]:


print(data.isnull().sum())      


# In[31]:


print(data.corr())

import seaborn as sns
plt.figure(figsize =(8,8))
sns.heatmap(data.corr())


# In[22]:


print(data.corr()['Result'].sort_values()) 


# In[33]:


data.drop(['Favicon','Iframe','Redirect',
                'popUpWidnow','RightClick','Submitting_to_email'],axis=1,inplace=True)
print(len(data.columns))


# In[35]:


y = data['Result'].values
X = data.drop(['Result'], axis = 1)

from sklearn.metrics import accuracy_score,roc_curve,auc, confusion_matrix
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# Split the data as training and testing data - 70% train size, 30% test size
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size = 0.3, random_state = None)


# In[39]:


#1 Classification using Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc = rfc.fit(X_train,y_train)
prediction = rfc.predict(X_test)
print("Accuracy with RF classifier:",accuracy_score(y_test, prediction)) 
fpr,tpr,thresh = roc_curve(y_test,prediction)      
roc_auc = accuracy_score(y_test,prediction)         # Calculate ROC AUC

# Plot ROC curve for Random Forest
plt.plot(fpr,tpr,'g',label = 'Random Forest')
plt.legend("Random Forest", loc='lower right')
plt.legend(loc='lower right')
print("Conf matrix RF classifier:",confusion_matrix(y_test,prediction)) 
# Plot ROC curve for Random Forest
plt.plot(fpr,tpr,'g',label = 'Random Forest')
plt.legend("Random Forest", loc='lower right')
plt.legend(loc='lower right')
print("Conf matrix RF classifier:",confusion_matrix(y_test,prediction))  #  Generate confusion matrix

#2 Classification using logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg = logreg.fit(X_train,y_train)
prediction = logreg.predict(X_test)
print("Accuracy with Log Reg:", accuracy_score(y_test, prediction))
print ("Conf matrix Log Reg:",confusion_matrix(y_test,prediction))
fpr,tpr,thresh = roc_curve(y_test,prediction)
roc_auc = accuracy_score(y_test,prediction)
# Plot ROC curve for Logistic Regression
plt.plot(fpr,tpr,'orange',label = 'Logistic Regression')
plt.legend("Logistic Regression", loc='lower right')
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.legend(loc='lower right')
# Classification using SVM
from sklearn.svm import SVC
svc_l = SVC(kernel = "linear", C = 0.025)
svc_l = svc_l.fit(X_train,y_train)
prediction = svc_l.predict(X_test)
print("Accuracy with SVM-Linear:",accuracy_score(y_test, prediction))
fpr,tpr,thresh = roc_curve(y_test,prediction)
roc_auc = accuracy_score(y_test,prediction)

# Plot ROC curve for SVM-linear
plt.plot(fpr,tpr,'b',label = 'SVM')
plt.legend("SVM", loc ='lower right')
plt.legend(loc ='lower right')
print("Conf matrix SVM-linear:",confusion_matrix(y_test,prediction))

plt.show()
from sklearn.feature_selection import RFE
rfe = RFE(rfc,27)                              
rfe = rfe.fit(X_train, y_train)               # Train RF classifier with only 27 features now
pred = rfe.predict(X_test)

# Test accuracy on reduced data
print("Accuracy by RFClassifier after RFE is applied:", accuracy_score(y_test,pred))

rfe = RFE(svc_l,27)
rfe = rfe.fit(X_train, y_train)               # Train SVM with only 27 features now
pred = rfe.predict(X_test)
print("Accuracy by SVM-Linear after RFE is applied:", accuracy_score(y_test,pred))

rfe = RFE(logreg,27)
rfe = rfe.fit(X_train, y_train)              # Train Logistic-Reg with only 27 features now
pred = rfe.predict(X_test)
print("Accuracy by Logistic Regression after RFE is applied:", accuracy_score(y_test,pred))


# In[ ]:




