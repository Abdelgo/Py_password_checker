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

def password_checker(allpass, hashtocheck,password):
    allpass = (line.split(':') for line in allpass.splitlines())
    print(hashtocheck)
    #print(list(allpass))
    for h, count in allpass:
        if h == hashtocheck:
            return count, password
        else:
            pass
    return 0,password


def password_searched(password):
    for i in password:
        print(i)
        pswrd = hashlib.sha1(i.encode('utf-8')).hexdigest().upper()
        firstchar, lastchar  = pswrd[:5], pswrd[5:]
        #print(f'1st5char : {firstchar} second part is : {lastchar}')
        response = request_api_data(firstchar)
        print(type(response))
        print(i)
        return password_checker(response, lastchar,i)




def passwordloop(thelist):
    count,password = password_searched(thelist)
    print(password)
    if count:
        print(f'your password {password} has been used {count} times')
    else:
        print(f'you can go with your {password} its okeyy')    

listr = ('batata','toto')
passwordloop(listr)
#request_api_data('123')
