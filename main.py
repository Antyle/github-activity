import sys
import request # is it this ?

print(sys.version) # print python version 


while True:
    try:
        username = input("Please enter a github username :")
    except ValueError:
        continue

def get_github_info(username):
    ...

if __name__ == '__main__':
    ...