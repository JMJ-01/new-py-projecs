import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats
from scipy.stats import ttest_1samp 


pd.set_option('display.max_columns', None)
os. chdir(r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 5\DatasetData_Description-20250812")
cars_data= pd.read_csv('cars_sampled.csv')
cars=cars_data.copy()
"""-------------------------------------------------------------------------------------------"""
#plt.rcParams["figure.figsize"]=(7,7)
#v1=scipy.stats.norm.rvs(loc=0, scale=1, size=1000)
#print('Mean', v1.mean())
#print('Std Dev', v1.std())

#scipy.stats.norm.pdf(np.arange(-3,-1,0.01),loc=0, scale=1)
#plt.ylim(0, 0.45)
#z_1=scipy.stats.norm.cdf(x=-1, loc=0, scale=1)
#z=1-scipy.stats.norm.cdf(x=-1, loc=0, scale=1)
#plt.fill_between(x=np.arange(-3,-1,0.01), y1=scipy.stats.norm.pdf(np.arange(-3,-1,0.01)), facecolor='blue', alpha=0.65, edgecolor='black')
#plt.fill_between(x=np.arange(-1,3,0.01), y1=scipy.stats.norm.pdf(np.arange(-1,3,0.01)), facecolor='red', alpha=0.65, edgecolor='black')
#plt.vlines(x=-1, ymin=0, ymax=0.24, linestyles='dashed', colors='black')

#plt.text(x=-1.9, y=0.03, s=round(z_1, 4), fontsize=14)
#plt.text(x=0.5, y=0.03, s=round(z, 4), fontsize=14)

#plt.show()


#scipy.stats.binom.rvs(n=10,p=0.5)
#scipy.stats.binom.rvs(size=5, n=10,p=0.5, random_state=0)
"""-------------------------------------------------------------------------------------------"""
"""Q. 3 years back, the average price of a used car was 6000$. Has it changed now?"""
print ('Question 1.')
cars=cars[(cars['yearOfRegistration']<=2018)
          &(cars['yearOfRegistration']>=1950)
          &(cars['price']>=100)&(cars['price']<=150000)
          &(cars['powerPS']>=10)
          &(cars['powerPS']<=500)]
alpha= 0.05
""" Arriving at sub sample from 'cars' data """

sample_size=1000
sample_1=cars.sample(sample_size, random_state=0)
sample_2=cars.sample(sample_size, random_state=56)
sample_3=cars.sample(sample_size, random_state=78)

pos_mean= 6000
print(sample_1['price'].mean())
print(sample_2['price'].mean())
print(sample_3['price'].mean())

statistic_1,pvalue_1=ttest_1samp(sample_1['price'], pos_mean)
statistic_2,pvalue_2=ttest_1samp(sample_2['price'], pos_mean)
statistic_3,pvalue_3=ttest_1samp(sample_3['price'], pos_mean)

print (statistic_1,pvalue_1)
print (statistic_2,pvalue_2)
print (statistic_3,pvalue_3)

"""Calculating degrees of freedom"""
n= len(cars['price'])
defr=n-1

from scipy.stats import t
cv=t.ppf([alpha/2,1-alpha/2],defr)
print(cv)
"""-------------------------------------------------------------------------------------------"""
"""Q. 3 years back, the percentage of used with automatic transmission were 25%. Has it changed now?"""
print ('Question 2.')

from statsmodels.stats.proportion import proportions_ztest
p0=0.23
count_1=sample_1['gearbox'].value_counts().iloc[1]
nobs_1=len(sample_1['gearbox'])

count_2=sample_2['gearbox'].value_counts().iloc[1]
nobs_2=len(sample_2['gearbox'])

count_3=sample_3['gearbox'].value_counts().iloc[1]
nobs_3=len(sample_3['gearbox'])


statistic_oneprop_1,pvalue_oneprop_1=proportions_ztest(count=count_1, nobs=nobs_1, value=p0, alternative='two-sided', prop_var=False)
statistic_oneprop_2,pvalue_oneprop_2=proportions_ztest(count=count_2, nobs=nobs_2, value=p0, alternative='two-sided', prop_var=False)
statistic_oneprop_3,pvalue_oneprop_3=proportions_ztest(count=count_3, nobs=nobs_3, value=p0, alternative='two-sided', prop_var=False)
print(statistic_oneprop_1,pvalue_oneprop_1)
print(statistic_oneprop_2,pvalue_oneprop_2)
print(statistic_oneprop_3,pvalue_oneprop_3)

cv_norm=scipy.stats.norm.ppf([alpha/2,1-alpha/2])
print(cv_norm)
"""-------------------------------------------------------------------------------------------"""
"""Q. Is the mean price of cars that have run 30K -60k km the sam e as that of 70k-90k km?"""
print ('Question 3.')

cars_1=cars[(cars['kilometer']>=30000)&(cars['kilometer']<=60000)]
cars_2=cars[(cars['kilometer']>=70000)&(cars['kilometer']<=90000)]

"""But, here you dont know if there is a statistically difference in the compuerd values
mean=cars_1['price'].sum()/len(cars_1['price'])
print(mean)
mean1=cars_2['price'].sum()/len(cars_2['price'])
print(mean1)"""

sample_cars_10=cars_1.sample(500, random_state=0)
sample_cars_11=cars_1.sample(500, random_state=67)
sample_cars_12=cars_1.sample(500, random_state=59)

sample_cars_20=cars_2.sample(500, random_state=0)
sample_cars_21=cars_2.sample(500, random_state=67)
sample_cars_22=cars_2.sample(500, random_state=59)

#Sample variance

var_10=sample_cars_10['price'].var()
var_11=sample_cars_11['price'].var()
var_12=sample_cars_12['price'].var()

var_20=sample_cars_20['price'].var()
var_21=sample_cars_21['price'].var()
var_22=sample_cars_22['price'].var()

#Sample mean

mean_10=sample_cars_10['price'].mean()
mean_11=sample_cars_11['price'].mean()
mean_12=sample_cars_12['price'].mean()

mean_20=sample_cars_20['price'].mean()
mean_21=sample_cars_21['price'].mean()
mean_22=sample_cars_22['price'].mean()

# F statistic
from scipy.stats import f
F1=var_20/var_10 #The larger value is usually put in the numerator
F2=var_21/var_11
F3=var_22/var_12
print('F1',F1,'F2',F2,'F3',F3)
df_10=len(sample_cars_10)-1
df_11=len(sample_cars_11)-1
df_12=len(sample_cars_12)-1

df_20=len(sample_cars_20)-1
df_21=len(sample_cars_21)-1
df_22=len(sample_cars_22)-1

f_stat1=scipy.stats.f.cdf(F1,df_10,df_20)
f_stat2=scipy.stats.f.cdf(F2,df_11,df_21)
f_stat3=scipy.stats.f.cdf(F3,df_12,df_22)
print('f_stat1',f_stat1,'f_stat2',f_stat2,'f_stat3',f_stat3)
critical_value=f.ppf([alpha/2,1-alpha/2],df_10,df_20)
print('Critical value=',critical_value)

from scipy.stats import ttest_ind
statistic_twomean1,pvalue_twomean1=ttest_ind(sample_cars_10['price'],sample_cars_20['price'],equal_var=False)
statistic_twomean2,pvalue_twomean2=ttest_ind(sample_cars_11['price'],sample_cars_21['price'],equal_var=False)
statistic_twomean3,pvalue_twomean3=ttest_ind(sample_cars_12['price'],sample_cars_22['price'],equal_var=False)

print('St_twomean1',statistic_twomean1,'pvalue1',pvalue_twomean1,
      'St_twomean2',statistic_twomean2,'pvalue2',pvalue_twomean2,
      'St_twomean3',statistic_twomean3,'pvalue3',pvalue_twomean3)


# Print a header
print(f"{'Sample Set':<15} {'T-Statistic':<15} {'P-Value':<15}")
print("-" * 45) # Print a separator line

# Print each row of results
print(f"{'Set 1':<15} {statistic_twomean1:<15} {pvalue_twomean1:<15}")
print(f"{'Set 2':<15} {statistic_twomean2:<15} {pvalue_twomean2:<15}")
print(f"{'Set 3':<15} {statistic_twomean3:<15} {pvalue_twomean3:<15}")

