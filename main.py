import sys
import requests
version = 1.0
debug = True 

def get_username():
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
    if debug == True: print(response.status_code) # debug only
    if response.status_code == 200:
        print("Request sucessful")
        global info
        info = response.json()
        if debug == True: print(info)
        display_user_event(info)
    else:
        print(f"an error occured, error {response.status_code}")

def display_user_event(data):
    if debug == True: print("Data received")
    activities = data
    for activity in activities:
        if activity['type'] == 'WatchEvent':
            print(f"Followed the repo/organization {activity['repo']['url']}")
        if activity['type'] == 'PushEvent':
            print(f'Pushed to {activity['repo']['url']}')
        if activity['type'] == 'CreateEvent':
            print(f"Created {activity['repo']['name']}")

if __name__ == '__main__':
    print(f"Script version {version}")
    if len(sys.argv) > 1:
        api_request(sys.argv[1])
    else:
        print("No argument, calling get_username...")
        get_username()   