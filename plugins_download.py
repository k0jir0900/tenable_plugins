import requests
from datetime import datetime
import os

# Define the API keys
ACCESS_KEY = 'api_access'
SECRET_KEY = 'api_secret'

# Define the size parameter
SIZE = 10000
PAGE = 1

# Define the API endpoint and headers
base_url = 'https://cloud.tenable.com/plugins/plugin'
headers = {
    'accept': 'application/json',
    'x-apikeys': f'accessKey={ACCESS_KEY};secretKey={SECRET_KEY}'
}

# Get the current date and time
current_datetime = datetime.now().strftime('%Y%m%d')

# Define the output CSV filename
csv_filename = f'plugins_tenable-{current_datetime}.csv'

# List to keep track of all filenames
filenames = []

while True:
    # Construct the URL with the current page and size
    url = f'{base_url}?size={SIZE}&page={PAGE}'

    # Make the GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # If the 'size' key in the response is 0 or 'plugin_details' list is empty, break the loop
        if data.get('size', 1) == 0 or not data['data']['plugin_details']:
            print('No more data to retrieve.')
            break

        # Create the filename with the current date and time
        filename = f'plugins_{current_datetime}-{PAGE}.json'

        # Append the response JSON to the file
        with open(filename, 'a') as file:
            file.write(response.text + '\n')
        print(f'Response appended to {filename}')

        # Add filename to the list
        filenames.append(filename)

        # Increment the page number
        PAGE += 1
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        break

# Check if any files were downloaded
if filenames:
    # Construct the cat and jq command to process the JSON files with a header
    cat_command = (
        f'echo "id,name,has_patch,exploit_available,risk_factor,cve" > {csv_filename} && '
        'cat ' + ' '.join(filenames) + " | jq -r '.data.plugin_details[] | "
        '{id: .id, name: .name, has_patch: (.attributes.has_patch), exploit_available: (.attributes.exploit_available), risk_factor: (.attributes.risk_factor), cve: (.attributes.cve[] // "")} '
        f'| [.id, .name, .has_patch, .exploit_available, .risk_factor, .cve] | @csv\' >> {csv_filename}'
    )

    # Execute the command
    os.system(cat_command)
    print(f'CSV file created: {csv_filename}')

    # Delete the JSON files
    for filename in filenames:
        os.remove(filename)
       # print(f'Deleted file: {filename}')
else:
    print('No files were downloaded.')
