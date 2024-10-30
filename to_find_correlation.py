import pandas as pd

file_path = 'users.csv'
data = pd.read_csv(file_path)

column1 = 'public_repos'
column2 = 'followers'

correlation = data[column1].corr(data[column2])

print(f"Correlation between {column1} and {column2}: {correlation}")



