import requests
import json
from bs4 import BeautifulSoup

with open('ELECTION_ID') as f: hayda = json.load(f)
for x in hayda:
    link = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
    modifiedlink = link.replace("{}", x.split(" ")[1])
    resp = requests.get(modifiedlink)
    file_name = x.split(" ")[0] +".csv"
    with open(file_name, "w") as out: out.write(resp.text)
