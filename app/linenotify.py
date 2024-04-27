import requests
import os
import subprocess
from dotenv import load_dotenv

def main():
    send_line_notify('test message')

def send_line_notify(notification_message):
    load_dotenv()
    CLIENT_SECRET = os.getenv('API_KEY')
    line_notify_token = CLIENT_SECRET
    line_notify_api = 'https://notify-api.line.me/api/notify'

    try_count = 5
    for i in range(try_count):
#        request = requests.post(line_notify_api, headers = headers, data = data)
        post = send_image(line_notify_api, line_notify_token, 'images/image.png')

        if post.status_code == 200:
            print('message sent successfully')
            break
        else:
            print(f'Error: {post.status_code}')

    
    # headers = {'Authorization': f'Bearer {line_notify_token}'}
    # data = {'message': f'message: {notification_message}'}


def send_image(url, token, image_path):
    headers = {"Authorization" : "Bearer "+ token}

    message = '侵入者を検出しました. 画像を送信します.'

    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open('images/image.png','rb')}
    #rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)
    return post

if __name__ == "__main__":
    main()
