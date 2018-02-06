# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Set working directory
import os
os.chdir('/Users/nicholasbeaudoin/Desktop/PGATour')

# ##import packages
import pandas as pd
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

### LOAD DATA ###

### Load 2017 season Shotlink data into pandas dataframe
file = '2017.TXT'
df = pd.read_table(file, sep=';', dtype={'Tour Code': np.object_, 
                                         'Tour Description': np.object_,
                                         'Year': np.object_,
                                         'Tourn.#': np.object_,
                                         'Player #': np.object_,
                                         'Course #': np.object_,
                                         'Permanent tournament': np.object_,
                                         'Player Last Name': np.object_,
                                         'Round': np.object_,
                                         'Tournament Name': np.object_,
                                         'Course Name': np.object_,
                                         'Hole': np.object_,
                                         'Hole Score': int,
                                         'Yardage': int,
                                         'Shot Type(S/P/D)': np.object_,
                                         '# of Strokes': int,
                                         'From Location(Scorer)': np.object_,
                                         'From Location(Enhanced)': np.object_,
                                         'To Location(Scorer)': np.object_,
                                         'To Location(Enhanced)': np.object_,
                                         'Distance': int,
                                         'Distance to Pin': int,
                                         'In the Hole Flag': np.object_,
                                         'Around the Green Flag': np.object_,
                                         '1st Putt Flag': np.object_,
                                         'Distance to Hole after the Shot': int,
                                         'Time': np.object_,
                                         'Lie': np.object_,
                                         'Elevation': np.object_,
                                         'Slope': np.object_,
                                         'X Coordinate': int,
                                         'Y Coordinate': int,
                                         'Z Coordinate': int,
                                         'Distance from Center': int,
                                         'Distance from Edge': int,
                                         'Date': np.object_,
                                         'Left/Right': int,
                                         'Strokes Gained/Baseline': int,
                                         'Recovery Shot': np.object_}
                   )

### DATA CLEANING ###

### Check dataframe and data type
print(df.shape)
print(type(df))
print(df.columns)
df.loc[0:5,:]

'''
There is a problem in the test file that we are trying to load. 
There are 8 columns that have leading white spaces. 
To remove these and use the specified delimiter consistenty, 
we need to call the "strip()" function in pandas to create these consistent 
column headers.
'''

### Trim white space
df = df.rename(columns=lambda x: x.strip())
# Check to see if leading white space is removed from header names
print(df.columns)

'''
Another issue that we are running into is that the numbers for some of the 
variables are strings and have leading whitespace before their values. 
Below one can see that there are significant doulbe counting of the scores. 
This all stems from the variable being a string.

We will use "Hole "Score" as an example of what this looks like and how to fix 
it by converting to a pandas series, then a string value, then using the 
"strip()" method to replace the white space. We will then conver the string 
to a numeric value.
'''

### Problem: values are double counts and have leading white space.
df["Hole Score"].dtype
df["Hole Score"].value_counts()

### Remove leading white space on "Hole Score"
# Convert to string
# Strip white space
df["Hole Score_2"] = df["Hole Score"].str.strip()

# Convert back to integer
df["Hole Score_2"] = pd.to_numeric(df["Hole Score_2"])

# Look at "Hole Score"
df["Hole Score_2"].dtype
df["Hole Score_2"].value_counts()
df["Hole Score"] = df["Hole Score_2"]

# Check our work
df["Hole Score"].value_counts()

### DATA EXPLORATION ###

### How many shots were taken on the PGA Tour in 2017?
print("Total Strokes: ")
print(df["# of Strokes"].sum())

# What did the shot distribution look like? How many penalties and double shots?
print(df["# of Strokes"].value_counts())

ax = df['# of Strokes'].value_counts().plot(kind='barh', figsize=(15, 10),
                                        color="coral", fontsize=15);
ax.set_alpha(1)
ax.set_title("Stroke Distribution for 2017 PGA Tour Season (shots)", fontsize=20)
ax.set_xlabel("Shots hit per category", fontsize=18);
ax.set_xticks([0, 250000, 500000, 750000, 1000000, 1250000])

# create a list to collect the plt.patches data
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_width())
    
# set individual bar lables using above list
total = sum(totals)

# set individual bar labels using above list
for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=15, color='dimgrey')

# invert for largest on top 
ax.invert_yaxis()

# Source: http://robertmitchellv.com/blog-bar-chart-annotations-pandas-mpl.html

### What is the average distance on Par 3, 4, 5s?

ax = df.groupby(["Par Value"])["Yardage"].mean().plot(kind='barh', figsize=(12, 8),
                                        color="blue", fontsize=15);
ax.set_alpha(1)
ax.set_title("Average Yardages in 2017", fontsize=20)
ax.set_xlabel("Yardage", fontsize=18);
ax.set_xticks([0, 100, 200, 300, 400, 500, 600])

# create a list to collect the plt.patches data
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_width())
    
# set individual bar lables using above list
total = sum(totals)

# set individual bar labels using above list
for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=15, color='dimgrey')

### What is the longest distance on Par 3, 4, 5s?

ax = df.groupby(["Par Value"])["Yardage"].max().plot(kind='barh', figsize=(12, 8),
                                        color="red", fontsize=15);
ax.set_alpha(1)
ax.set_title("Average Yardages in 2017", fontsize=20)
ax.set_xlabel("Yardage", fontsize=18);
ax.set_xticks([0, 100, 200, 300, 400, 500, 600])

# create a list to collect the plt.patches data
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_width())
    
# set individual bar lables using above list
total = sum(totals)

# set individual bar labels using above list
for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=15, color='dimgrey')
    

### What is the shortest distance on Par 3, 4, 5s?

ax = df.groupby(["Par Value"])["Yardage"].min().plot(kind='barh', figsize=(12, 8),
                                        color="red", fontsize=15);
ax.set_alpha(1)
ax.set_title("Average Yardages in 2017", fontsize=20)
ax.set_xlabel("Yardage", fontsize=18);
ax.set_xticks([0, 100, 200, 300, 400, 500, 600])

# create a list to collect the plt.patches data
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_width())
    
# set individual bar lables using above list
total = sum(totals)

# set individual bar labels using above list
for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=15, color='dimgrey')    


