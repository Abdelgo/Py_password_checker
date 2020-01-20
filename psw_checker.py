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
        raise RuntimeError(f'status code error {res.status_code} check the API adress\n')
    else:
        return res.text

#checking if the password have ever been used and how many times
def password_checker(allpass, hashtocheck):
    allpass = (line.split(':') for line in allpass.splitlines())
    #print(allpass) allpass is a generator that we can loop over!
    for h, count in allpass:
        if h == hashtocheck:
            return count
        else:
            pass
    return 0

#password transformation to SHA1 and split in 2 parts
def password_searched(password):
    pswrd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firstchar, lastchar  = pswrd[:5], pswrd[5:]
    #print(f'1st5char : {firstchar} second part is : {lastchar}')
    response = request_api_data(firstchar)
    return password_checker(response, lastchar)



#the password_loop over the list password to be checked
def passwordloop(thelist):
    for item in thelist:
        count = password_searched(item)
        if count:
            print(f"your password '{item}' has been used {count} times, you may change it for more security\n")
        else:
            print(f"you can go with your '{item}' password its okeyy\n")    


#starting the loop over the program
listr = ('batata','toto','seflkgdfkjdqsldkez')
passwordloop(listr)
