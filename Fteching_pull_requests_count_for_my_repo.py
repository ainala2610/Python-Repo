
# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/ainala2610/Python-Repo/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    #pr_creators = {}
    pull_requests_list = {}

    for pullid in pull_requests:
      pullrequest_id = pullid['id']
      print(pullrequest_id)
      if pullrequest_id in pull_requests_list:
          pull_requests_list[pullrequest_id] += 1
             #print(pull_requests_list)
      else:
        pull_requests_list[pullrequest_id] = 1


    print (pull_requests_list)
    print("Formated pull requests:",list(pull_requests_list.keys()))

    count =  pull_requests_list.items()
    print("Total Number of pull requests:", len(pull_requests_list))

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
