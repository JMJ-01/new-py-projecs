import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option ('display.max_columns',None)
os. chdir(r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 4\Assignment - 04-20250802")
 
date_format = '%d-%b-%y' 

df_csv=pd.read_csv('Stock_File_1.csv')
df_txt=pd.read_csv('Stock_File_2.txt')

df_csv['Date'] = pd.to_datetime(df_csv['Date'], format=date_format)
df_txt['Date'] = pd.to_datetime(df_txt['Date'], format=date_format)

df_csv.set_index('Date', inplace=True)
df_txt.set_index('Date', inplace=True)


df_merged= pd.concat([df_csv,df_txt], ignore_index=False)

df_merged.columns
