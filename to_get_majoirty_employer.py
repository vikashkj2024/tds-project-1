import pandas as pd
file_path = 'users.csv'
df = pd.read_csv(file_path)

column_name = 'company'
top_1_value = df[column_name].value_counts().head(1)

print(top_1_value)
