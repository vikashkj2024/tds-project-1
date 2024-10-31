import pandas as pd

# Load both CSV files
df1 = pd.read_csv('users.csv')  # CSV with loginName and Year
df2 = pd.read_csv('repositories.csv') # CSV with loginName, repos, and language used

# Filter df1 to include only rows where Year is greater than 2020
filtered_df1 = df1[df1['Year'] > 2020]

# Merge the filtered df1 with df2 on loginName to get only relevant loginNames
merged_df = pd.merge(filtered_df1[['login']], df2, on='login', how='inner')

# Now find the most used language for each loginName
# Group by loginName and language used, count occurrences, then find the max for each loginName
language_counts = merged_df.groupby(['login', 'language']).size().reset_index(name='count')
most_used_language = language_counts.loc[language_counts.groupby('login')['count'].idxmax()]

# Display the results
print("Most used language for each loginName with Year > 2020:")
print(most_used_language[['login', 'language']])
