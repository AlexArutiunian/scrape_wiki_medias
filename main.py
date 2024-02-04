import json
import requests
from bs4 import BeautifulSoup

file_in = "merge_res.json"

with open(file_in, "r", encoding="utf-8") as f:
    datas = json.load(f)

names = []

wiki = "https://en.wikipedia.org/wiki/"
count = 0
for data in datas:
    count += 1
    len_= len(datas)
    print(f"{count}/{len_}")
    
    if(data.get("wiki") != ""):
      print("IT is processed")
      continue  
    name = data["page"]
    name = name.replace(" ", "_")
    names.append(name)
    req = requests.get(data["wiki_link"])
    soup = BeautifulSoup(req.text, "html.parser")
    test = soup.find("div", class_="mw-content-container").get_text()
     
    if("does not have an article") in test:
      print("DOES not exist")
      continue
    
    print(data["wiki_link"])
   
    divs = soup.find_all("div", class_="mw-body-content")
    bio = str()
    for d in divs:
      bio += d.get_text()
    data["wiki"] = bio
    print(data)
    with open("data_.json", "w", encoding="utf-8") as f:
        json.dump(datas, f, indent=2)



