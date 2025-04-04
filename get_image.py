import requests

def get_image():
    # open file output/picuture.txt and get only the url inside parenthesis
    with open('output/picture.txt', 'r') as f:
        url = f.read().split('(')[1].split(')')[0]

    # download the image
    response = requests.get(url)
    with open('output/picture.jpg', 'wb') as f:
        f.write(response.content)
