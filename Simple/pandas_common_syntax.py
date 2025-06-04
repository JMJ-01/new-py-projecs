import pandas as pd
import numpy as np # For creating sample data

# Sample data
data = {
    'age': [25, 30, 22, 35, 28],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'],
    'occupation': ['Engineer', 'Artist', 'Analyst', 'Doctor', 'Designer']
}
# Custom index labels
index_labels = ['person_A', 'person_B', 'person_C', 'person_D', 'person_E']

df = pd.DataFrame(data, index=index_labels)
print("Original DataFrame:")
print(df)
print("-" * 30)

print("\nUsing loc - Single row ('person_B'):")
print(df.loc['person_B'])
print("-" * 30)
print("\nUsing loc - Multiple rows (['person_A', 'person_D']):")
print(df.loc[['person_A', 'person_D']])
print("-" * 30)
print("\nUsing loc - Slice of rows ('person_B':'person_D'):")
print(df.loc['person_B':'person_D']) # Includes 'person_D'
print("-" * 30)
print("\nUsing loc - Single cell ('person_C', 'city'):")
print(df.loc['person_C', 'city'])
print("-" * 30)
print("\nUsing loc - Specific rows and columns (['person_A', 'person_E'], ['age', 'occupation']):")
print(df.loc[['person_A', 'person_E'], ['age', 'occupation']])
print("-" * 30)
print("\nUsing loc - All rows for 'city' and 'occupation' columns:")
print(df.loc[:, ['city', 'occupation']]) # ':' means all rows
print("-" * 30)
print("\nUsing loc - Boolean indexing (age > 28):")
print(df.loc[df['age'] > 28])
print("-" * 30)
print("-" * 30)
print("-" * 30)
print("-" * 30)
print("-" * 30)