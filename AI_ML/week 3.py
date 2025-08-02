import os
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

os. chdir(r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 3\Datasets")

#data_csv=pd.read_csv('Iris_data_sample.csv', index_col=0, na_values=["??","###"])
#data_xlsx=pd.read_excel('Iris_data_sample_x.xlsx', sheet_name='Iris_data', index_col=0, na_values=["??","###"])

data_csv1=pd.read_csv('Toyota.csv', index_col=0, na_values=["????","??"," "])

#samp=data_csv1.copy(deep=False) #simply a copy, changes to this will be reflected n he original data
#cars_data1=data_csv1.copy(deep=True)


#data_csv1.info()

#print (np.unique(cars_data1['Doors']))

data_csv1['Doors'] = data_csv1['Doors'].replace('three', 3)
data_csv1['Doors'] = data_csv1['Doors'].replace('four', 4)
data_csv1['Doors'] = data_csv1['Doors'].replace('five', 5)
data_csv1['Doors'] = data_csv1['Doors'].astype(int)

#print (np.unique(data_csv1['Doors'])) 

#data_csv1.isnull().sum()

data_csv1.insert(10,"Price_Class","")
data_csv1.insert(11,"Age_converted",0)
data_csv1.insert(12,"Kilometers_per_Month",0)
data_csv1.insert(13,"1",0)
data_csv1.insert(14,"2",0)

i=0
while i < len(data_csv1['Price']):
    if data_csv1.loc[i,'Price']<=8550:
        data_csv1.loc[i,'Price_Class']="Low"
    elif data_csv1.loc[i,'Price']>=11950:
        data_csv1.loc[i,'Price_Class']="High"
    else: data_csv1.loc[i,'Price_Class']="Medium"
    i+=1

#data_csv1['Price_Class'].value_counts()
def c_converted (val):
    val_converted=val/12
    return val_converted

data_csv1["Age_converted"]=c_converted(data_csv1["Age"])

def d_converted (val1,val2):
    val_converted=val1/12
    ratio = val2/val1
    return [val_converted,ratio]


data_csv1["1"],data_csv1["2"]= d_converted(data_csv1['Age'], data_csv1['KM'])
print(data_csv1)


###-------------------------------------------------###
# Save the modified DataFrame to a new CSV file
data_csv1.to_csv('Toyota_cleaned_final.csv', index=False)