import requests

url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi"

querystring = {"scope":"103","format":"json","appid":"379020","bk_key":"time","bk_length":"600"}

headers = {'User-Agent': "PostmanRuntime/7.13.0",'Accept': "*/*",'Cache-Control': "no-cache",'Postman-Token': "fb5b4f0d-2cd6-40ad-9519-af01637b0703,804ce478-c28b-4602-812a-a20c0d635ad4",'Host': "baike.baidu.com",'cookie': "BAIDUID=F31FBAA9DB7982486721F423A367C98F:FG=1",'accept-encoding': "gzip, deflate",'Connection': "keep-alive",'cache-control': "no-cache"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())