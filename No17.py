import requests
import httpx


headers = {
    'User-Agent' : 'yuanrenxue.project',
    'cookie' : 'sessionid=hijd4ut9kq4fbrice79h4n4ck4lvi5dd',
}
api_url = 'https://match.yuanrenxue.com/api/match/17'
client = httpx.Client(http2=True,verify=False)
res = client.get(api_url,headers = headers)
sum = 0
for page in range(1,6):
    params = {
        'page' : page,
    }
    response_text = client.get(api_url,headers = headers,params=params)
    print(response_text.text)
    response = response_text.json()
    value = response['data']
    print(value)
    for i in value:
        sum += i['value']
print(sum)