import requests
import hashlib  # sha1 hashing with this library


def request_api_data(querry_char):
    url = 'https://api.pwnedpasswords.com/range/' + querry_char  # kate anomity
    res = requests.get(url)
    # print(res)  # 200 means good
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def pwned_api_check(password):
    # check password if it exist in api response
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    # print(hashlib.sha1(password.hexdigest() # if not encoded it gives error to first convert
    # shah1password = hashlib.sha1(password.encode('utf-8'))
    first5char, tailchar = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    #print(response)
    return getpasswordleakcount(response, tailchar)


def getpasswordleakcount(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print (h, count)


pwned_api_check('123')
