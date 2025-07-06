from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlcleanup, urlopen, urlretrieve
import urllib.request
import ssl
import sys
import traceback

print(f"Python version: {sys.version}")
print(f"SSL version: {ssl.OPENSSL_VERSION}")
print(f"Default SSL context options: {ssl._DEFAULT_CIPHERS}")
print(f"Has SNI: {ssl.HAS_SNI}")
print(f"URLOpen default context: {urllib.request.urlopen.__globals__.get('context', 'not found')}")
print(f"{ssl.create_default_context().minimum_version = }")
print(f"{ssl.create_default_context().get_ciphers() = }")
for c in ssl.create_default_context().get_ciphers(): print('-', c['description'])

url = 'https://www.aleksey.com/xmlsec/download/'
headers = {'User-Agent': 'https://github.com/xmlsec/python-xmlsec'}
request = Request(url, headers=headers)
try:
    with urlopen(request) as response:
        print(len(response.read()))
except Exception:
    traceback.print_exc()

magic = ssl.create_default_context()
magic.minimum_version = ssl.TLSVersion.TLSv1_3
request = Request(url, headers=headers)
with urlopen(request, context=magic) as response:
    print(len(response.read()))
