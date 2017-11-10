import json
import time
import webbrowser
import requests

class YahooFantasySports:
    def __init__(self, credentials_file):
        self.credentials_file = open(credentials_file)
        self.credentials = json.load(self.credentials_file)   
        self.credentials_file.close()
        
        self.authorize_url = 'https://api.login.yahoo.com/oauth2/request_auth'
        self.access_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
        
        self.client_id = self.credentials['consumer_key']
        self.client_secret = self.credentials['consumer_secret']
        
        self.redirect_uri = 'oob'
                   
    def get_initial_tokens(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': 'oob',

            'response_type': 'code',
            'language': 'en-us',
        }

        res = requests.post(creds['authorize_url'], params=data, headers={ 'Content-Type': 'application/json'})
        webbrowser.open(res.url)
        
        code = input('Enter code: ')
        
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': 'oob',
            'code': code,
            'grant_type': 'authorization_code',
        }

        response = requests.post(creds['access_token_url'], data=data)

        self.set_tokens(response.json())

        
    def set_tokens(self, data):
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']

    def refresh_tokens(self):
        data = {
            'client_id': credentials['consumer_key'],
            'client_secret': credentials['consumer_secret'],
            'redirect_uri': 'oob',
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
        }
        response = requests.post(creds['access_token_url'], data=data)

        self.set_tokens(response.json())
