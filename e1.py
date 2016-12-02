
import requests
import json
from bs4 import BeautifulSoup
election_address = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
response = requests.get(election_address)
soup = BeautifulSoup(response.content, "html.parser")
trs = soup.find_all("tr")
hayda = []
for row in trs:
    rowid = row.get("id")
    if rowid != None and "election-id" in rowid:
        baddehhol = rowid.replace("election-id-", "")
        year = row.find("td", attrs = {"class" : "year first"}).text
        alldata = year + " " + baddehhol
        hayda.append(alldata)
        print(year, baddehhol)
with open('ELECTION_ID', 'w') as f:
     json.dump(hayda, f) ### Not quite the format we requested but since it works for your e2 it's ok
