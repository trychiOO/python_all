import json
import requests

class RanMian():
    def send_Post(self,url,data ):
        result = requests.post(url=url, data=data ).json()
        res = json.dump(result)
        return  res
    def send_Get(self,url):
        result = requests.get(url=url)
        res  = json.dump(result)
        return res

    def run_main(self ,method , data= None ,url = None):
        result = None
        if method =='post':
            result = self.send_Post()
        if method =='get':
            result= self.send_Get()
        else:
            print("method Error")
        return result