import pandas as pd

def popular_lang():
    file_path = 'repositories.csv'
    df = pd.read_csv(file_path)

    column_name = 'language'
    top_1_values = df[column_name].value_counts().head(1)

    print(top_1_values)

def to_get_popular_prog_lan_after_2020():
    file_path = 'repositories.csv'
    df = pd.read_csv(file_path)
    year_column = 'created_at'
    lang = 'language'

    filtered_data = df[df[year_column] > 2020]

    print(filtered_data)

to_get_popular_prog_lan_after_2020()

