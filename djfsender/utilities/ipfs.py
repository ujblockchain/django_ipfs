import requests
from django.conf import settings

# init upload url
url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'

#init payloads and header
payload = {}
headers = {'Authorization': f'Bearer {settings.PINETA_JWT}'}


def pin_file(file_name, file_location):

    # IPFS file pinning  with pineta
    payload = {
        'pinataOptions': '{"cidVersion": 1}',
        'pinataMetadata': '{"name": "%s", "keyvalues": {"company": "DJIPFS"}}' % (file_name),
    }

    files = [('file', (file_name, open(file_location, 'rb'), 'application/octet-stream'))]

    response = requests.request('POST', url, headers=headers, data=payload, files=files)

    return response.text
