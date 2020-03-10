import requests

url = "http://127.0.0.1:12356/selectEq"

payload = "equipmentid=10003"
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
