import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

os. chdir(r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 4\Week - 4_Datasets_for_Data_Preparation")

AD=pd.read_csv('acDetails.txt', delimiter="\t", index_col=0)
DD=pd.read_csv('demoDetails.csv', index_col=0)
SD=pd.read_csv('serviceDetails.csv', index_col=0)

#Primary checks for duplicity i.e we should have ha 251 unique elements
print(len(np.unique(DD['customerID'])))
print(len(np.unique(AD['customerID'])))
print(len(np.unique(SD['customerID'])))

#But we find only 250 unique elements. So we have duplicates.

#Checking if there are any duplicate records
#DD.duplicated(subset=['customerID'], keep=False)<<--->> creats boolean mask
DD[DD.duplicated(subset=['customerID'], keep=False)]  #keep=first  or keep=last
AD[AD.duplicated(subset=['customerID'], keep=False)]
SD[SD.duplicated(subset=['customerID'], keep=False)]

#===========================================Removing duplicate records==============================================

dDD=DD.drop_duplicates()
dAD=AD.drop_duplicates()
dSD=SD.drop_duplicates()   #(subset=['column1', 'column2']) > remove duplicates based on these columns

#Keeps the first occurance of the duplicate and subsequent occurrence have been removed.

#2 Is the customer ID same accross all files?

dAD.customerID.equals(dDD.customerID)
dDD.customerID.equals(dSD.customerID)
dSD.customerID.equals(dAD.customerID)

#3 Merging df
churn= pd.merge(dDD, dAD, on=['customerID'])
churn= pd.merge(churn, dSD, on=['customerID'])
churn_1= churn.copy()

churn_1.info()

np.unique(churn_1['tenure'], return_counts=True)
np.unique(churn_1['SeniorCitizen'], return_counts=True)
#Checking frequencies of each categories in a variable
categorical_data= churn_1.select_dtypes(include=['object']).copy()
categorical_data.columns
categorical_data['gender'].value_counts()  # gives you the frequesncies of unique values in col. gender

#To view this for all the columns, we use a lambda function...(!! value _counts can only used on a series. not a data frame!!)
categorical_data=categorical_data.drop(['customerID','tenure'], axis=1)
freq=categorical_data.apply(lambda x:x.value_counts()).T.stack()
 
#Replacing 'Four' and and 'One' in 'tenure'

churn_1['tenure']=churn_1['tenure'].replace('Four',4)
churn_1['tenure']=churn_1['tenure'].replace('One',1)
churn_1['tenure']=churn_1['tenure'].astype(int)
np.unique(churn_1['tenure'], return_counts=True)

#Cleaning 'dependents' column

pd.crosstab(index=churn_1['Dependents'], columns="counts")

churn_1['Dependents']=churn_1['Dependents'].replace('1@#','No')

##########################################Checking for logical inconsistencies###############################

# Checking if 'customer ID' is consistent
"""
1. Total number of characters
2. Sequence of chara. 
"""

#1 Any Id chara != 10?

#print(churn_1['customerID'])

len_ind= [i for i,value in enumerate(churn_1['customerID']) if len(value)!=10]

import re
pattern= '^[0-9]{4,4}-[A-Z]{5,5}'
p=re.compile(pattern)

q= [i for i,values in enumerate(churn_1['customerID']) if p.match(str(values))==None]

#found that other patterns are also being used 

fp1= re.compile(r'^[A-Z]{5,5}-[0-9]{4,4}$')
fp2= re.compile(r'^[0-9]{4,4}/[A-Z]{5,5}$')
fp3= re.compile(r'^([0-9]{4,4})([A-Z]{5,5})$')


for i in q:
    false_str=str(churn_1.loc[i, 'customerID'])
    if (fp1.match(false_str)):
        str_splits=false_str.split('-')
        churn_1.loc[i, 'customerID']=str_splits[1]+'-'+str_splits[0]
    elif (fp2.match(false_str)):
        churn_1.loc[i, 'customerID']=false_str.replace('/','-')
        
#Logical checks - check for fallacies in the data
#If Internet service = No, then all the allied services related to internet should be No!

#We subset them
y= churn_1[(churn_1['InternetService']=='No')]
z= y.iloc[:,13:20]

''' Logic- If there are say 2 or more Yes in the allied services, then go back and change Internet service= Yes, Else chnge the allied services to No''' 

for i,row in z.iterrows():
    yes_cnt=row.str.count('Yes').sum()
    if yes_cnt>=2:
        z.loc[i,'InternetService']='Yes'
    else:
        z.loc[i,:]='No internet service'







