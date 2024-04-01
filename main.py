import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL_MAIN")
token = os.getenv("TOKEN")

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,mt;q=0.8",
    "Authorization": token,
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Dnt": "1",
    "Origin": "https://sg-play.mobilelegends.com",
    "Referer": "https://sg-play.mobilelegends.com/",
    "Sec-Ch-Ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "X-Actid": "2667211",
    "X-Appid": "2667210",
    "X-Lang": "id",
    "X-Token": token
}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
