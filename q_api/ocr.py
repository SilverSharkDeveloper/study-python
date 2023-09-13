# https://ocr.space/OCRAPI
import requests
import u_mysql.images
import json
import os


# url = "https://api.ocr.space/parse/imageurl?apikey=K84875884788957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true"
# print(json.dumps(data, ensure_ascii=False, indent=2))


def get_text(file_name):
    try:
        url = f"https://api.ocr.space/parse/imageurl?apikey=K81113553688957&url={file_name}&language=kor&isOverlayRequired=true"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['ParsedResults'][0]['ParsedText']
    except Exception as e :
        return False
