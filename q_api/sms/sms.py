import json
import platform
import random



import requests
import q_api.sms.config as config



import q_api.sms.auth as auth
import random



# default_agent = {
#     'sdkVersion': 'python/4.2.0',
#     'osPlatform': platform.platform() + " | " + platform.python_version()
# }
#
#
# url = "http://api.coolsms.co.kr/messages/v4/send"
# headers = auth.get_headers('NCS8NC18VYMQRARY', ' C3C8PYYLBMIQXAFQHSPJ1M0LSUONVAUK')

# data = {
#     "message": {
#         "to": "01080128867",
#         "from": "01080128867",
#         "text": "안녕"
#     }
# }
#
#
# # print(json.dumps(data, ensure_ascii=False))
#
# response = requests.post(config.get_url('/messages/v4/send'),
#                          headers=auth.get_headers(config.api_key, config.api_secret),
#                          json=data)
#
# print(response.status_code)
# print(response.text)


def sms(to):
    code = ""
    data = {
        "message": {
            "to": "",
            "from": "01080128867",
            "text": ""
        }
    }
    for i in range(6) :
        code += str(random.randint(0,9))
    data["message"]["to"] = to
    data["message"]["text"] =f"당신의 인증번호는 {code}입니다."

    #설정들
    # default_agent = {
    #     'sdkVersion': 'python/4.2.0',
    #     'osPlatform': platform.platform() + " | " + platform.python_version()
    # }
    response = requests.post(config.get_url('/messages/v4/send'),
                             headers=auth.get_headers(config.api_key, config.api_secret),
                             json=data)
    return code,response


