import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

os. chdir(r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 3\Datasets")
data_csv1=pd.read_csv('Toyota_cleaned_final.csv')



missing=data_csv1[data_csv1.isna().any(axis=1)]


data_csv1['Age'] = data_csv1['Age'].fillna(data_csv1['Age'].mean())
data_csv1['KM'] = data_csv1['KM'].fillna(data_csv1['KM'].median())
data_csv1['HP'] = data_csv1['HP'].fillna(data_csv1['HP'].mean())
data_csv1['FuelType']=data_csv1['FuelType'].fillna(data_csv1['FuelType'].value_counts().index[0])
data_csv1['MetColor'] = data_csv1['MetColor'].fillna(data_csv1['MetColor'].mode()[0])

data_csv1=data_csv1.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))

#print(data_csv1)
#print(data_csv1.isnull().sum(axis=0))
#print (data_csv1.describe().T)
#pd.crosstab(index=data_csv1['Automatic'], columns=data_csv1['FuelType'],normalize='columns' ,dropna=True, margins=True)
#correlation_matrix= data_csv1.corr(method='pearson',numeric_only=True)
#print(correlation_matrix)
#plt.figure(figsize=(10, 8))
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.3f')

#plt.title('Correlation Matrix Heatmap', fontsize=16)

#plt.show()


#plt.scatter(data_csv1['Age'],data_csv1['Price'], c='red')
#plt.title('Scatter plot of Price vs Age')
#plt.xlabel('Age(months)')
#plt.ylabel('Price (Euros)')
#plt.show()

#plt.hist(data_csv1['KM'], color= 'green', edgecolor='white', bins=5)
#plt.xlabel('Kilometer')
#plt.ylabel('Frequency')
#plt.show()

counts=[979, 120, 12]
fuektypes=('Pet','Dis','CNG')
index= np.arange(len(fuektypes))

#plt.bar(index,counts,color=['red','blue','cyan'])
#plt.xticks(index, fuektypes, rotation= 90)
#plt.xlabel('xlabel')
#plt.ylabel('ylabel')
#plt.show()

sns.set(style="darkgrid")
sns.lmplot(x='Age', y='Price', data=data_csv1, fit_reg=False, hue='FuelType', legend=True, palette="Set1")
plt.show()

sns.displot(data_csv1['Age'],bins=20)
plt.show()

sns.countplot(x="FuelType", data=data_csv1, hue= "Automatic")
plt.show()

sns.boxplot(y=data_csv1["Price"], x=data_csv1["FuelType"], hue=data_csv1['Automatic'])
plt.show()

f, (ax_box, ax_hist) = plt.subplots(2, gridspec_kw={"height_ratios": (.50, .50)})
sns.histplot(data_csv1['Age'],bins=20, ax=ax_box)
sns.boxplot(y=data_csv1["Price"], x=data_csv1["FuelType"], hue=data_csv1['Automatic'], ax=ax_hist)
plt.show()

sns.pairplot(data_csv1, kind="scatter", hue="FuelType")
plt.show()