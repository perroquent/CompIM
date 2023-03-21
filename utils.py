import requests
import os

CHUNK_SIZE = 32768
URL = 'https://docs.google.com/uc?export=download'


def download_file_from_google_drive(id, destination):
    print(f'# Downloading {destination}', end=' => ')
    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)
    print('Saved')


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def extract_image_names_recursive(top):
    img_exts = ['.jpg', '.jpeg', '.png']
    return [os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(top)
        for filename in filenames if os.path.splitext(filename)[1] in img_exts]