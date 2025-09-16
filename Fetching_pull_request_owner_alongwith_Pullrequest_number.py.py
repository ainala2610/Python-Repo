

# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/ainala2610/Python-Repo/pulls'

token = ''
headers = {
    'Authorization': f'{token}'                    # Provide the toke here
    'Accept': 'application/vnd.github.v3+json'
}

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url, headers=headers)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    #pr_creators = {}
    pull_requests_list = {}

    for pullid in pull_requests:
      pullrequest_id = pullid['number']
      print(pullrequest_id)
      if pullrequest_id in pull_requests_list:
          pull_requests_list[pullrequest_id] += 1
             #print(pull_requests_list)
      else:
        pull_requests_list[pullrequest_id] = 1


    print (pull_requests_list)
    print("Formated pull requests_id's:",list(pull_requests_list.keys()))

    count =  pull_requests_list.items()
    print("Total Number of pull requests:", len(pull_requests_list))

    for number in pull_requests_list:
        url2 = f'https://api.github.com/repos/ainala2610/Python-Repo/pulls/{number}'
        response1 = requests.get(url2)
        data2 = response1.json()
        pullrequest_owner = data2['user']['login']
        print(f"The Pull Request {number} has been reaised by :", pullrequest_owner)

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")




