import pandas as pd
import numpy as np

# --- Create a Sample DataFrame ---
# This creates a sample DataFrame similar to what you might have.
data = {
    'Price': [5000, 8450, 9000, 11950, 15000, 7000, 20000]
}
data_csv1 = pd.DataFrame(data)

# --- Method 1: The pd.cut() function (Often the best for binning) ---
# This "vectorized" approach is very fast and readable.
# It's designed for this exact task: segmenting data into discrete intervals.

print("\n--- Running Method 1: pd.cut() ---")
# Define the edges of our price bins.
# -inf to 8450, 8450 to 11950, 11950 to +inf
bins = [-np.inf, 8450, 11950, np.inf]
# Define the labels for those bins.
labels = ["Low", "Medium", "High"]
# Create the 'Price_Class' column in one go.
data_csv1['Price_Class_Cut'] = pd.cut(data_csv1['Price'], bins=bins, labels=labels)


# --- Method 2: The .apply() method ---
# This is very flexible. You write a standard Python function and then
# "apply" it to every value in a Series (a column).

print("\n--- Running Method 2: .apply() ---")
# 1. Define the function that contains your logic for a single value.
def classify_price(price):
    if price <= 8450:
        return "Low"
    elif price <= 11950:
        return "Medium"
    else:
        return "High"

# 2. Apply the function to the 'Price' column.
data_csv1['Price_Class_Apply'] = data_csv1['Price'].apply(classify_price)


# --- Method 3: Boolean Indexing ---
# This method is extremely fast and powerful. You create logical conditions
# (which return True/False) and use those conditions to select and update
# parts of the DataFrame.

print("\n--- Running Method 3: Boolean Indexing ---")
# 1. Create the column, you can set a default value.
# Here, we'll use np.select for a clean, multi-condition approach.
conditions = [
    data_csv1['Price'] <= 8450,
    data_csv1['Price'] <= 11950
]
choices = ['Low', 'Medium']
# np.select takes a list of conditions, a list of choices, and a default value.
data_csv1['Price_Class_Boolean'] = np.select(conditions, choices, default='High')


# --- Display the final result ---
# All three methods produce the same result, but are useful in different scenarios.
print("\n--- Final DataFrame ---")
print(data_csv1)