#urllib

1、最简单
```python
import urllib.request as request

url = 'http://test.llq.com/test.html'
resp = request.urlopen(url)
print(resp.read().decode('utf-8'))
```

2、使用 Request
```python
import urllib.request as request

url = 'http://test.llq.com/test.html'
req = request.Request(url)
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
```


3、发送数据
GET
```python
import urlib.request

url = 'http://test.llq.com/a.php?act=login&id=123'
req = urllib.request.Request(url, method='GET')

resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))
# {"act":"login","id":"123"}
```
POST
```python
import urllib.request
import urllib.parse

url = 'http://test.llq.com/a.php'

values = {
    'act': 'login',
    'id': '123'
}
data = urllib.parse.urlencode(values).encode('utf-8')

req = urllib.request.Request(url, data)
# req = urllib.request.Request(url, data, method='POST')

resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))
# {"act":"login","id":"123"}
```

4、发送数据和header
```python
import urllib.request
import urllib.parse

url = 'http://test.llq.com/a.php'

values = {
    'act': 'login',
    'login[name]': '张三',
    'login[password]': '123456'
}
data = urllib.parse.urlencode(values).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
    'Referer': 'http://www.baidu.com',
    'haha': 'xixi'
}

req = urllib.request.Request(url, data, headers)

resp = urllib.request.urlopen(req)
s = resp.read().decode('utf-8')
print(s)
```

5、http 错误
```python
import urllib.request
from urllib.error import HTTPError

url = 'http://test.llq.com/b.php'
req = urllib.request.Request(url)
try:
    urllib.request.urlopen(req)
except HTTPError as e:
    print(e.code, e.msg)
# 404 Not Found 
```

6、异常处理
```python
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = 'http://test.llq.com /a.php'  # url error
req = Request(url)
try:
    resp = urlopen(req)
except HTTPError as e:
    print('http error')
    print(e.code, e.msg)
except URLError as e:
    print('url error')
    print(e.reason)
else:
    print(resp.read().decode())
# url error
# [Errno 11004] getaddrinfo failed
```