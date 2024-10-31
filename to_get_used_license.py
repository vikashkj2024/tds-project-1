import pandas as pd
file_path = 'repositories.csv'
df = pd.read_csv(file_path)

column_name = 'license_name'
top_3_values = df[column_name].value_counts().head(3)

print(top_3_values)
