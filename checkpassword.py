from urllib import response
import requests
import hashlib
import sys


def request_api_data(query):

    url = "https://api.pwnedpasswords.com/range/" + query
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}\n"
                           "**Check the API and try again!")
    return response


def get_password_leaks_count(hashes, hash_to_check):

    hashes = (line.split(":") for line in hashes.text.splitlines())

    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pwned_api_check(password):

    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_head, tail = sha1pass[:5], sha1pass[5:]

    response = request_api_data(first5_head)
    return get_password_leaks_count(response, tail)


def main(args):

    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f"{password} was found {count} times.")
        else:
            print(f"{password} was not found! Good to go!")

    return "\ndone!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
