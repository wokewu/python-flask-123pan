from flask import Flask,jsonify
from flask import request
import simplejson
import requests
import time
import os

#初始化
def start():
    cok='UM_distinctid=1811099c31e450-06af99d0df9f8c-4c647e53-1fa400-1811099c31f47d; Hm_lvt_d815f2e1f682c86565c1063aafaef292=1653840922,1656128121,1656177609; CNZZDATA1280304515=936831681-1653839152-https%253A%252F%252Fhello.sb%252F%7C1656174570; Hm_lpvt_d815f2e1f682c86565c1063aafaef292='
    t=str(int(time.time()))
    user='; username=用户账号; authorToken='
    coke=cok+t#+user
    headers={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': coke,
        'origin': 'https://www.123pan.com',
        'referer': 'https://www.123pan.com/login',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53',
    }
    posturl='https://www.123pan.com/b/api/user/sign_in'
    postdata={
        "passport": "用户账号",
        "password": "用户密码",
    }
    jsondata=requests.post(url=posturl,data=postdata,headers=headers)
    jsondata=jsondata.text
    print("-----------")
    return jsondata

#初始化
def timedataapi():
    timedata='0'
    return timedata

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    jiexi=request.args.get("jiexi")
    print(jiexi)
    jxpd=jiexi.split('-')[0]
    jiexi=jiexi.split('-')[1]
    #初始化
    #0print(timedata)
    if jxpd=='123pan':
        fd = open( 'time.txt','r',encoding="utf-8")
        timedata = fd.read()
        fd.close()
        timenew=int(time.time())
        if int(timedata) == 0 :
            timedata=str(int(time.time()))
            fd = open( 'time.txt','w',encoding="utf-8")
            fd.write(timedata)
            fd.close()
            jsondata=str(start())
            timenew=int(time.time())
            jsondata=simplejson.loads(jsondata)
            print(type(jsondata))
            fd = open( 'startdata.txt','a',encoding="utf-8")
            with open('friends.json', 'w') as f:
                simplejson.dump(jsondata, f)
            fd.close()
            authorToken=jsondata['data']
            authorToken=authorToken['token']
            #初始化
            cok='UM_distinctid=1811099c31e450-06af99d0df9f8c-4c647e53-1fa400-1811099c31f47d; Hm_lvt_d815f2e1f682c86565c1063aafaef292=1653840922,1656128121,1656177609; CNZZDATA1280304515=936831681-1653839152-https%253A%252F%252Fhello.sb%252F%7C1656174570; Hm_lpvt_d815f2e1f682c86565c1063aafaef292='
            t=str(int(time.time()))
            coke=cok+t
            user='; username=同上; authorToken='
            tokenend='; areaid=自己f12抓包; nickName=自己f12抓包'
            coke1=coke+t+user+authorToken+tokenend
            Bearer='Bearer '+authorToken
            headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'app-version': '1.1',
                'authorization': Bearer,
                'cookie':coke1,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53',
            }
            posturl='https://www.123pan.com/b/api/user/info'
            postdata=requests.get(url=posturl,headers=headers).text
            user='; username=同上; authorToken='
            tokenend='; areaid=同上; nickName=同上'
            coke=coke+user+authorToken+tokenend
            headers1={
                'authorization': Bearer,
                'cookie': coke,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53'
            }
            geturl='https://www.123pan.com/b/api/file/list/new'
            getdata='driveId=0&limit=100&next=0&orderBy=fileId&orderDirection=desc&parentFileId=0&trashed=false&SearchData=&Page=1'
            getdata1=requests.get(url=geturl,data=getdata,headers=headers1).text
            getdata1=simplejson.loads(getdata1)
            getdata1=getdata1['data']
            InfoList=getdata1['InfoList']
            Etag=jiexi
            for InfoList1 in InfoList:
                if Etag==InfoList1['Etag']:
                    playurl=InfoList1['DownloadUrl']
            print('下载地址:'+playurl)
            return jsonify(code='200' , url=playurl , 状态 ='成功' , 声明 ='本接口仅供学习交流-违法使用后果自负', 版权='蜗牛村长')
    
        elif int(timenew-30000) > int(timedata):
            print(timedata)
            jsondata = str(start())
            timedata=str(int(time.time()))
            print(timedata)
            fd = open( 'time.txt','w',encoding="utf-8")
            fd.write(timedata)
            fd.close()
            jsondata=simplejson.loads(jsondata)
            fd = open( 'startdata.txt','a',encoding="utf-8")
            with open('friends.json', 'w') as f:
                simplejson.dump(jsondata, f)
            fd.close()
            authorToken=jsondata['data']
            authorToken=authorToken['token']
            #初始化
            cok='UM_distinctid=1811099c31e450-06af99d0df9f8c-4c647e53-1fa400-1811099c31f47d; Hm_lvt_d815f2e1f682c86565c1063aafaef292=1653840922,1656128121,1656177609; CNZZDATA1280304515=936831681-1653839152-https%253A%252F%252Fhello.sb%252F%7C1656174570; Hm_lpvt_d815f2e1f682c86565c1063aafaef292='
            t=str(int(time.time()))
            coke=cok+t
            user='; username=同上; authorToken='
            tokenend='; areaid=同上; nickName=同上'
            coke1=coke+t+user+authorToken+tokenend
            Bearer='Bearer '+authorToken
            headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'app-version': '1.1',
                'authorization': Bearer,
                'cookie':coke1,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53',
            }
            posturl='https://www.123pan.com/b/api/user/info'
            postdata=requests.get(url=posturl,headers=headers).text
            user='; username=同上; authorToken='
            tokenend='; areaid=同上; nickName=同上'
            coke=coke+user+authorToken+tokenend
            headers1={
                'authorization': Bearer,
                'cookie': coke,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53'
            }
            geturl='https://www.123pan.com/b/api/file/list/new'
            getdata='driveId=0&limit=100&next=0&orderBy=fileId&orderDirection=desc&parentFileId=0&trashed=false&SearchData=&Page=1'
            getdata1=requests.get(url=geturl,data=getdata,headers=headers1).text
            getdata1=simplejson.loads(getdata1)
            getdata1=getdata1['data']
            InfoList=getdata1['InfoList']
            Etag=jiexi
            for InfoList1 in InfoList:
                if Etag==InfoList1['Etag']:
                    playurl=InfoList1['DownloadUrl']
            print('下载地址:'+playurl)
            return jsonify(code='200' , url=playurl , 状态 ='成功' , 声明 ='本接口仅供学习交流-违法使用后果自负', 版权='同上')
        else:
            print(timedata)
            fd = open( 'friends.json','r' )
            jsondata=simplejson.load(fd)
            fd.close()
            #jsondata=simplejson.load(jsondata)
            authorToken=jsondata['data']
            authorToken=authorToken['token']
            #初始化
            cok='UM_distinctid=1811099c31e450-06af99d0df9f8c-4c647e53-1fa400-1811099c31f47d; Hm_lvt_d815f2e1f682c86565c1063aafaef292=1653840922,1656128121,1656177609; CNZZDATA1280304515=936831681-1653839152-https%253A%252F%252Fhello.sb%252F%7C1656174570; Hm_lpvt_d815f2e1f682c86565c1063aafaef292='
            t=str(int(time.time()))
            coke=cok+t
            user='; username=同上; authorToken='
            tokenend='; areaid=同上; nickName=同上'
            coke1=coke+t+user+authorToken+tokenend
            Bearer='Bearer '+authorToken
            headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'app-version': '1.1',
                'authorization': Bearer,
                'cookie':coke1,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53',
            }
            posturl='https://www.123pan.com/b/api/user/info'
            postdata=requests.get(url=posturl,headers=headers).text
            user='; username=同上; authorToken='
            tokenend='; areaid=同上; nickName=同上'
            coke=coke+user+authorToken+tokenend
            headers1={
                'authorization': Bearer,
                'cookie': coke,
                'referer': 'https://www.123pan.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/103.0.5060.53'
            }
            geturl='https://www.123pan.com/b/api/file/list/new'
            getdata='driveId=0&limit=100&next=0&orderBy=fileId&orderDirection=desc&parentFileId=0&trashed=false&SearchData=&Page=1'
            getdata1=requests.get(url=geturl,data=getdata,headers=headers1).text
            getdata1=simplejson.loads(getdata1)
            getdata1=getdata1['data']
            InfoList=getdata1['InfoList']
            Etag=jiexi
            for InfoList1 in InfoList:
                if Etag==InfoList1['Etag']:
                    playurl=InfoList1['DownloadUrl']
            print('下载地址:'+playurl)
            return jsonify(code='200' , url=playurl , 状态 ='成功' , 声明 ='本接口仅供学习交流-违法使用后果自负', 版权='蜗牛村长')
    else:
        return jsonify(code='404' , url='' , 状态 ='成功' , 声明 ='本接口仅供学习交流-违法使用后果自负', 版权='蜗牛村长')
if __name__ == '__main__':
    timedata=timedataapi()
    app.config['JSON_AS_ASCII'] = False
    #app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"  # 指定浏览器渲染的文件类型，和解码格式；
    app.run(debug=True)
