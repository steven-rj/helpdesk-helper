import requests
import socket


def check_localhost():
    """Returns true if you are able to get the local host address"""
    local = socket.gethostbyname("localhost")
    return local == "127.0.0.1"


def check_connectivity():
    """Returns true if requests call gets a successful status code from a website"""
    request = requests.get("http://www.google.com")
    return request.status_code == 200


def main():

    print("\nRunning network diagnostics..")
    print("Checking localhost..")
    if not check_localhost():
        print("--pinging localhost ERROR!")
    else:
        print("--pinging localhost PASSED!")

    print("\nChecking internet connectivity..")
    if not check_connectivity():
        print("--pinging google.com ERROR!\n")
    else:
        print("--pinging google.com PASSED!\n")
