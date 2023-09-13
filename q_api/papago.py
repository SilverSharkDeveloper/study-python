# https://developers.naver.com/docs/papago/papago-nmt-overview.md


import os
import sys
import urllib.request
import urllib.parse
import json

client_id = "Yh8ZyfE1QoJeDUiBOELc" # 개발자센터에서 발급받은 Client ID 값
client_secret = "LAWN5k454J" # 개발자센터에서 발급받은 Client Secret 값
url = "https://openapi.naver.com/v1/papago/n2mt"

def papago_api(sentence):
    encText = urllib.parse.quote(sentence)
    data = "source=ko&target=en&text=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()


    if rescode == 200:
        # 받은 데이터는 json이다.
        response_body = json.loads(response.read().decode('utf-8'))
        # json.loads(json)을 사용하여 dict로 변환한다.
        translatedText = response_body["message"]["result"]["translatedText"]
        return translatedText
    else:
        return False



