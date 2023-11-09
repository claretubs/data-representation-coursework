# Using the package PyGitHub to interact with GitHub
# Clare Tubridy

from config import config as cfg
from github import Github
import requests

apiKey = cfg["apiKey"]
g = Github(apiKey)

# Test
#for repo in g.get_user().get_repos():
#    print(repo.name)

repo = g.get_repo("claretubs/privateone")
#print(repo.clone_url)

file_info = repo.get_contents("text.txt")
url_of_file = file_info.download_url
#print(url_of_file)

response = requests.get(url_of_file)
content_of_file = response.text
#print(content_of_file)

new_contents = content_of_file + "more stuff \n"
#print(new_contents)

git_hub_response = repo.update_file(file_info.path, "updated by prog",
                                    new_contents, file_info.sha)
print(git_hub_response)