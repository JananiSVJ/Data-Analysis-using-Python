import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\saich\\Desktop\\banana-republic-copy.csv")

# DATA CLEANING

# To insert a unique Id to the original data set
df.insert(0, 'Order_Id', range(1, 1+len(df)))

#To rename the incorrect column names - estimated time & actual time -- change to -- estimated date & actual date

df = df.rename(columns={'ESTIMATED TIME OF ARRIVAL': 'ESTIMATED DATE OF ARRIVAL'}, errors="raise")
df = df.rename(columns={'ACTUAL TIME OF ARRIVAL': 'ACTUAL DATE OF ARRIVAL'}, errors= "raise")

# To check for duplicated rows - There are no such rows in this data set
# print(df.duplicated(subset=None, keep='first')) # Displays true for the duplicated rows
# df.drop_duplicates(keep='first', inplace=True)  # Drops the second occurrence of the duplicated rows,if any

# df = df.replace('-NOT AVAILABLE-', np.nan)  # REPLACE -NOT AVAILABLE- VALUES TO Nan IN ALL COLUMNS (To add default value)
# df = df.replace(' ', np.nan)                # REPLACE "empty values"  TO Nan IN ALL COLUMNS

# df = df.dropna(how='all')    - To drop rows that have all NA values
# df = df.dropna(thresh=5)     - Data needs to have at least 5 non-null values
# df = df.dropna(subset=['SHIPPER'])  - To remove the rows with na in shipper column
df = df.dropna()    # - to drop the rows with any na values



# To convert the date format from string to date
df['ESTIMATED DATE OF ARRIVAL'] = pd.to_datetime(df['ESTIMATED DATE OF ARRIVAL'], infer_datetime_format=True)
df['ACTUAL DATE OF ARRIVAL'] = pd.to_datetime(df['ACTUAL DATE OF ARRIVAL'], infer_datetime_format=True)
# To find the delay in shipping
df['delay'] = df['ESTIMATED DATE OF ARRIVAL']-df['ACTUAL DATE OF ARRIVAL']
print(df['delay'])

# Correlation between delay and number of orders
plot_df = pd.DataFrame({'Order_Id': df['Order_Id'], 'Delay': df['delay']})
plot_df = plot_df.dropna()
plot_Delay = plot_df['Delay'].values
for i in plot_df['Delay']:
    print(i)
plt.hist(plot_df['Delay'], color = 'blue', edgecolor = 'black',
         bins = int(180/5))
plt.xlabel('Delay')
plt.ylabel('Number of Orders')
plt.title('Histogram of Delay')
plt.grid(True)
plt.show()

# Correlation between origin and number of orders
plot_origin_df = pd.DataFrame({'Order_Id': df['Order_Id'], 'Origin': df['COUNTRY OF ORIGIN']})
plt.hist(plot_origin_df['Origin'], color = 'blue', edgecolor = 'black',
         bins = int(180/5))
plt.xlabel('Origin')
plt.ylabel('Number of Orders')
plt.title('Histogram of Number of Orders from a origin')
plt.grid(True)
plt.show()






