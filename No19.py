import requests
import base64
import json
import urllib3
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
###考察浏览器指纹JA3

url = 'https://match.yuanrenxue.com/api/match/19'

headers = {
    'User-Agent' : 'yuanrenxue.project',
    'Host' : 'match.yuanrenxue.com',
    'Referer' : 'http://match.yuanrenxue.com/match/19',
    'cookie' : 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1649919513,1649942101,1650293126; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1649919516,1649942101,1650293134; tk=2177057098001530217; sessionid=2kvhmql98cy1nxjpw9dhk38a6ovmdfl4; Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1650702235; Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1650702235; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1650704515; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1650704531',
}
sum = 0
for page in range(1,6):
    params = {
        'page' : page,
    }
    response_text = requests.get(url = url ,headers = headers,params=params)
    print(response_text.text)
    response = response_text.json()
    value = response['data']
    print(value)
    for i in value:
        sum += i['value']
print(sum)
