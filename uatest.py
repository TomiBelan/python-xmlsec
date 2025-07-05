from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlcleanup, urlopen, urlretrieve
import ssl

print(ssl.OPENSSL_VERSION)

url = 'https://www.aleksey.com/xmlsec/download/'
headers = {'User-Agent': 'https://github.com/xmlsec/python-xmlsec'}
request = Request(url, headers=headers)
with urlopen(request) as response:
    print(len(response.read()))
