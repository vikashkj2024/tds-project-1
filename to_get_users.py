
import requests
import csv

# GitHub API URL and Authentication
GITHUB_TOKEN = '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'  
headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# Set parameters
city = "Moscow"
min_followers = 50
url = "https://api.github.com/search/users"

# Search users by location
params = {
    'q': f'location:{city}',
    'per_page': 100  # GitHub's max per page limit
}

# Function to clean company names
def clean_company_name(company):
    if company:
        company = company.strip().lstrip('@').upper()
    return company

# Initialize list for users
users = []
page = 1

while True:
    # Update page for pagination
    params['page'] = page
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'items' not in data:
        print("No users found or an error occurred.")
        break

    # Filter users by followers count
    for user in data['items']:
        user_data = requests.get(user['url'], headers=headers).json()
        if user_data.get('followers', 0) > min_followers:
            users.append({
                'login': user_data['login'],
                'name': user_data.get('name', ''),
                'company': clean_company_name(user_data.get('company', '')),
                'location': user_data.get('location', ''),
                'email': user_data.get('email', ''),
                'hireable': user_data.get('hireable', False),
                'bio': user_data.get('bio', ''),
                'public_repos': user_data.get('public_repos', 0),
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'created_at': user_data.get('created_at', '')
            })

    # Check if more pages exist
    if 'next' not in response.links:
        break
    page += 1

# Save data to CSV
csv_file = "users.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

print(f"Data saved to {csv_file}")


