import http.client
import datetime

list = []
result = 1

for i in range(100):      //请求100次
    conn = http.client.HTTPSConnection("www.baidu.com")
    conn.request("GET","/")
    d1=datetime.datetime.now()
    res = conn.getresponse()
    if(res.status!=''):                 //判断状态码不为空值计算时间
        d2=datetime.datetime.now()
    conn.close()
    d=(d2-d1).microseconds     //计算微妙差值
    list.append(d)             //加入数组
print (list)
for i in list:  //加时间总和
    result = i+result
print(result/len(list)) //计算平均值
print(len(list))  //总个数
