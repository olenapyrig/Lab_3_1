import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def in_put():
    account = str(input('Enter Twitter Account:'))

    return account


def features():
    lst_loc = []
    lst_name = []
    lst_id = []
    lst = ['id', 'location', 'name']
    s = str(input("Choose the option you want to get(location, name, id): "))
    for i in lst:

        s = str(
            input("Choose the option you want to get(location, name, id): "))
        if s in i:
            if s == 'location':
                lst_loc.append(s)
                return lst_loc
            elif s == "name":
                lst_name.append(s)
                return lst_id
            elif s == "id":
                lst_id.append(s)
                return lst_id
                break


def main(account):
    lst1 = []
    lst = features()

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': account, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    headers = dict(connection.getheaders())
    dct = {}
    lst = []
    for u in js['users']:
        d = {}
        for k, v in u.items():
            if k in lst:
                d[k] = v
        lst.append(d)
    dct['name'] =lst

    return dct


print(main(input()))
