import requests
import hashlib #sha1 hashing with this library



def request_api_data(querry_char):
    url = 'https://haveibeenpwned.com/api/v3/range/' + querry_char   # kate anomity
    res = requests.get(url)
    #print(res)  # 200 means good
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')

def pwned_api_check(password):
    #check password if it exist in api response
    print(password.encode('utf-8'))
    # shah1password = hashlib.sha1(password.encode('utf-8'))


pwned_api_check('123')