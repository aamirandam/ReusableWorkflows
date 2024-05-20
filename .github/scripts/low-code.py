import requests
import json

# GitHub repository details
owner = 'your_username'
repo = 'your_repository'
branch = 'main'  # or any other branch you're working on

# File details
target_directory = 'path/to/target/directory'  # Relative path to the target directory
file_name = 'new_file.txt'
file_content = 'This is the content of the new file.'

# Authentication token - required for private repositories or for making many requests
# token = 'your_access_token'  # Uncomment and fill in if needed

# Construct the API endpoint
api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{target_directory}/{file_name}"

# Headers for the request
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'python'
}

# If authentication is required, add token to headers
# if token:
#     headers['Authorization'] = f'token {token}'

# Create a new file
def create_file():
    # Prepare the payload
    payload = {
        "message": "Create new file",
        "content": file_content,
        "branch": branch
    }

    # Convert content to base64
    content_bytes = file_content.encode('utf-8')
    content_base64 = b64encode(content_bytes).decode('utf-8')

    payload["content"] = content_base64

    # Make the request
    response = requests.put(api_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print("File created successfully.")
    else:
        print(f"Failed to create file. Status code: {response.status_code}")
        print(response.text)

# Call the function to create the file
create_file()
