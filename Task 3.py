"""You are provided with insurance dataset on blackboard. Please logon on blackboard and download the 
dataset. Write a python code to:
§ 
§ 
§ 
§"""

import pandas as pd


#Read the dataset.

data = pd.read_csv("")

#Inspects its column by displaying the first 10 records.
print(data.head(10))

#Display records for make and usage for sets_num that are more than 40.
print(data[data['sets_num']>40[['make', 'usage']]])

# Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes

import matplotlib.pyplot as plt

plt.plot(data['EFFECTIVE_YR'], data['CARRYING_CAPACITY'])
plt.tlabel('EFFECTIVE YEAR')
plt.xlabel('CARRYING CAPACITY')
plt.title('Effective year vs carrying capacity')
plt.show()