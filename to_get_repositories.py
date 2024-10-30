import requests
import csv
import pandas as pd

# GitHub API Authentication
GITHUB_TOKEN = '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' 
headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# Input CSV file with user IDs (login)
input_csv_file = "users.csv"  
output_csv_file = "repositories.csv"  # Output CSV file

# Function to fetch repositories for a user
def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    params = {
        'sort': 'pushed',
        'direction': 'desc',
        'per_page': 100  # Max per request
    }
    
    repositories = []
    page = 1
    
    while len(repositories) < 500:
        params['page'] = page
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        if not data or 'message' in data:
            break

        for repo in data:
            # Stop if we exceed 500 records for this user
            if len(repositories) >= 500:
                break

            repositories.append({
                'login': username,
                'full_name': repo.get('full_name', ''),
                'created_at': repo.get('created_at', ''),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ''),
                'has_projects': repo.get('has_projects', False),
                'has_wiki': repo.get('has_wiki', False),
                'license_name': repo.get('license', {}).get('key', '') if repo.get('license') else ''
            })

        # Check if more pages exist
        if 'next' not in response.links:
            break
        page += 1

    return repositories

# Read the list of logins from the input CSV file
user_logins = []
with open(input_csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if row:
            user_logins.append(row[0].strip())  # Assuming login is in the first column

# Fetch data for each user and save to the output CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = [
        'login', 'full_name', 'created_at', 'stargazers_count', 
        'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for username in user_logins:
        print(f"Fetching repositories for user: {username}")
        repositories = fetch_repositories(username)
        writer.writerows(repositories)

print(f"Data saved to {output_csv_file}")
