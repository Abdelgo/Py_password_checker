#library needed
import requests
import hashlib


# function to communicate with api to check sha1 password looked for
def request_api_data(query_sha):
    url = 'https://api.pwnedpasswords.com/range/'+ query_sha
    res = requests.get(url)
    #print(res.status_code)
    #print(res.text)
    if res.status_code != 200:
        raise RuntimeError(f'status code error {res.status_code} check the API adress')
    else:
        return res.text



def password_searched(password):
    for i in password:
        pswrd = hashlib.sha1(i.encode('utf-8')).hexdigest().upper()
        firstchar, lastchar  = pswrd[:5], pswrd[5:]
        print(f'1st5char : {firstchar} second part is : {lastchar}')
        response = request_api_data(firstchar)
        print(response)



listr = ('password1', 'password2')
password_searched(listr)

#request_api_data('123')
