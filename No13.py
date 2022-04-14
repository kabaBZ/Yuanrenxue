import requests
import re
session = requests.session()
headers = {
    'User-Agent' : 'yuanrenxue.project',
}
key,value = ['sessionid','hijd4ut9kq4fbrice79h4n4ck4lvi5dd']
session.cookies.set(key,value)
res = session.get('http://match.yuanrenxue.com/match/13',headers = headers)
# print(res.text)
reg = re.compile("'([a-zA-Z0-9=|_])'")
results = reg.findall(res.text)
# print(results)
cookie =  ''.join(results)
key,value = cookie.split('=')
session.cookies.set(key,value)
# key,value = ['sessionid','hijd4ut9kq4fbrice79h4n4ck4lvi5dd']
# session.cookies.set(key,value)

sum = 0
for page in range(1,6):
    params = {
        'page' : page,
    }
    api_url = 'https://match.yuanrenxue.com/api/match/13'
    session.headers = headers
    response_text = session.get(url = api_url ,params=params)#,headers = headers
    print(session.cookies)
    print(response_text.text)
    response = response_text.json()
    value = response['data']
    print(value)
    for i in value:
        sum += i['value']
print(sum)

# import re
# import requests
#
#
# cookie = {
#     'Cookie': 'sessionid=hijd4ut9kq4fbrice79h4n4ck4lvi5dd;'
# }
# headers = {
#     "User-Agent": "yuanrenxue.project",
# }
#
# url = 'http://match.yuanrenxue.com/match/13'
# session = requests.Session()
# # key,value = ['sessionid','hijd4ut9kq4fbrice79h4n4ck4lvi5dd']
# # session.cookies.set(key,value)
# response = session.get(url=url, headers=cookie)#
# com = re.compile("('(?P<cookie>.?)')")
# ret = com.finditer(response.text)
# cookie = ''
# for i in ret:
#     cookie += i.group('cookie')
# key, value = cookie.split('=')
# session.cookies.set(key, value)
#
# sum_list = []
# for page in range(1, 6):
#     api_url = f'http://match.yuanrenxue.com/api/match/13?page={page}'
#     ret = session.get(api_url, headers=headers)
#     print(ret.text)
#     for i in ret.json()['data']:
#         # print(i['value'])
#         sum_list.append(i['value'])
# print(sum(sum_list))