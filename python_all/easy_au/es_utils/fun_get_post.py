import requests
class fun_method:

    def send_get(self, url, params, headers, ):

        response = requests.get(url=url, params=params, headers=headers)
        return response

    def send_post(self, url, data, headers, ):
        response = requests.post(url, data, headers)

    def fun_main(self, url, params, data, headers, method):
        response = None
        if method == 'GET':
            response = requests.get(url=url, params=params, headers=headers)
        else:
            response = requests.post(url= url, data=data, headers= headers)
        return response
