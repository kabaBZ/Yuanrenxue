import json
import requests
from selenium import webdriver

headers = {
    'User-Agent': 'yuanrenxue.project'
}
cookies_g = {
    'sessionid': "9jaju269e191ygfoytnkfxdjg6eek749",
}


def exec_js(js_str, url=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    if url:
        browser.get(url)
    result = browser.execute_script(js_str)
    browser.close()
    return result


if __name__ == '__main__':
    prices = 0
    count = 0
    session = requests.session()
    for key in cookies_g:
        session.cookies.set(key, cookies_g.get(key))
    js = """
        var timestamp = Date.parse(new Date()) + 100000000;
        var m = oo0O0(timestamp.toString()) + window.f;
        var m = m + '丨' + timestamp / 1000
        return m
        """
    m = exec_js(js, url='http://match.yuanrenxue.com/match/1')
    for page in range(1, 6):
        result = session.get(url='http://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(page, m),
                             headers=headers)
        result = json.loads(result.text)
        for data in result.get('data'):
            print(data)
            count += 1
            prices += data.get('value')
    print(prices/count)