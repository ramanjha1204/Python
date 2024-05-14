import urllib.request
import re

url = "https://www.chat.openai.com/"
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(.*?)"', html)

