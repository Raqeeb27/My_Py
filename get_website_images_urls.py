import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_images_from_html(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')

    image_urls = []
    for img_tag in img_tags:
        src = img_tag.get('src')
        if src:
            absolute_url = urljoin(base_url, src)
            image_urls.append(absolute_url)

    return image_urls

url = "https://"  # Enter URL
response = requests.get(url)
html_content = response.text

image_urls = get_images_from_html(html_content, url)
for i, image_url in enumerate(image_urls, start=1):
    print(f"Image {i}: {image_url}")