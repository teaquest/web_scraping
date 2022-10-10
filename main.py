import requests
from bs4 import BeautifulSoup

github_user = input("Input Github user: ")
# We will expect to get back a 200 code meaning it's successful

url = "https://github.com/" + github_user

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

profile_image = soup.find("img", {"class":"avatar avatar-user width-full border color-bg-default"})["src"]
print(profile_image)