![UJ Blockchain Logo](https://blockchain.uj.ac.za/static/images/main-logo.png)


# UJ Blockchain
South Africa-Switzerland Bilateral Research Chair in Blockchain Technology (UJ Blockchain) aims to explore blockchain integrations with real-world applications and development in Agric food.


## About Project.
DJIPFS uses django and PInata to store files in IPFS (Interplanetary File System). Files are first checked using Sha256 to check their hash using file byte string in memory before saving to a local directory. This is done to prevent duplicate. If a file has not been uploaded before after checking their unique hash, they are then uploaded to IPFS using Pinata API. The corresponding ipfs hash, pin size and timestamp are then save to the database along with other details. This project uses the pinata IPFS gateway to lookup files but you can use other gateways like Cloudflare IPFS gateway



## Setup
Set environment variable for Django Secret Key, Debug, Allowed Host, and Admin Path.

```
SECRET_KEY = '...'
DEBUG = ..
ALLOWED_HOSTS = '...'
ADMIN_PATH = '..'

```

### Pinata Credentials
Create an API key from your Pinata dashboard. API key and secrete can be gotten from https://app.pinata.cloud/. Ensure you use replace '...' with right details.

```
# pinata credentials
PINETA_JWT = '...'
PINETA_API_KEY = '...'
PINETA_API_SECRET = '...'

```


## Running Project

### Install Dependencies
```
$ poetry install

```

### Make Migrations
```
$ python manage.py makemigrations
$ python manage.py migrate

```

### create Superuser

```
$ python manage.py createsuperuser

```

### Run Server
```
$ python manage.py runserver

```