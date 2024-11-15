import requests

cookies = {
    'buvid3': '5C23EC43-44EA-B7E7-7944-94FC9F27AE0311558infoc',
    'b_nut': '1724559711',
    '_uuid': '7108537DB-FB32-84FF-3E1B-A6FC1047C5E7612222infoc',
    'buvid_fp': '36d2f592fe1d922b0d4209118dc5af4d',
    'enable_web_push': 'DISABLE',
    'home_feed_column': '4',
    'buvid4': '8E64F3D7-3D32-920B-A26B-38EC15A2B1D412866-024082504-e%2FUQ2sCP1ZHg1zKm%2FtQDuw%3D%3D',
    'CURRENT_FNVAL': '4048',
    'rpdid': "|(YYl~R)YJk0J'u~kRllm~~Y",
    'DedeUserID': '3546750453287303',
    'DedeUserID__ckMd5': 'f6da692c64d39e09',
    'header_theme_version': 'CLOSE',
    'browser_resolution': '1225-596',
    'b_lsid': '465E998A_1932FD36CB0',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE5MzM0MDksImlhdCI6MTczMTY3NDE0OSwicGx0IjotMX0.RcmgcAegf1DO6Tv-EKAr6SAw97nNAymPiiYURMJF0HU',
    'bili_ticket_expires': '1731933349',
    'SESSDATA': '3ab55afa%2C1747226211%2C3972c%2Ab1CjDlgZAM8tBFePsWCf4piEYajAdS2NiwutH0rQi2pyHFmt6HrJ-uqWEQifIDV5QQW2QSVnJXcEpOUGNkWGhyeTZmcnd1M3o5UzZfOWRObENtYm53M2dHRzJqVnB5Q3g5TjlJc3REdkZKSkNSdmhNR3ZwUUpCWWJjalVXZWZyNUNBaFZnR0x4bUNRIIEC',
    'bili_jct': '9efe21f63fa5e35a7031e4c78b790e97',
    'sid': '8mruf3bx',
    'bp_t_offset_3546750453287303': '1000022928022044672',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': "buvid3=5C23EC43-44EA-B7E7-7944-94FC9F27AE0311558infoc; b_nut=1724559711; _uuid=7108537DB-FB32-84FF-3E1B-A6FC1047C5E7612222infoc; buvid_fp=36d2f592fe1d922b0d4209118dc5af4d; enable_web_push=DISABLE; home_feed_column=4; buvid4=8E64F3D7-3D32-920B-A26B-38EC15A2B1D412866-024082504-e%2FUQ2sCP1ZHg1zKm%2FtQDuw%3D%3D; CURRENT_FNVAL=4048; rpdid=|(YYl~R)YJk0J'u~kRllm~~Y; DedeUserID=3546750453287303; DedeUserID__ckMd5=f6da692c64d39e09; header_theme_version=CLOSE; browser_resolution=1225-596; b_lsid=465E998A_1932FD36CB0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE5MzM0MDksImlhdCI6MTczMTY3NDE0OSwicGx0IjotMX0.RcmgcAegf1DO6Tv-EKAr6SAw97nNAymPiiYURMJF0HU; bili_ticket_expires=1731933349; SESSDATA=3ab55afa%2C1747226211%2C3972c%2Ab1CjDlgZAM8tBFePsWCf4piEYajAdS2NiwutH0rQi2pyHFmt6HrJ-uqWEQifIDV5QQW2QSVnJXcEpOUGNkWGhyeTZmcnd1M3o5UzZfOWRObENtYm53M2dHRzJqVnB5Q3g5TjlJc3REdkZKSkNSdmhNR3ZwUUpCWWJjalVXZWZyNUNBaFZnR0x4bUNRIIEC; bili_jct=9efe21f63fa5e35a7031e4c78b790e97; sid=8mruf3bx; bp_t_offset_3546750453287303=1000022928022044672",
    'origin': 'https://space.bilibili.com',
    'priority': 'u=1, i',
    'referer': 'https://space.bilibili.com/380132202?spm_id_from=333.337.search-card.all.click',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
}

params = {
    'web_location': '333.999',
}

response = requests.get('https://api.bilibili.com/x/space/v2/myinfo', params=params, cookies=cookies, headers=headers)