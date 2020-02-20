import requests
import json


# Format the dict for easy of reading as JSON
def jprint(obj):
    text_output = json.dumps(obj, sort_keys=True, indent=4)
    return print(text_output)


# Create a JSON web-token (JWT)
token=requests.post('http://127.0.0.1:5000/auth',
                        json={"username":"Alan","password":"testpassword"},
                        headers={'Content-Type': 'Application/json'})

# JWT token
token_value = token.json()['access_token']

# GET all the stored items, in the puppies list, using the API
all_pups = requests.get('http://127.0.0.1:5000/puppies', 
                        headers={'Authorization': 'JWT '+token_value})

# Print the string with the appearance of JSON object
jprint(all_pups.json()["puppies"])





