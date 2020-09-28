import requests


def getBaidu():
    r = requests.get('https://www.baidu.com')
    print(r)
    print(r.status_code)
    print(r.text)


def getParams():
    # 利用params传递额外的信息
    data = {'name': 'bill', 'age': 39}
    r = requests.get('http://httpbin.org/get', params=data)
    # json()生成dict
    json = r.json()

    print(r.text)
    print(json)
    print(type(json))
    print(r.content)


def getContent():
    r = requests.get('https://github.com/favicon.ico')
    # print(r.text)
    # print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def postData():
    data = {'name': 'bill', 'age': 39}
    r = requests.post('http://httpbin.org/post', data=data)
    print(r.text)
    print(r.json())


if __name__ == "__main__":

    # getBaidu()

    # 利用params传递额外的信息
    # getParams()
    # 抓取二进制数据
    # getContent()
    # post请求传递data
    postData()
