# coding:utf-8
import json
import requests

basic_url = 'https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&pageNo={}&pageSize=30'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
path = "c:/Users/Administrator/Desktop/v1ssq"
for i in range(1, 2):
    url = basic_url.format(str(i))
    print(url)
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    htm = response.text
    # print(htm)
    try:
        data = json.loads(htm)
        arraydata = data.get("result")
        # print("data:", arraydata)
        lines = []
        for data in arraydata:
            code = data.get('code')
            red = data.get('red')
            blue = data.get('blue')
            line = "{}\t{}\t{}".format(code, red, blue)
            lines.append(line)
        with open(path + str(i) + ".txt", 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
    except json.JSONDecodeError as e:
        print("JSON解析错误:", e)
