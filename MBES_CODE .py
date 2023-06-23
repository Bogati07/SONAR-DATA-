#!/usr/bin/env python
# coding: utf-8

# # SFT  REPORT
# 
# **SEDIMENT MASS PERUNIT VOLUME CALCULATION FOR SEDIMENT DEPOSITS IN RIVER ELBBE**
# 
# **DEEPAK BOGATI (6066481)**
# 
# **SUBMITTED TO Ellen Werner, Mona Lütjens, Annette Scheider**

# # INTRODUCTION 
# 
# Python is a programming language that is widely used in the software industry and academia. It is known for its simplicity, readability, and flexibility, which make it a popular choice for beginners and experienced programmers alike. Python has a large and active community of users, which has contributed to the development of a wide range of libraries and frameworks that support a variety of programming tasks, including data analysis, machine learning, and scientific computing. In this project, we are analyzing a Multibeam and single beam data form DV Ocean survey done on 2nd of july 2021 using python in jupiternote book.
# 
# After cleaning the noise form the data in qimera, x,y,z export from qimera is imported in jupiter notebook for volume calculation of the sediments in five diefferent target locations. 
# 
# 

# **Importing Necessary Liberaries** 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon


# # sample 1

# **Importing x,y,z Low Frequency singlebeam data form qimera for location/Line 1 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for low frequancy data**

# In[37]:


#LfL1 (short form for lowfrequensy SBES data for line 1) 
df = pd.read_csv('test.csv')
#print(df.head())
# Extract the XYZ coordinates from the DataFrame
#x = df['Footprint X']
#y = df['Footprint Y']
#z = df['Footprint Z']
df


# **Importing x,y,z High frequency singlebeam data form qimera for location/Line 1 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for High frequamcy data**

# In[39]:


df1


# In[40]:


df2


# In[36]:


# Loading the data into a data frame
df1 = pd.read_csv('LfL1.csv')
df2 = pd.read_csv('HfL1.csv')

# Extracting the columns to be plotted
low = df['Footprint Z']
high = df2['Footprint Z']
low.mean()

plt.plot(low)
plt.plot(high)
plt.ylim(1, 14)

# Adding a label to the y-axis
plt.ylabel('Depth in meters')

# Show the plot
plt.show()
thickness = df["Footprint Z"] - df2["Footprint Z"] 
thickness = thickness.mean()
thickness


# In[38]:


df1


# In[16]:


a = low.mean()
b = high.mean()
a-b


# **The approximate bulk density of wet clay that is commonly used in normal-weight concrete is between 1240-1410 kg/m3. considering 1300kg/m3 density for the sample sediment**

# In[17]:


#area of the target survey areas imported from Qimera.
area1 = 8050.50
area2 = 5443.01
area3 = 1423.81
area4 = 393.31
area5 = 12155.63


# In[18]:


#Calculation of sediment mass per unit area.
density = 1300
volume = area1 * thickness
mass = density*volume
mass
sediment_mass_per_unit_area = mass/area1
sediment_mass_per_unit_area


# # Sample 2

# **Importing x,y,z Low Frequency singlebeam data form qimera for location/Line 2 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for low frequancy data**

# In[19]:


df3 = pd.read_csv('LfL2.csv')
df4 = pd.read_csv('HfL2.csv')
df3


# In[20]:


df4


# In[22]:


# Extracting the columns to be plotted
low = df3['Footprint Z']
high = df4['Footprint Z']
# Adding a label to the y-axis
plt.ylim(1, 14)

plt.ylabel('Depth in meters')
plt.xlabel('sounding samples')

plt.plot(low)
plt.plot(high)

plt.legend(["High Frequency", "Low Frequency"], loc ="lower right")

# Show the plot
plt.show()
thickness = df3["Footprint Z"] - df4["Footprint Z"]
thickness = thickness.mean()
thickness


# In[23]:


#Calculation of sediment mass per unit area.
density = 1300
volume = area2 * thickness
mass = density*volume
sediment_mass_per_unit_area = mass/area2
sediment_mass_per_unit_area


# In[24]:


a = low.mean()
b = high.mean()
#a


# # Sample 3
# 
# **Importing x,y,z Low Frequency singlebeam data form qimera for location/Line 3 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for low frequancy data**
# 

# In[25]:



df3 = pd.read_csv('LfL3.csv')
df4 = pd.read_csv('HfL3.csv')
df3
df4

# Extracting the columns to be plotted
low = df3['Footprint Z']
high = df4['Footprint Z']
# Adding a label to the y-axis
plt.ylim(1, 8)

plt.ylabel('Depth in meters')
plt.xlabel('sounding samples')

plt.plot(low)
plt.plot(high)

plt.legend(["High Frequency", "Low Frequency"], loc ="lower right")

# Show the plot
plt.show()
thickness = df3["Footprint Z"] - df4["Footprint Z"]
thickness = thickness.mean()
thickness


# In[26]:


a = low.mean()
b = high.mean()
#b


# In[27]:


#Calculation of sediment mass per unit area.
density = 1300
volume = area3 * thickness
mass = density*volume
sediment_mass_per_unit_area = mass/area3
sediment_mass_per_unit_area


# # Sample 4
# 
# **Importing x,y,z Low Frequency singlebeam data form qimera for location/Line 4 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for low frequancy data**
# 

# In[29]:



df3 = pd.read_csv('LfL4.csv')
df4 = pd.read_csv('HfL4.csv')
#df3
#df4

# Extracting the columns to be plotted
low = df3['Footprint Z']
high = df4['Footprint Z']
# Adding a label to the y-axis
plt.ylim(1, 7)

plt.ylabel('Depth in meters')
plt.xlabel('sounding samples')

plt.plot(low)
plt.plot(high)

plt.legend(["High Frequency", "Low Frequency"], loc ="lower right")

# Show the plot
plt.show()
thickness = df3["Footprint Z"] - df4["Footprint Z"]
thickness = thickness.mean()
thickness


# In[30]:


#Calculation of sediment mass per unit area.
density = 1300
volume = area4 * thickness
mass = density*volume
sediment_mass_per_unit_area = mass/area4
sediment_mass_per_unit_area


# In[31]:


a = low.mean()
b = high.mean()
#a


# # Sample 5
# 
# **Importing x,y,z Low and high Frequency singlebeam data form qimera for location/Line 5 and**
# 
# **Also removed the outliers form the height data for final vertical(z) data for low frequancy data**

# In[32]:



df3 = pd.read_csv('LfL5.csv')
df4 = pd.read_csv('HfL5.csv')
df3
df4

# Extracting the columns to be plotted
low = df3['Footprint Z']
high = df4['Footprint Z']
# Adding a label to the y-axis
plt.ylim(1, 14)

plt.ylabel('Depth in meters')
plt.xlabel('sounding samples')

plt.plot(low)
plt.plot(high)

plt.legend(["High Frequency", "Low Frequency"], loc ="lower right")

# Show the plot
plt.show()
thickness = df3["Footprint Z"] - df4["Footprint Z"]
thickness = thickness.mean()
thickness


# In[33]:


#Calculation of sediment mass per unit area.
density = 1300
volume = area5 * thickness
mass = density*volume
sediment_mass_per_unit_area = mass/area5
sediment_mass_per_unit_area

