#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/satvik/Desktop/dataset/movies.csv')


# # 1. Display Top 10 Rows of The Dataset

# In[2]:


data.head(10) # Head function is used to display the rows of the dataset from top , in this case it will display
# top 10 rows as we have passed the argumen 10


# # 2. Check Last 10 Rows of the dataset
# 

# In[3]:


data.tail(10) # tail column displays the rows of dataset from last 


# # 3. Find shape of the dataset (no of rows and columns)

# In[ ]:


# data.shape # shape attribute is used for calculating the no of rows and columns present in the database
print("No of rows in dataset:" , data.shape[0])
print("No of column in dataset:",data.shape[1])


# # 4. Getting Information about our dataset like total number of rows , total number of columns , datatypes of each column and memory requirement
# 

# In[8]:


data.info() # gives information about the dataset 


# # 5. Check missing values in the dataset 

# In[10]:


print("Any missing values:", data.isnull().values.any())
# As the output displayed is true we need to check , which columnn has got missing values 


# In[11]:


data.isnull().sum()


# In[12]:


# As we can see that there is one missing value in the certificate column
# we need to visulize it , for which we will use seaborn library
# In the seaborn library we will be using heatmap , to visualize missing value
sns.heatmap(data.isnull()) # Heatmap is showing missing values in light colour 


# In[14]:


# Checking the percentage of missing values in the dataset
per_missing = data.isnull().sum() * 100 / len(data)
per_missing


# # 6. Drop all the missing values 

# In[15]:


data.dropna(axis = 0)


# # 7. Check for Duplicate Data 

# In[18]:


dup_data = data.duplicated().any()
print("Are there any duplicate values in dataset:", dup_data)


# In[ ]:


# In the dataset currently we don't have any duplicate values , but if we they are present in the dataset we can drop the
# values using : data = data.drop_duplicates()


# # 8.Get overall statistics about the DataFrame

# In[19]:


data.describe()


# # 9. Plot a graph to show distribution of the genere in the top 250 movies 

# In[5]:


# Loading the dataset into pandas data frame
df = pd.read_csv('/Users/satvik/Desktop/dataset/movies.csv')

# Getting the count of each genere in the top 250 movies 
genre_counts = df['genre'].head(15).value_counts()
genre_counts


# In[8]:


# Plotting the graph
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 9))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Genres in Top 250 Movies')
plt.axis('equal')


# # 10. find out movies of each genre which has maximum number of votes. 
# 

# In[3]:


import pandas as pd
data = pd.read_csv('/Users/satvik/Desktop/dataset/movies.csv')

# Important : Please note as there is mistake in dataset instead of "imdb", "imbd" is written in the column that why i have used 
#"imbd" for my doing analysis 
max_votes = data.groupby("genre").agg({"imbd_votes": "max"})
max_votes


# # 11. find out which movie has the maximum number of votes and which genre it belongs to and its duration

# In[4]:


import pandas as pd 
data = pd.read_csv('/Users/satvik/Desktop/dataset/movies.csv')
max_votes = (data["imbd_votes"].max())
print(max_votes)
# This will get the maximum votes 


# In[8]:


# finding out the name of the movie and other details like genere , duration etc
Max = data[data["imbd_votes"] == data["imbd_votes"].max()]
print("Movies:", Max["title"].values[0])
print("Genre:",Max["genre"].values[0])
print("Duration:", Max["duration"].values[0])


# # 12. find out which movie has the minimum number of votes and which genre it belongs to and its duration

# In[9]:


import pandas as pd 
data = pd.read_csv('/Users/satvik/Desktop/dataset/movies.csv')
min_votes = (data["imbd_votes"].min())
print(min_votes)
# This will get the minimum votes 


# In[10]:


Min = data[data["imbd_votes"] == data["imbd_votes"].min()]
print("Movies:", Min["title"].values[0])
print("Genre:",Min["genre"].values[0])
print("Duration:", Min["duration"].values[0])
# finding out the name of the movie and other details like genere , duration etc


# In[11]:


data.columns


# # 13. Displaying no of movies per year 

# In[12]:


data['year'].value_counts()
# displaying no of movies per year 


# In[ ]:





# In[ ]:




