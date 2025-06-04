import pandas as pd
file_path= r'C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Python projects local\AI_ML\qm7_subset.csv'

df=pd.read_csv(file_path)

print (df.head(7)) # print first seven rows

print (df.columns) # prints all the columns in the dataframe

print (df.info) #gives total number of rows and columns

print (df.describe()) #mean mode and so on..

print (df.iloc[0])