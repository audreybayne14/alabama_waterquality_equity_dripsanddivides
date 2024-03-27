#!/usr/bin/env python
# coding: utf-8

# In[81]:


# import necessary packages

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy.stats import pearsonr
import matplotlib.colors as mcolors


# In[17]:


# load csv data from merged excel power query table
merged_table = pd.read_csv("al_wq_master_query.csv")

# load shapefile for alabama counties
alabama_counties = gpd.read_file("alabama_counties.shp")


# In[28]:


# Load population data
population_data = merged_table[['CountiesServed', 'cons_demo.ACSTOTPOP']].drop_duplicates()

# merge population data with aggregated county data
county_data = county_data.merge(population_data, how='left', on='CountiesServed')

# calculate violations rate per 100,000 residents
county_data['violations_per_100k'] = (county_data['total_violations'] / county_data['cons_demo.ACSTOTPOP']) * 100000


# In[87]:


# create custom colormap
colors = ['#FFFFFF', '#5D6457']
cmap = mcolors.LinearSegmentedColormap.from_list('custom_colormap', colors, N=256)

# merge county data with shapefile
county_map_data = alabama_counties.merge(county_data, how='left', left_on='NAME', right_on='CountiesServed')

# create the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# plot the map
county_map_data.plot(column='violations_per_100k', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# set plot title and labels
ax.set_title('Health-Significant Water Quality Violations per 100,000 Residents by County')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Show the plot
plt.show()


# In[89]:


# create custom colormap
colors = ['#FFFFFF', '#5D6457']
cmap = mcolors.LinearSegmentedColormap.from_list('custom_colormap', colors, N=256)

# merge county data with shapefile
county_map_data = alabama_counties.merge(county_data, how='left', left_on='NAME', right_on='CountiesServed')

# create the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# plot the map
county_map_data.plot(column='pct_people_of_color', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# set plot title and labels
ax.set_title('Percentage of Population Identifying as People of Color by County')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# show the plot
plt.show()

# calculate Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(county_data['pct_people_of_color'], county_data['violations_per_100k'])

print("Pearson correlation coefficient:", correlation_coefficient)
print("p-value:", p_value)


# In[92]:


# create custom colormap
colors = ['#FFFFFF', '#5D6457']
cmap = mcolors.LinearSegmentedColormap.from_list('custom_colormap', colors, N=256)

# merge county data with shapefile
county_map_data_lowincome = alabama_counties.merge(county_data, how='left', left_on='NAME', right_on='CountiesServed')

# create the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# plot the map
county_map_data_lowincome.plot(column='PCT_LOWINCOME', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# set plot title and labels
ax.set_title('Percentage of Population Categorized as "Low-Income" by County')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# show the plot
plt.show()

# Calculate Pearson correlation coefficient
correlation_coefficient_lowincome, p_value_lowincome = pearsonr(county_data['PCT_LOWINCOME'], county_data['violations_per_100k'])

print("Pearson correlation coefficient:", correlation_coefficient_lowincome)
print("p-value:", p_value_lowincome)


# In[96]:


# create custom colormap
colors = ['#FFFFFF', '#5D6457']
cmap = mcolors.LinearSegmentedColormap.from_list('custom_colormap', colors, N=256)

# merge county data with shapefile
county_map_data_lesshs_x = alabama_counties.merge(county_data, how='left', left_on='NAME', right_on='CountiesServed')

# create the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# plot the map
county_map_data_lesshs_x.plot(column='PCT_LESSHS_x', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# set plot title and labels
ax.set_title('Percentage of Population with Less than a High School Education by County')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# show the plot
plt.show()

# Calculate Pearson correlation coefficient
correlation_coefficient_lesshs_x, p_value_lesshs_x = pearsonr(county_data['PCT_LESSHS_x'], county_data['violations_per_100k'])

print("Pearson correlation coefficient:", correlation_coefficient_lesshs_x)
print("p-value:", p_value_lesshs_x)

