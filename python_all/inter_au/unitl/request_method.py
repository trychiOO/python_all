# coding: utf-8
import json
import requests
class mainMethod:
    def post_method(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, header=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()
    def get_method(self, url, params, header=None):
        if header != None:
            res = requests.get(url=url, params=params, header=header)
        else:
            res = requests.get(ur=url, params=params)
        return res.json()
    def main_Method(self, method, url, data, params, header):
        if method == 'psot':
            res = self.post_method(url, data, header)
        else:
            res = self.get_method(url, params, header)
        return res
