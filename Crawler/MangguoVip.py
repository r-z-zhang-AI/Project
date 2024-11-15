import requests

cookies = {
    '_source_': 'A',
    'Province': 'zhejiang',
    'xff': '2408:8642:893:32ec:513b:65cd:f163:bbaf',
    '__STKUUID': '5f1f3cc6-bda3-41d9-974d-037118263b1e',
    'mba_deviceid': 'b48723e1-9178-0ae0-7aa3-2353481a48d2',
    'mba_sessionid': '7f4175a4-6983-1999-5977-4f935a4e7f86',
    'mba_cxid_expiration': '1731686400000',
    'mba_cxid': '8kpqp21m4cm',
    'PLANB_FREQUENCY': 'ZzdIWqfh8QfDKQis_24111521',
    'MQGUID': '1857409519433465856',
    'beta_timer': '1731676252611',
    '__MQGUID': '1857409519433465856',
    'finger': '7b52f496ece388a30a1a4b559f1c9c5d',
    'uuid': 'e58a0ef73c7b51a087df4c4b7f9172d0',
    'loginAccount': '15534077112',
    'vipStatus': '1',
    'HDCN': '3944020CA69C3047937DF3D65A9C3AE0-602006816',
    'id': '12874466',
    'rnd': 'rnd',
    'wei': '18cf00d4c6d130daef2b66656938a3fb',
    'wei2': '9ffdUOYhS23kvQ9cvQByST1MTVYV%2F56D3pAPqVocIlgJb9NSDtNaFzI40F%2FfwWQhh7MsF5n56eXGybteXUeZzEUbmUXPv9FtLG2lwDe8scX%2Bznq8yV8Nl7sqsKDJu1DuR%2F%2F8wN0NdiQjjqBcX95v9Yl3MqPNCBOsJ7Zc7SxLoJeI5n6UHuB0KyMjpTQLKa6sAxTWrSiUPC%2FI56Q',
    'sessionid': '1731676303443_8kpqp21m4cm',
    'mba_last_action_time': '1731676445073',
    'lastActionTime': '1731676445467',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': '_source_=A; Province=zhejiang; xff=2408:8642:893:32ec:513b:65cd:f163:bbaf; __STKUUID=5f1f3cc6-bda3-41d9-974d-037118263b1e; mba_deviceid=b48723e1-9178-0ae0-7aa3-2353481a48d2; mba_sessionid=7f4175a4-6983-1999-5977-4f935a4e7f86; mba_cxid_expiration=1731686400000; mba_cxid=8kpqp21m4cm; PLANB_FREQUENCY=ZzdIWqfh8QfDKQis_24111521; MQGUID=1857409519433465856; beta_timer=1731676252611; __MQGUID=1857409519433465856; finger=7b52f496ece388a30a1a4b559f1c9c5d; uuid=e58a0ef73c7b51a087df4c4b7f9172d0; loginAccount=15534077112; vipStatus=3; HDCN=3944020CA69C3047937DF3D65A9C3AE0-602006816; id=12874466; rnd=rnd; wei=18cf00d4c6d130daef2b66656938a3fb; wei2=9ffdUOYhS23kvQ9cvQByST1MTVYV%2F56D3pAPqVocIlgJb9NSDtNaFzI40F%2FfwWQhh7MsF5n56eXGybteXUeZzEUbmUXPv9FtLG2lwDe8scX%2Bznq8yV8Nl7sqsKDJu1DuR%2F%2F8wN0NdiQjjqBcX95v9Yl3MqPNCBOsJ7Zc7SxLoJeI5n6UHuB0KyMjpTQLKa6sAxTWrSiUPC%2FI56Q; sessionid=1731676303443_8kpqp21m4cm; mba_last_action_time=1731676445073; lastActionTime=1731676445467',
    'origin': 'https://www.mgtv.com',
    'priority': 'u=1, i',
    'referer': 'https://www.mgtv.com/',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
}

params = {
    'allowedRC': '1',
    '_support': '10000000',
}

response = requests.get('https://u.api.mgtv.com/user/get_login_user', params=params, cookies=cookies, headers=headers)

# 虚拟机打开网站
