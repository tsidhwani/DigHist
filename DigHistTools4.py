import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/tapansidhwani/Downloads/census_data.csv' 
census_data = pd.read_csv(file_path)

davidson_code = 370 
relevant_years = [1820, 1830, 1840]

davidson_data = census_data[
    (census_data['county'] == davidson_code) & (census_data['year'].isin(relevant_years))
]

population_totals = davidson_data.groupby('year')['ntotal'].sum()

plt.figure(figsize=(8, 6))
plt.plot(population_totals.index, population_totals.values, marker='o', color='b')
plt.title('Davidson County Population (1820-1840)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Population', fontsize=12)
plt.grid(True)
plt.xticks(population_totals.index)
plt.show()
