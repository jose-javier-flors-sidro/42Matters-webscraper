# Fetching and paging of the metadata
# HTTP POST
import requests


import json

import errors

class Connection:
    def __init__(self):
        self.os = ""
        self.keyword = ""
        self.categories = ""
        self.langs = ""
        self.token = ""

    def set_os(self,os):
        self.os = os

    def get_os(self):
        return self.os

    def set_keyword(self,keyword):
        self.keyword = keyword

    def get_keyword(self):
        return self.keyword

    def set_categories(self,categories):
        self.categories = categories

    def get_categories(self):
        return self.categories

    def set_langs(self,langs):
        self.langs = langs

    def get_langs(self):
        return self.langs

    def set_token(self,token):
        self.token = token

    def get_token(self):
        return self.token

    
    def get_data(self):
        data = []
        has_next = True
        page_number = 1

        while has_next:
            print('fetching page {}'.format(page_number))

            payload = {
                'query': {
                    'query_params': {
                        'full_text_term': '{keyword}'.format(keyword=self.keyword),
                        'include_full_text_desc':True, # When NOT commented, the web scraper also searches in the apps' full description
                         
                    }
                },
                'lang': self.langs
            }
            if (self.categories):
                payload['query']['query_params']['cat_keys'] = self.categories.split(',') 
            
            # API query
            urlToOpen = 'https://data.42matters.com/api/v2.0/{os}/apps/query.json?access_token={token}&page={page}'.format(os=self.os, keyword=self.keyword, token=self.token, page=page_number)
            r = requests.post(urlToOpen, data=json.dumps(payload))

            # Error handling
            if r.status_code == 400:
                raise errors.RequestNotValid
            if r.status_code == 402:
                raise errors.ExceededRequestError
            if r.status_code == 403:
                raise errors.AccessTokenError
            if r.status_code == 429:
                raise errors.RequestRateError
            if r.status_code == 443:
                raise errors.SecureChannelError
            if r.status_code >= 500:
                raise errors.ServerError

            temp_data = r.json()
            print('fetching done')
            has_next = temp_data['has_next']
            print('has next {}'.format(temp_data['has_next']))
            page_number += 1
            data.extend(temp_data['results'])

        return data