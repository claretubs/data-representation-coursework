# Program that reads a file from a repository,
# Replaces all the instances of the text "Andrew" with my name,
# Commits those changes and push the file back to the repository.
# Clare Tubridy

from config import config as cfg
from github import Github
import requests

def authenticate_github(apiKey):
    return Github(apiKey)

def get_file_content(repo, file_path):
    file_info = repo.get_contents(file_path)
    url_of_file = file_info.download_url
    return requests.get(url_of_file).text, file_info

def update_file(repo, file_info, new_content, commit_message):
    updated_content = new_content
    return repo.update_file(file_info.path, commit_message, updated_content, file_info.sha)

if __name__ == "__main__":

    apiKey = cfg["apiKey"]
    repo = "claretubs/privateone"
    file_path = "assignment04.txt"
    commit_message = "Updated Content"

    github_instance = authenticate_github(apiKey)
    repo = github_instance.get_repo(repo)

    current_content, file_info = get_file_content(repo, file_path)
    new_content = current_content.replace("Andrew", "Clare Tubridy")

    git_hub_response = update_file(repo, file_info, new_content, commit_message)

    print(git_hub_response)



    
