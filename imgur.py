import os

from imgurpython import ImgurClient

CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')

client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

def upload_receive():
    image_path = '2024-08-16 22.23.12.jpg'
    uploaded_image = client.upload_from_path(image_path)

    image_url = uploaded_image['link']
    return image_url

print(f"Image URL: {upload_receive()}")