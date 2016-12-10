#urllib

[TOC]

##1、最简单：直接抓取页面代码
```python
import urllib.request
import urllib.error

url = 'http://test.llq.com/test.html'
try:
    resp = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e.code, e.msg)
except urllib.error.URLError as e:
    print(e.reason)
else:
    result = resp.read().decode('utf-8')
    print(result)
```

##2、使用 Request
```python
import urllib.request
import urllib.error

url = 'http://test.llq.com/test.html'
try:
    req = urllib.request.Request(url)  # 构造一个Request对象，推荐
    resp = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code, e.msg)
except urllib.error.URLError as e:
    print(e.reason)
else:
    result = resp.read().decode('utf-8')
    print(result)

```


##3、发送数据，GET
```python
import urlib.request
import urllib.parse

url = 'http://test.llq.com/a.php?act=login&id=123'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

# or

url = 'http://test.llq.com/a.php'
params = {
    'act': 'login',
    'id': 123,
    'name': u'张三'
}
geturl = url + '?' + urllib.parse.urlencode(params)
req = urllib.request.Request(geturl)
resp = urllib.request.urlopen(req)

print(resp.read().decode('utf-8'))
# {"act":"login","name":"\u5f20\u4e09","id":"123"}
```

##4、发送数据，POST
```python
import urllib.request
import urllib.parse

url = 'http://test.llq.com/a.php'
params = {
    'act': 'login',
    'login[name]': u'张三',
    'login[password]': '123456'
}
data = urllib.parse.urlencode(params).encode('utf-8')

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

print(resp.read().decode('utf-8'))
# {"act":"login","login":{"password":"123456","name":"\u5f20\u4e09"}}}
```

## 5、发送数据和header
```python
import urllib.request
import urllib.parse

url = 'http://test.llq.com/a.php'
params = {
    'act': 'login',
    'login[name]': u'张三',
    'login[password]': '123456'
}
data = urllib.parse.urlencode(params).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.99 Safari/537.36',
    'Referer': 'http://www.baidu.com',
    'haha': 'xixi'
}

req = urllib.request.Request(url, data, headers)
resp = urllib.request.urlopen(req)

print(resp.read().decode('utf-8'))
```
