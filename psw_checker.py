#library needed
import requests
import hashlib


# function to communicate with api to check sha1 password looked for
def request_api_data(query_sha):
    url = 'https://api.pwnedpasswords.com/range/'+ query_sha
    res = requests.get(url)
    print(res.status_code)
    print(res.text)
    if res.status_code != 200:
        raise RuntimeError(f'status code error {res.status_code} check the API adress')
    else:
        return res



def password_searched(*args):
    passwrd = hashlib.sha1('koukou'.encode('utf-8')).hexdigest().upper()
    #print(encode(passwrd, 'utf-8'))
    print(passwrd)



password_searched(1)
#request_api_data('123')
