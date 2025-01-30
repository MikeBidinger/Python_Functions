import requests
from github import Github
import base64
import json


def get_api_google_sheets_request(url):
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        content = response.content  # Get content
        data_string = content.decode("utf-8")  # Convert byte stream to string
        data_rows = data_string.split("\n")
        data = []
        for row in data_rows:
            data.append(row.split('"', 1)[1].rsplit('"', 1)[0].split('","'))
        return data
    else:
        print("File was not found:", url)


def get_api_github_request(url, object=True):
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        json_response = response.json()  # JSON response encoded base 64
        content = base64.b64decode(json_response["content"])  # Decode content
        json_string = content.decode("utf-8")  # Convert byte stream to string
        if object:
            return json.loads(json_string)  # Convert to JSON object (dict)
        else:
            return json_string
    else:
        print("File was not found:", url)


def put_api_github_request(url, token, data):
    r = requests.put(
        url,
        headers={"Authorization": "Token " + token},
        json={
            "message": "add new file",
            "content": base64.b64encode(data.encode()).decode(),
            "branch": "main",
        },
    )
    print(r.status_code)
    print(r.json())


def get_api(token, repo, file, dir=""):
    g = Github(token)
    repo = g.get_repo(repo)
    if dir != "":
        for content in repo.get_contents(dir):
            if content.name == file:
                response = content
                break
    else:
        response = repo.get_contents(file)  # Full response encoded base 64
    byte_stream = base64.b64decode(response.content)  # Decode content
    content = byte_stream.decode("utf-8")  # Convert byte stream to string
    return content


def put_api(token, repo, file, data, commit_message, branch, update=True):
    g = Github(token)
    repo = g.get_repo(repo)
    if update:
        f = repo.get_contents(file)
        repo.update_file(file, message=commit_message, content=data, sha=f.sha)
    else:
        repo.create_file(path=file, message=commit_message, content=data, branch=branch)


if __name__ == "__main__":

    SHEET_ID = ""  # https://docs.google.com/spreadsheets/d/{SHEET_ID}/
    SHEET_NAME = ""
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    data = get_api_google_sheets_request(url)
    print(data)

    TOKEN = ""
    REPO = ""  # {USER_NAME}/{REPO_NAME}
    DIR = ""
    FILE = ""
    content = get_api(TOKEN, REPO, FILE, DIR)
    print(content)

    if DIR != "":
        url = f"https://api.github.com/repos/{REPO}/contents/{DIR}/{FILE}"
    else:
        url = f"https://api.github.com/repos/{REPO}/contents/{FILE}"
    obj = get_api_github_request(url)
    print(obj)

    # put_api(token, repo, file, "123", "Create new file", "main", False)

    # put_api(token, repo, file, "123", "Update file content", "main")
