import requests

class Runmain:

    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers)
        return response
        # return json.dumps(response,sort_keys=True,indent=4)
 
    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url,params,headers)
        else:
            respose = self.send_post(url,data,headers)
        return respose
if __name__ == '__main__':
    ll = Runmain()
    hh = ll.send_get(url="https://www.baidu.com",params=None,headers=None)
    print(hh.status_code)
