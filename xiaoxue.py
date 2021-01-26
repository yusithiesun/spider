import urllib3
#import json
from pyquery import PyQuery as pq
import re

http = urllib3.PoolManager()  
# 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
response = http.request('GET', 'http://www.zuowen.com/xiaoxue/') 
# get方式请求
#print(response.status,response.data.decode('gb2312'))  
# 获得状态码, html源码(utf-8解码)
html=response.status,response.data.decode('gb2312')

doc=pq(html[1]) #创建pyquery对象doc
#print(type(doc))
#print(doc('href'))
d = doc('.tager .taglist [target=_blank]').not_('.buxian')
#筛选出想要的下一层链接
#json_obj=json.dumps(d)
#print(d.__dict__)
#print(str(d))
li=str(d).split(';',d.size())
pattern=re.compile("http.*[a-z]/")
#print(li[0])
for i in li:
    i=pattern.findall(i)
    print(i)
#print(d)
#print (d.not_('.buxian'))
#print(d.removeClass('.buxian'))
#print (d('a').html().split(';',1))
#print(json_obj)