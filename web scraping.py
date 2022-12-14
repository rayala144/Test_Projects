import requests
from bs4 import BeautifulSoup as bs
github_user = input('Enter the github username: ')
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']

if __name__ == '__main__':
    print(profile_image)