import requests
import base64
import json


url = 'https://match.yuanrenxue.com/api/match/12'

def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

headers = {
    'User-Agent' : 'yuanrenxue.project',
    'Host' : 'match.yuanrenxue.com',
    'Referer' : 'http://match.yuanrenxue.com/match/6',
    'cookie' : 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1649919513; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1649919516; tk=-6986891110371688747; sessionid=hijd4ut9kq4fbrice79h4n4ck4lvi5dd; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1649919617; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1649920727'
}
sum = 0
for page in range(1,6):

    params = {
        'page' : page,
        'm' : encode_base64('yuanrenxue' + str(page)),
    }
    response_text = requests.get(url = url ,headers = headers,params=params)
    print(response_text.text)
    response = response_text.json()
    value = response['data']
    print(value)
    for i in value:
        sum += i['value']
print(sum)
