import requests
from bs4 import BeautifulSoup as bs


def get_img_link(userName):
    url = "https://github.com/" + userName
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image_link = soup.find('img', {'alt' : 'Avatar'})['src']
    return profile_image_link


if __name__ == '__main__':
    print(get_img_link('rayala144'))
