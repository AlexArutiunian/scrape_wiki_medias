import json
import requests
from bs4 import BeautifulSoup

with open("output.json", "r", encoding="utf-8") as f:
    datas = json.load(f)

names = []

wiki = "https://en.wikipedia.org/wiki/"

for data in datas:
    name = data["page"]
    name = name.replace(" ", "_")
    names.append(name)
    req = requests.get(wiki + name)
    soup = BeautifulSoup(req.text, "html.parser")
    test = soup.find("div", class_="mw-content-container").get_text()
    if("does not have an article") in test:
      print("DOES not exist")
      continue
    print(wiki + name)
    trs = soup.find_all("tr")
   # print(trs)
   
    divs = soup.find_all("div", class_="mw-body-content")
    bio = str()
    for d in divs:
      bio += d.get_text()
    data["wiki"] = bio
    print(data)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(datas, f, indent=2)


