import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv('/Users/abhinavpundir/Desktop/Studies/Data Science/Examining Netflix Movies/netflix_data.csv')
# Subset of DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type']=='Movie']
netflix_movies_col_subset = netflix_df_movies_only.loc[:,['title','country', 'genre', 'release_year','duration']]
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration'])
plt.title("Movie Duration by Year of Release")
plt.show()

# Filter for durations shorter than 60 minutes
short_movies =netflix_movies_col_subset[netflix_movies_col_subset['duration']<60]

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for l,r in netflix_movies_col_subset.iterrows():
    if r['genre']=='Children':
        colors.append('red')
    elif r['genre']=='Documentaries':
        colors.append('blue')
    elif r['genre']=='Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset['duration'],netflix_movies_col_subset['release_year'],edgecolors=colors)

# Create a title and axis labels
plt.title('Movie duration by year of release')
plt.xlabel('Duration(hours)')
plt.ylabel('Release Year')

# Show the plot
plt.show()