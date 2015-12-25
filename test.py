import asyncio
import http.client
import datetime



#建立连接
async def connection():
   
    conn = http.client.HTTPSConnection("www.baidu.com")
    conn.request("GET","/")
    res = conn.getresponse()
    if(res.status != ''):
        list.append(res.status)
    conn.close()


async def main():
    
    for i in range(10):
        
        await connection()


def result():
    sum = (end-start).seconds
    print(sum)
    print(list)
    print(len(list))

list = []
start = datetime.datetime.now()
tasks = [main(),main(),main(),main(),main(),main(),main()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = datetime.datetime.now()
result()

