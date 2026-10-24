
import requests
username = input("Enter GitHub username: ")

url = "https://api.github.com/users/" + username

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print("\nGitHub Profile")
    print("--------------------")
    print("Username:", user["login"])
    print("Name:", user["name"])
    print("Bio:", user["bio"])
    print("Followers:", user["followers"])
    print("Following:", user["following"])
    print("Public Repositories:", user["public_repos"])
    print("Profile URL:", user["html_url"])

    repo_url = url + "/repos"
    repo_response = requests.get(repo_url)

    if repo_response.status_code == 200:
        repositories = repo_response.json()

        print("\nRepositories")
        print("----------------")
        for repo in repositories:
            print("\nName:", repo["name"])
            print("Language:", repo["language"])
            print("Stars:", repo["stargazers_count"])
            print("Forks:", repo["forks_count"])
            print("URL:", repo["html_url"])

        if repositories:
            top_repo = repositories[0]
            for repo in repositories:
                if repo["stargazers_count"] > top_repo["stargazers_count"]:
                    top_repo = repo

            print("\nMost-Starred Repository")
            print("--------------------")
            print("Name:", top_repo["name"])
            print("Stars:", top_repo["stargazers_count"])
            print("URL:", top_repo["html_url"])

    else:
        print("Could not fetch repositories.")

elif response.status_code == 404:
    print("GitHub user not found.")

else:
    print("Error fetching GitHub profile.")