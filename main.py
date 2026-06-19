import sys
import request # is it this ?
version = 1.0

def get_username():
    print(f"Script version {version}")
    while True:
        try:
            username = input("Please enter a github username :")
        except ValueError:
            continue
    print(f"The entered github username is {username}")
    

def get_github_info(username):
    ...
if __name__ == '__main__':
    get_username()    