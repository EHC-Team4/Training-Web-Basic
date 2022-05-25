import requests
url = 'http://18.162.149.167/ehc'

headers = {
    'Host': '18.162.149.167',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'EHC',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'ccept-Encoding': 'gzip, deflate',

    'Accept-Language': 'ja',

    'Connection': 'close',
    'referer': 'http://18.162.149.167',
    'DNT' : '1',
    'Date' : '2017'
}
r = requests.get(url, headers=headers)
print(r.text)
