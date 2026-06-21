import sys
import requests
version = 1.0

def get_username():
    print(f"Script version {version}")
    while True:
        try:
            username = input("Please enter a github username :")
            print(f"The entered github username is {username}")
            print("[DEBUG] : sending username to get_github_info")
            get_github_info(username)
        except ValueError:
            continue


def get_github_info(username):
    print("[DEBUG] : asking github api...")
    api_request(username)
    print(info)

def api_request(username):
    api = f"https://api.github.com/users/{username}/events"
    response = requests.get(api, timeout=10)
    if response.status_code == 200:
        print("Request sucessful")
        global info
        info = response.json()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_github_info(sys.argv[1])
    else:
        print("No argument, calling get_username...")
        get_username()   