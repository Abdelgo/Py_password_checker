#library needed
import requests



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
    pass

request_api_data('123')
