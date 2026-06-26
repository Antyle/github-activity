import sys
import requests
version = 1.0

debug = False 

def get_username():
    print(f"Script version {version}")
    while True:
        try:
            username = input("Please enter a github username :")
            print(f"The entered github username is {username}")
            if debug == True: print("[DEBUG] : sending username to get_github_info")
            api_request(username)
        except ValueError:
            continue


def api_request(username):
    api = f"https://api.github.com/users/{username}/events"
    if debug == True: print("[DEBUG] : asking github api...")
    response = requests.get(api, timeout=10)
    if debug == True:  print(response.status_code) #debug only
    if response.status_code == 200:
        print("Request sucessful")
        global info
        info = response.json()
        print(info)
    else:
        print(f"an error occured, error {response.status_code}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        api_request(sys.argv[1])
    else:
        print("No argument, calling get_username...")
        get_username()   